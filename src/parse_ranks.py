import re, subprocess, sys
def page_text(p):
    return subprocess.run(["./cols.sh", str(p)], capture_output=True, text=True).stdout
pages = [int(x) for x in sys.argv[1:]]
t = "\n".join(page_text(p) for p in pages)
t = re.sub(r"(\w)-\n(\w)", r"\1\2", t)          # dzielenie wyrazów
lines = t.split("\n")
blocks, cur = [], None
for ln in lines:
    m = re.match(r"^([0-9XO]) - (.+)$", ln.strip())
    if m:
        cur = [m.group(1), re.sub(r"(?<=\b\w) (?=\w\b)", "", m.group(2)).strip(), ""]; blocks.append(cur); continue
    if cur is not None:
        cur[2] += " " + ln.strip()
for lvl, name, body in blocks:
    body = re.sub(r"\s+", " ", body)
    pre = re.search(r"PREREQUISITE:(.*?)(RESULT:|EQUIPMENT:|$)", body)
    res = re.search(r"RESULT:(.*?)(EQUIPMENT:|$)", body)
    eq = re.search(r"EQUIPMENT:(.*?)$", body)
    r = res.group(1).strip() if res else ""
    print(f"[{lvl}] {name} | P: {pre.group(1).strip() if pre else '-'} | R: {r[:260]} | E: {(eq.group(1).strip()[:140]) if eq else '-'}")
