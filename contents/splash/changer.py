#!/usr/bin/env python3

from pathlib import Path

configs = [
	["blue.gif",	"#000000", "500", "500"],
	["dune.gif",	"#000000", "700", "525"],
	["hud.gif",	"#000000", "700", "525"],
	["source.gif",	"#000000", "500", "500"],
	["sphere.gif",	"#000000", "500", "500"],
]

PATH = Path(__file__).parent

with open(PATH / "idx", "r+") as f:
	idx = int(f.read())
	nxt = (idx + 1) % len(configs)
	f.seek(0)
	f.write(str(nxt))
	f.truncate()

with open(PATH / "base.qml", "r") as f:
	script = f.read()

script = script.replace("REPLACE_IMAGE", configs[idx][0]).replace("REPLACE_COLOR", configs[idx][1]).replace(
	"REPLACE_WIDTH", configs[idx][2]).replace("REPLACE_HEIGHT", configs[idx][3])

with open(PATH / "Splash.qml", "w") as f:
	f.write(script)
