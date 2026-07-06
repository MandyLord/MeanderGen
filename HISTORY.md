</> Markdown
---
## Version 0.2

### Milestone 1 – The First Drawing

Today MeanderGen generated its very first SVG.

Although it is only a simple path, it represents the birth of the project.

The following core components had been completed:

- Geometry Engine
- Path
- SVG Writer
- First SVG Output

The file `examples/first_path.svg` has been permanently preserved as the first drawing ever created by MeanderGen.

---

The journey continues...

4th July 2026

Today MeanderGen drew its first line.

It wasn't a quilting pattern.

It wasn't even a curve.

It was simply proof that the Core Engine, the Path class and the SVG Writer could all work together.

From this point onwards, every future path would begin here.
Every great journey begins with a single path.

5th July 2026

Today MeanderGen completed its first independent movement.

The first Wander model generated a smooth curved path using heading memory.

It was only a short journey, but it proved that MeanderGen could begin choosing its own direction.
## 5th July 2026

Today MeanderGen completed its first successful local run on Mandy's computer.

After installing Python, GitHub Desktop and Visual Studio Code, MeanderGen generated and displayed its first independently created long walk from the local development environment.

Although only a simple curved path, it marked the beginning of MeanderGen running as a true software application rather than existing only as a GitHub repository.

**Development Session — Mandy & PathFinder completed the first Local Tea Test.**
Sprint 2.4C

Sprint 2.4C

• Created the new EdgeSteering helper class.
• Moved edge avoidance logic out of PathFinder.
• PathFinder now delegates edge steering to EdgeSteering.
• Successfully verified the refactor with Tea Test #7.

Sprint 2.5

• Added predictive (look-ahead) edge steering.
• EdgeSteering now evaluates a future position instead of the current position.
• Paths begin turning before reaching the canvas edge.
• Produces smoother, more natural wandering paths.

Sprint 2.6B

• Introduced a generic SteeringBehaviour base class.
• EdgeSteering now inherits from SteeringBehaviour.
• PathFinder now supports a list of steering behaviours.
• Steering adjustments are applied by iterating over all behaviours.
• Refactored architecture without changing path behaviour.

Sprint 2.6C

• BoundaryGuide now inherits from SteeringBehaviour.
• PathFinder no longer contains any special-case steering logic.
• All steering is now handled through a generic behaviour list.
• Completed the steering behaviour framework.

print 2.7M

Implemented the first working version of SelfAvoidance. The path now detects nearby previous points and applies a steering correction based on the direction to the nearest point and the distance from it. Initial behaviour is promising but requires tuning to reduce oscillations and prevent tight spirals.