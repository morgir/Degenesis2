import re,sys
cults={"SPITALIANS":(50,53),"CHRONICLERS":(54,57),"HELLVETICS":(58,61),"JUDGES":(62,65),"CLANNERS":(66,70),"SCRAPPERS":(70,73),"NEOLIBYANS":(74,77),"SCOURGERS":(78,81),"ANUBIANS":(82,85),"JEHAMMEDANS":(86,89),"APOCALYPTICS":(90,93),"ANABAPTISTS":(94,97),"PALERS":(98,101)}
which=sys.argv[1:]
for c in which:
    a,b=cults[c]
    t=" ".join(open(f"{i:03d}.txt").read() for i in range(a,b+1))
    t=re.sub(r"\s+"," ",t)
    # cut at POTENTIALS
    ranks=t.split("POTENTIALS")[0]
    print("=====",c)
    for m in re.finditer(r"(\d|X|0) - ([A-ZÄÖÜ’'\.\- ]{3,40}?) (PREREQUISITE:.*?)(?=(?:\d|X) - [A-ZÄÖÜ’'\.\- ]{3,40}? PREREQUISITE:|$)",ranks):
        body=m.group(3)
        pre=re.search(r"PREREQUISITE:(.*?)(RESULT:|EQUIPMENT:|$)",body)
        res=re.search(r"RESULT:(.*?)(EQUIPMENT:|$)",body)
        eq=re.search(r"EQUIPMENT:(.*?)(?=\d - |RANKS|$)",body)
        print(f"{m.group(1)} {m.group(2).strip()} | P:{pre.group(1).strip()[:120] if pre else ''} | R:{res.group(1).strip()[:150] if res else ''} | E:{eq.group(1).strip()[:90] if eq else ''}")
