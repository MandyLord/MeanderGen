
</> Markdown
## v0.4a

Implemented the planner's first decision-making capability.

- Added `DirectionPlanner.choose_turn()`.
- Planner now selects the highest-scoring candidate.
- Improved `planner_test.py` with a clear tabular display.
- Verified candidate selection through testing.

# Version 0.3 – Organic Motion

## Added

- Introduced FlowSteering to encourage smooth, flowing curves.
- Added inertia smoothing to reduce abrupt changes in direction.
- Added configurable look-ahead distance to SelfAvoidance.
- Improved SelfAvoidance with configurable recent segment exclusion.
- Created the project ROADMAP.md.
- Established design principles and the long-term project vision.

## Changed

- Refactored steering architecture to support more modular behaviours.
- Improved path smoothness through turn filtering.
- Continued development towards intelligent path planning.

## Notes

Version 0.3 concludes the reactive steering phase of MeanderGen.

The next major milestone (v0.4) introduces a new Direction Planner that will evaluate multiple candidate directions instead of reacting after a turn has already been chosen.

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

Sprint 2.8

Refactored SelfAvoidance to use configurable parameters (avoid_radius, max_turn, strength) instead of hard-coded values. No behavioural changes expected. This provides a flexible foundation for tuning different meander styles.

Milestone: Segment-Based Geometry

Introduced a LineSegment geometry class with reusable methods for vectors, projections and closest-point calculations. Refactored SelfAvoidance to steer away from the nearest path segment instead of the nearest stored point, laying the foundation for more advanced path-planning behaviours.

## Sprint 2.5 – Planner Boundary Fix

### Fixed
- Fixed a boundary scoring bug where points exactly on the boundary were treated as outside.
- Changed `BoundaryScore` from `distance <= 0` to `distance < 0`.
- Removed the continuous boundary-turning behaviour ("The Ugly Lollipop").

### Verified
- DirectionPlanner successfully evaluates SpaceScore, BoundaryScore and FlowScore.
- Planner correctly maintains a straight heading when no steering is required.
- Boundary penalties now apply only when candidates move outside the drawing area.

### Notes
The planner now behaves predictably. The next stage is to introduce controlled wandering behaviour so the path develops into a natural stipple rather than a straight line.

# Project History

- First Tea Test
- First Planner SVG
- The First Ugly Circle™
- The Ugly Lollipop™
- First Successful Boundary Fix
- The Stripe Revelation™
- Birth of Planner Phases