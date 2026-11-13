#!/usr/bin/env python3
"""Refine PR #18's 13 existing black-pen doodles into blue-pen sketches.

Usage: python scripts/refine_timeline.py
Run once on the original black-ink drawings, not repeatedly on outputs.
"""
from pathlib import Path
from PIL import Image, ImageDraw
import random, math

ROOT=Path("images/timeline")
BLUE=(32,76,142)
FACES={
 "guiem_ai":(305,330),"guiem_atic":(275,360),
 "guiem_caish":(300,358),"guiem_coneptum":(335,355),
 "guiem_cvi":(365,375),"guiem_data_analyst_freelancer":(341,353),
 "guiem_gfm":(343,369),"guiem_kemlg":(335,350),
 "guiem_mabrian":(323,355),"guiem_psychology":(320,355),
 "guiem_signaturit":(311,367),
}
def oval(cx,cy,rx,ry,seed):
    rng=random.Random(seed)
    return [(cx+rx*math.cos(2*math.pi*i/42)+rng.uniform(-.75,.75),
             cy+ry*math.sin(2*math.pi*i/42)+rng.uniform(-.75,.75))
             for i in range(43)]
def improve(path):
    im=Image.open(path).convert("RGB")
    if im.size!=(900,900):
        raise ValueError(f"Unexpected dimensions for {path}: {im.size}")
    converted=[]
    for r,g,b in im.getdata():
        strength=(255-(r+g+b)/3)/255
        converted.append(tuple(round(255*(1-strength)+c*strength) for c in BLUE))
    out=Image.new("RGB",im.size)
    out.putdata(converted)
    if path.stem in FACES:
        x,y=FACES[path.stem]
        d=ImageDraw.Draw(out)
        for i,(dx,dy) in enumerate(((-35,4),(32,1))):
            d.line(oval(x+dx,y+dy,29,24,f"{path.stem}-{i}"),
                   fill=BLUE,width=4,joint="curve")
        d.line([(x-6,y-2),(x-2,y-6),(x+4,y-6)],fill=BLUE,width=4)
        d.line([(x-64,y+3),(x-85,y-8)],fill=BLUE,width=4)
        d.line([(x+61,y+2),(x+86,y-6)],fill=BLUE,width=4)
        # Very sparse beard/stubble, preserving stick-figure simplicity.
        for offset in (-24,-6,13,30):
            d.arc((x+offset-6,y+64,x+offset+7,y+79),
                  190,340,fill=BLUE,width=2)
    out.save(path,format="JPEG",quality=95,optimize=True,subsampling=0)

if __name__=="__main__":
    paths=sorted(ROOT.glob("guiem_*.jpg"))
    if len(paths)!=13:
        raise RuntimeError(f"Expected 13 illustrations, found {len(paths)}")
    for path in paths:
        improve(path)
        print("Updated",path)
