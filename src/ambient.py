# -*- coding: utf-8 -*-
"""Proceduralne pętle ambientu do przygody (numpy -> WAV -> OGG)."""
import numpy as np, wave, subprocess, os

SR = 22050
DUR = 96  # s
OUT = "/home/claude/degenesis2/assets/audio"
rng = np.random.default_rng(2595)
t = np.arange(int(SR * DUR)) / SR

def lowpass(x, a):
    y = np.empty_like(x); acc = 0.0
    for i in range(len(x)):  # prosty filtr jednobiegunowy (wystarczy dla ambientu)
        acc += a * (x[i] - acc); y[i] = acc
    return y

def lp_fast(x, k):
    """Filtr przez splot z oknem (szybszy)."""
    w = np.hanning(k); w /= w.sum()
    return np.convolve(x, w, mode="same")

def norm(x, peak=0.8):
    return x / (np.max(np.abs(x)) + 1e-9) * peak

def loopify(x, fade=3.0):
    """Bezszwowa pętla: przenikanie końca w początek."""
    n = int(fade * SR)
    head, tail = x[:n].copy(), x[-n:].copy()
    ramp = np.linspace(0, 1, n)
    x = x[:-n].copy()
    x[:n] = head * ramp + tail * (1 - ramp)
    return x

def drone(freqs, amp=0.2, wobble=0.05):
    s = np.zeros_like(t)
    for f in freqs:
        lfo = 1 + wobble * np.sin(2 * np.pi * rng.uniform(0.02, 0.07) * t + rng.uniform(0, 6))
        s += np.sin(2 * np.pi * f * t + 0.6 * np.sin(2 * np.pi * 0.11 * t)) * lfo
    return s * amp / len(freqs)

def wind():
    n = rng.standard_normal(len(t))
    gust = 0.5 + 0.5 * np.sin(2 * np.pi * 0.045 * t) * np.sin(2 * np.pi * 0.013 * t + 1)
    return lp_fast(n, 60) * (0.4 + gust)

def drips(rate=0.6, pitch=(900, 1600)):
    s = np.zeros_like(t)
    k = int(0.35 * SR); env = np.exp(-np.linspace(0, 9, k))
    for start in np.cumsum(rng.exponential(1 / rate, 400)):
        i = int(start * SR)
        if i + k >= len(t): break
        f = rng.uniform(*pitch)
        sweep = np.sin(2 * np.pi * (f * np.linspace(0, 0.35, k) + 300 * np.linspace(0, 0.35, k) ** 2))
        s[i:i + k] += sweep * env * rng.uniform(0.2, 0.6)
    # pogłos studni
    out = s.copy()
    for d, g in [(0.11, .5), (0.23, .35), (0.41, .22), (0.67, .12)]:
        sh = int(d * SR); out[sh:] += s[:-sh] * g
    return out

def pulse(bpm=48):
    s = np.zeros_like(t); k = int(0.5 * SR)
    env = np.exp(-np.linspace(0, 7, k)); thump = np.sin(2 * np.pi * 52 * np.linspace(0, 0.5, k)) * env
    period = 60 / bpm
    for beat in np.arange(0, DUR, period):
        for off, g in [(0, 1), (0.28, .6)]:
            i = int((beat + off) * SR)
            if i + k < len(t): s[i:i + k] += thump * g
    return s

def bells():
    s = np.zeros_like(t); k = int(5 * SR); env = np.exp(-np.linspace(0, 5, k))
    notes = [220, 261.6, 311.1, 392, 466.2]
    for start in np.arange(4, DUR - 6, 9.5):
        f = rng.choice(notes); i = int(start * SR); x = np.linspace(0, 5, k)
        s[i:i + k] += (np.sin(2 * np.pi * f * x) + .4 * np.sin(2 * np.pi * f * 2.76 * x)) * env * .3
    return s

def write(name, mono_l, mono_r=None):
    os.makedirs(OUT, exist_ok=True)
    l = loopify(norm(mono_l)); r = loopify(norm(mono_r)) if mono_r is not None else l
    st = np.stack([l, r], 1)
    wav = f"/tmp/{name}.wav"
    with wave.open(wav, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((st * 32767).astype(np.int16).tobytes())
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-c:a", "libvorbis", "-q:a", "3", f"{OUT}/{name}.ogg"], check=True)

if __name__ == "__main__":
    w1, w2 = wind(), wind()
    write("wiatr-nad-dzielnica", w1 + drone([55, 82.4, 110], .5), w2 + drone([55, 82.4, 110.5], .5))
    d = drips()
    write("studnia", d + drone([41.2, 61.7], .9, .02) + .15 * wind(), d * .8 + drone([41.2, 62], .9, .02) + .15 * wind())
    p = pulse()
    write("napiecie", p + drone([36.7, 55, 58.3], .7, .08), p + drone([36.7, 55.2, 58.3], .7, .08))
    b = bells()
    write("lazaret", b + drone([110, 130.8, 164.8], .45) + .1 * wind(), np.roll(b, int(.3 * SR)) + drone([110, 131, 164.8], .45) + .1 * wind())
    print(os.listdir(OUT))
