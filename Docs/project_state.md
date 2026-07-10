# MeanderGen – Project State
**Last Updated:** v0.4 Development
**Authors:** Mandy Lord & Winston

---

MeanderGen – Project State

Last Updated: v0.5 Development
Authors: Mandy Lord & Winston

Vision

MeanderGen is a Python application that generates beautiful continuous-line embroidery and quilting fill patterns.

The long-term goal is to produce designs that:

consist of one continuous path
avoid self-intersections (except where deliberately required by motifs)
maintain even spacing
naturally fill a region
are suitable for machine embroidery
later support decorative motifs (butterflies, birds, cats, etc.)

The emphasis is on elegant algorithms rather than randomness.

Development Philosophy

The project is built using very small, testable steps.

Every new feature should:

compile independently
be tested independently
avoid large rewrites
keep responsibilities separated

The architecture is more important than rushing towards the final algorithm.

A new guiding principle emerged during v0.5:

Never invent a new scorer until the SVG tells us we need one.

Behaviour should always be driven by observation rather than guesswork.

Versions
v0.1 – Random Walk

Completed.

Features:

initial continuous path generation
v0.2 – Steering Framework

Completed.

Features:

steering behaviour architecture
boundary steering
self avoidance
modular steering system

GitHub Release published.

v0.3 – Organic Motion

Completed.

Features:

FlowSteering
inertia smoothing
configurable self avoidance
look-ahead steering
improved movement quality

Conclusion:

Reactive steering creates attractive wandering paths but cannot reliably produce quilting fills.

GitHub Release published.

v0.4 – Intelligent Direction Planning

Completed.

Major features:

Candidate generation
Candidate scoring
DirectionPlanner
SpaceScore
BoundaryScore
FlowScore
Planner integrated into PathFinder
First planner-generated SVG successfully produced
v0.5 – Planner Validation

Current development version

Major achievements:

Planner successfully drives the movement engine.
Multiple scoring classes operate together correctly.
Extensive debugging tools added.
Behaviour analysed through SVG output.
First behavioural bugs identified and corrected.

Major fixes:

SpaceScore

Corrected an infinite scoring bug caused when no path segments existed.

Result:

planner no longer always selected the first candidate.
BoundaryScore

Corrected boundary handling:

Changed

if distance <= 0:

to

if distance < 0:

Result:

eliminated the continuous boundary loop ("The Ugly Lollipop™")
points exactly on the boundary are now considered valid
Current Architecture
Geometry
    ↓
Path
    ↓
Candidate Generation
    ↓
Candidate Scoring
    ↓
Direction Planner
    ↓
PathFinder
    ↓
SVG Writer

The complete planning pipeline is now operational.

Current Project Structure
MeanderGen/

docs/
examples/
gallery/
src/
tests/

README.md
ROADMAP.md
HISTORY.md
PROJECT_STATE.md
Important Classes
Candidate

Purpose:

Represents one possible future movement.

Current fields:

heading
position
score
breakdown
DirectionPlanner

Current responsibilities:

generate candidate headings
predict future positions
generate Candidate objects
evaluate scorers
record score breakdowns
choose best heading
PathFinder

Current responsibilities:

execute planner decisions
update heading
generate continuous paths
maintain movement state
Current Scorers

Implemented:

SpaceScore
BoundaryScore
FlowScore

Future scorers:

DensityScore
DeadEndScore
MotifScore
Current Testing

Current debugging tools include:

planner score tables
per-scorer breakdown
heading selection logging
SVG preview generation
start/end markers
development mode visualisation

These proved invaluable during planner debugging.

Lessons Learned

Major lessons from v0.5:

Hard penalties should only be used for impossible moves.
Preference scores should gently influence behaviour.
Visual debugging is significantly more effective than numerical debugging alone.
Behaviour should be understood before introducing additional algorithms.
Building in small verified steps dramatically reduces debugging complexity.
Current Status

The planner is now stable.

Current behaviour:

chooses headings correctly
updates movement correctly
respects boundaries correctly
produces deterministic paths

The planner currently favours perfectly straight movement.

This is expected.

The next stage is to teach it controlled, natural wandering.

Next Sprint – Sprint 2.6

Objective:

Teach the planner to wander gracefully.

Goals:

introduce gentle heading variation
preserve smooth movement
maintain boundary awareness
preserve self-avoidance
begin producing the first recognisable stipple behaviour

No new scorers should be added unless the generated SVG demonstrates a genuine need.

Git Workflow

Development commits should remain:

small
frequent
single-purpose

GitHub Releases should continue to represent major architectural milestones only.

Long-Term Goals

Produce embroidery-quality continuous fills comparable to commercial quilting software.

Future extensions:

butterflies
birds
cats
dogs
seasonal motifs
user-supplied SVG motifs

These should become plug-in components while leaving the planning engine unchanged.

Project Motto

Every beautiful path begins with one thoughtful step.

😊 One tiny addition I'd love to make

Right at the bottom, I'd add a little "Project History" section. Not technical—just the memorable moments.

# Project History

- First Tea Test
- First Planner SVG
- The First Ugly Circle™
- The Ugly Lollipop™
- First Successful Boundary Fix

Beautiful quilting emerges from maintaining consistent spacing, not from seeking maximum empty space.