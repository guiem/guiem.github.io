#!/usr/bin/env python3
"""Make blue-pen line sketches from the ORIGINAL CV drawings on master.

Unlike the old refinement script, this always reads master JPEGs so original
hair, clothing, face, scene details and real lettering are never silently lost.
Each image is processed independently with gently wandering line contours.
"""
from __future__ import annotations
from io import BytesIO
from pathlib import Path
import math
import random
import subprocess
import numpy as np
import cv2
from PIL import Image, ImageDraw

REPO = Path("images/timeline")
FILES = [
    "guiem_ai.jpg", "guiem_atic.jpg", "guiem_caish.jpg",
    "guiem_coneptum.jpg", "guiem_cs_young.jpg", "guiem_cvi.jpg",
    "guiem_data_analyst_freelancer.jpg", "guiem_gfm.jpg",
    "guiem_kemlg.jpg", "guiem_mabrian.jpg", "guiem_psychology.jpg",
    "guiem_signaturit.jpg", "guiem_yoga.jpg",
]
BLUE = (24, 62, 151)
SIZE = 900
RNG_SEED = 1729

def original(name):
    payload = subprocess.check_output(["git", "show", f"origin/master:images/timeline/{name}"])
    return Image.open(BytesIO(payload)).convert("RGB")

def sketch(im, seed):
    rng = random.Random(seed)
    # Extract structural contours on the source artwork, including the actual
    # hair silhouette, facial hair, clothes and printed signs.
    source = np.asarray(im.resize((900, 900), Image.Resampling.LANCZOS))
    gray = cv2.cvtColor(source, cv2.COLOR_RGB2GRAY)
    smoothed = cv2.GaussianBlur(gray, (3,3), 0.8)
    edges_a = cv2.Canny(smoothed, 45, 135, L2gradient=True)
    edges_b = cv2.Canny(smoothed, 100, 210, L2gradient=True)
    # Deduplicate adjacent edges and discard tiny compression artifacts.
    edges = cv2.bitwise_or(edges_a, edges_b)
    contours,_ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    canvas = Image.new("RGB", (SIZE, SIZE), "white")
    d = ImageDraw.Draw(canvas)
    for ctr in contours:
        pts = ctr[:,0,:]
        if len(pts) < 11:
            continue
        arc = cv2.arcLength(ctr, True)
        if arc < 17:
            continue
        # Keep enough points for natural curves; let pen wander subtly.
        eps = max(0.35, min(1.1, arc*0.00055))
        simplified = cv2.approxPolyDP(ctr, eps, True)[:,0,:]
        if len(simplified) < 4: continue
        points=[]
        for i,(x,y) in enumerate(simplified):
            wobble = 0.68 if i%3 else 1.15
            points.append((int(x+rng.gauss(0,wobble)), int(y+rng.gauss(0,wobble))))
        points.append(points[0])
        col=(BLUE[0]+rng.randint(0,11),BLUE[1]+rng.randint(0,11),BLUE[2])
        d.line(points,fill=col,width=rng.choice((1,2,2,2,3)),joint="curve")
    # A very sparse hand-hatching layer on original dark-tone areas.
    # This preserves the source silhouette, rather than redrawing generic props.
    mask = cv2.resize(gray, (450,450), interpolation=cv2.INTER_AREA)
    for yy in range(22, 435, 12):
        offset = rng.randint(-3,3)
        for xx in range(22+offset,435,12):
            v=int(mask[yy,xx])
            if v < 115 and rng.random()<0.47:
                x=xx*2; y=yy*2
                length=rng.randint(8,16)
                d.line([(x,y+length//2),(x+length,y-length//2)],
                       fill=(89,117,188),width=1)
    # No added text or invented props: all strokes derive from master.
    return canvas

def main():
    REPO.mkdir(parents=True, exist_ok=True)
    for i,name in enumerate(FILES):
        image = sketch(original(name), RNG_SEED+i)
        image.save(REPO/name,format="JPEG",quality=94,optimize=True,subsampling=0)
        print("Replaced from master:",name)

if __name__ == "__main__":
    main()
