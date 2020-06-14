#!/usr/bin/env python3

configs = [
	["blue.gif",	"#000000", "500", "500"],
	["dune.gif",	"#000000", "700", "525"],
	["hud.gif",	"#000000", "700", "525"],
	["source.gif",	"#000000", "500", "500"],
	["sphere.gif",	"#000000", "500", "500"],
	["vert.gif",	"#000000", "500", "530"],
]

PATH = "/home/archer/.local/share/plasma/look-and-feel/QuarksSplashDark/contents/splash/"

with open(PATH+"idx", "r") as f:
	idx = int(f.read())

nxt = (idx + 1) % len(configs)

with open(PATH+"idx", "w") as f:
	f.write(str(nxt))

with open(PATH+"base.qml", "r") as f:
	script = f.read()

script = script.replace("REPLACE_IMAGE", configs[idx][0]).replace("REPLACE_COLOR", configs[idx][1]).replace(
	"REPLACE_WIDTH", configs[idx][2]).replace("REPLACE_HEIGHT", configs[idx][3])

with open(PATH+"Splash.qml", "w") as f:
	f.write(script)
