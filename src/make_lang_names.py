import json
_L = json.load(open('/home/claude/degenesis2/lang/pl.json'))
SKILL_PL = _L['D2']['Skill']
BG_PL = {k: v for k, v in _L['D2']['Background'].items() if k in ["sojusznicy","autorytet","slawa","zasoby","sekrety","siec"]}
