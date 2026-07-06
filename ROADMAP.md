# MeanderGen Roadmap

## Version 0.3 – Organic Motion

- [ ] FlowSteering
- [ ] InertiaSteering
- [ ] Behaviour tuning
- [ ] Configuration experiments
- [ ] Unit tests

## Future Ideas

- [ ] Noise-based steering
- [ ] Goal attraction
- [ ] Spiral steering
- [ ] Embroidery optimisation
- [ ] SVG simplification
- [ ] Satin stitch planning

## Design Principles

- Randomness has memory.
- Steering corrections are immediate.
- Behaviours should be independent and composable.
- Geometry should remain independent of steering.

## Ultimate Goal

Generate a single continuous embroidery path that:

- Never self-intersects (except where a deliberate motif requires it).
- Maintains even spacing.
- Smoothly fills the available area.
- Can later incorporate decorative motifs.
- Produces designs suitable for machine embroidery.