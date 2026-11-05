---
name: studio-a-blueprint
description: Create architectural and landscape renderings in the Studio A blue-violet and pale-cyan linework style, with white backgrounds, hatched skies, crisp sparse vegetation, and no people or text by default. Use for perspectives, sections, axonometrics, or mapping companion images when this style is requested; preserve supplied site geometry.
---

# Studio A Blueprint

Create restrained architectural and landscape illustrations using the written [visual specification](references/style.md). For adaptable scene language read [prompt templates](references/prompts.md); optionally use [the prompt builder](scripts/build_prompt.py), which produces text only and makes no network requests.

## Style defaults

- Fine blue-violet outlines, pale lavender shading, restrained pale-cyan accents and a pure white canvas. Use a strong hierarchy of principal and secondary lines.
- Fine horizontal sky hatching, sharp architectural edges, sparse plants with open branches and irregular leaf contours. Avoid cartoons, fuzzy edges, dense foliage and decorative stippling.
- No people, animals, vehicles, text or logos by default; retain functional elements required to explain the design.
- Adapt location, species, architecture, view and composition to the project. User instructions override defaults.

## Workflow

1. Identify user inputs as site/design source, edit target or layout reference. Preserve the project geometry, scale relationships and requested viewpoint. Do not invent precise site conditions from unclear inputs.
2. Use the host's available image-generation/editing tool for raster artwork and follow its instructions. Inspect local image inputs before editing. If generation is unavailable, provide a prompt and explain the limitation.
3. Construct the prompt from the style specification and the user's scene. Keep line hierarchy and palette coherent across any requested series. Do not impose a fixed panel count or location.
4. Inspect for geometry drift, unwanted entourage, weak linework, cartoon foliage or excessive texture. Revise important failures where feasible and disclose remaining limitations.
5. Save a new version in the requested project location, preserve original files and provide a preview. State that raster concept images are not surveyed drawings. User preferences determine whether to save a separate prompt.

## Exact mapping preservation

If the user asks to keep mapping unchanged, do not ask an image model to redraw it. Generate companion illustrations separately, then assemble alongside the original through a layout workflow allowed by the host and the user. Preserve the original map's geometry, crop, colors and orientation. If composition is unavailable, deliver separate illustrations and explain the limitation. Do not claim pixel-perfect preservation from generative editing.
