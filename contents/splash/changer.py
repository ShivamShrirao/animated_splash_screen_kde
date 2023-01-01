#!/usr/bin/env python3

import os
from pathlib import Path

from PIL import Image

PATH = Path(__file__).parent

gifs = os.listdir(PATH / "images" / "choices")

configs = []
for gif in gifs:
    img = Image.open(PATH / "images" / "choices" / gif)
    w, h = img.size
    if w < 1000:
        h = int((h * 1000 / w))
        w = 1000

    dims = (str(w), str(h))
    config = [gif, "#000000", *dims]
    configs.append(config)

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
