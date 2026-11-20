# CV timeline illustrations — revision 3: detailed hand-drawn blue-pencil sketches

## Purpose

Regenerate every illustration in `images/timeline/` as a **rich but informal hand-drawn sketch**, using each ORIGINAL illustration on `master` as the authoritative content reference. **Do not trace, recolor, filter, or iterate on the simplified images currently in PR #18**: they have already lost details that need to be restored.

The approved young-Guiem sketch is a reference for *warmth, handmade quality, and character proportions*, not a restriction to five-line stick figures. The content of every original image takes precedence over radical minimalism.

## Essential visual direction

The picture should look as though an amateur-but-expressive artist sketched it in a personal notebook with a blue colored pencil or blue ballpoint pen. It should feel illustrated by hand, not constructed from precise geometry.

- Fine, naturally varying **blue pencil/ink strokes** on white paper (approximately navy blue #24528C; do not force one flat RGB value for every pixel).
- Hand-drawn, imperfect, slightly wandering contours. Uneven line pressure, occasional faint construction lines, and restrained scribbled shading where helpful to describe volume.
- Allow organic, irregular circles, hand-sketched laptop edges, loose curves and naturally imperfect straight lines.
- **No programmatic geometric primitives** (no ellipse/rectangle/polygon fonts composited using PIL, SVG, or Canvas). Draw each scene holistically through an image model or a human sketching process.
- No polished vector look, no mechanically consistent outlines, no computer-generated iconography, no glossy or gradient effects.
- **More detail than the previous PR version.** The objective is not a 45-second sketch. A warm, lively **5–10 minute notebook drawing** is a better target.

## Character identity

Keep a recognizable Guiem across all scenes, adjusted appropriately to each career stage.

- Slightly oversized but not balloon-sized head; simple expressive face and loose hair.
- **When the original wears glasses, preserve unmistakable glasses**: two slightly irregular frames surrounding eyes, connected by a bridge, with arms extending toward the ears. Avoid perfectly elliptical computer-drawn frames.
- Preserve a recognizable beard where present, hairstyle and length, clothing silhouette, graduation cap, headphones, pose, facial expression, gesture and any other distinctive details from the ORIGINAL scene.
- Bodies can be simplified and playful, but **do not insist on one-line stick torsos and limbs if this would lose meaningful identity, clothing, gestures, or posture**.

## Preserve details from the originals (critical)

**Use each master-branch JPEG as the source of truth.** Preserve:
1. The actual story, action, camera angle, composition and spatial relationships.
2. The identifiable props, objects and context (wheelchair, train, EEG cap, airplane, charts, clipboard, security shield, signed documents, laptop, books, symbols, etc.), at approximately their original positions.
3. Icon details and labels that identify the milestone: do not replace informative diagrams with generic symbols.
4. **ALL meaningful visible text, letters, numbers, labels, equations, signs and writing.** Transcribe spelling exactly from the original, at the same relative location, with comparable hierarchy and legibility.
5. For example, an ERP laptop must still say **ERP**; a CS book must still say **CS**; diagrams, chart markings and labels must remain interpretable.
6. If a marking is genuinely unreadable in the original, do not fabricate a plausible word. Preserve its rough appearance or flag it for review.

## Typography: hand lettering only

- **Every word and character must look like it was written by hand using the SAME blue pencil/pen.**
- Use irregular baselines, human letter shapes, gently varied spacing and weight, and restrained wobble consistent with the drawings.
- No system fonts, typeset letters, sterile monospaced computer text or synthetic stamped lettering.
- Letterforms must still be **accurate and clearly readable**.
- Prefer hand-rendered original lettering even when the source uses a conventional font, so the new series has a cohesive handmade quality.
- Verify every label character-by-character against the original at 100% zoom.

## Color and page treatment

Use blue pencil/pen strokes in a natural tonal range on clean white, optionally with subtle blue cross-hatching for depth. Preserve generous margins, but do NOT erase scene elements just to manufacture whitespace. Avoid solid gray circular backdrops and polished fills.

## Image-by-image procedure

For every one of the 13 filenames:
1. Open the **original `master:images/timeline/<filename>.jpg`** and make a checklist of *every* visual element and *every* text label.
2. Open the approved young-Guiem sketch only as a style reference.
3. Produce a **fresh image-to-image reinterpretation** from the original, not a postprocessing pass on the existing PR JPEG.
4. Inspect side by side at full resolution. Mark any dropped prop, missing character attribute, lost expression, typo, illegible text or machine-looking curve as a failure.
5. Revise individually until the scene is at least as semantically rich as the original while visually handmade.
6. Compare all 13 together for consistent character, stroke style, handwriting, blue color family and level of detail.

## Output / delivery

- Exactly 13 `.jpg` files, with original filenames and paths: `images/timeline/*.jpg`.
- Prefer the original aspect ratio and 900×900px target used in this PR; no cropping of content.
- Show a 13-image contact sheet **and** side-by-side original-vs-new pairs for approval.
- Replace JPEGs on the EXISTING branch `art/stick-figure-cv-timeline`, retaining PR #18; do not merge.
- Do not claim the artwork is revised until the replacement JPEG bytes are committed and reviewed.

## Negative prompt

Minimalist icon, corporate vector illustration, SVG geometry, perfect circles, perfect ellipses, uniform stroke width, Pillow-drawn lines, geometric diagram, generic clip art, cartoon sticker, chibi, kawaii, flat fills, gradients, perfectly typeset font, simplified text, omitted labels, meaningless pseudo-lettering, missing objects, generic laptop scene, excessively clean outlines.

**Acceptance test:** Someone comparing each drawing to the original should recognize the same scene and read the same labels, while sensing that it was naturally hand-sketched in blue pencil in a personal notebook.
