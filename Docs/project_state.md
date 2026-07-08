# MeanderGen – Project State
**Last Updated:** v0.4 Development
**Authors:** Mandy Lord & Winston

---

# Vision

MeanderGen is a Python application that generates beautiful continuous-line
embroidery and quilting fill patterns.

The long-term goal is to produce designs that:

- consist of one continuous path
- avoid self-intersections (except where deliberately required by motifs)
- maintain even spacing
- naturally fill a region
- are suitable for machine embroidery
- later support decorative motifs (butterflies, birds, cats, etc.)

The emphasis is on elegant algorithms rather than randomness.

---

# Development Philosophy

The project is built using very small, testable steps.

Every new feature should:

- compile independently
- be tested independently
- avoid large rewrites
- keep responsibilities separated

The architecture is more important than rushing towards the final algorithm.

---

# Versions

## v0.1

Initial random path generation.

---

## v0.2 – Steering Framework

Completed.

Features:

- steering behaviour architecture
- boundary steering
- self avoidance
- modular steering system

GitHub Release published.

---

## v0.3 – Organic Motion

Completed.

Features:

- FlowSteering
- inertia smoothing
- configurable self avoidance
- look-ahead steering
- improved movement quality

Conclusion:

Reactive steering creates attractive wandering paths,
but cannot reliably produce the desired quilting fills.

GitHub Release published.

---

## v0.4 – Intelligent Direction Planning

Current development version.

This replaces reactive steering with intelligent planning.

The planner now evaluates multiple possible futures before moving.

---

# Current Architecture

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

Future Path Generator

---

# Current Project Structure

MeanderGen/

Docs/

examples/

gallery/

src/

tests/

.gitignore

README.md

ROADMAP.md

HISTORY.md

---

# Important Classes

## Candidate

Location:

src/candidate.py

Purpose:

Represents one possible future movement.

Current fields:

- heading
- position
- score

---

## DirectionPlanner

Location:

src/direction_planner.py

Current responsibilities:

- generate candidate headings
- predict future positions
- generate Candidate objects
- score candidates

Still to implement:

- choose_turn()

---

## DistanceScore

Location:

src/scoring/distance_score.py

Purpose:

First scoring class.

Currently returns a temporary score
(distance from origin) purely to verify
the scoring architecture.

This will later become:

distance from nearest existing path.

---

# Scoring Architecture

The planner owns:

self.scorers

Currently:

DistanceScore()

Future scorers will include:

BoundaryScore()

SpacingScore()

FlowScore()

DensityScore()

DeadEndScore()

MotifScore()

Each scorer contributes to a candidate's total score.

This keeps the planner independent from individual algorithms.

---

# Current Tests

planner_test.py currently demonstrates:

✔ candidate generation

✔ future position prediction

✔ candidate objects

✔ scoring

Current output shows Candidate objects
with different scores.

---

# Git Workflow

Development commits:

small

frequent

single-purpose

Releases:

v0.2

v0.3

Only create a GitHub Release for major milestones.

---

# .gitignore

Created.

Python cache files are now ignored.

Repository is clean.

---

# Coding Style

Prefer:

small classes

small methods

clear responsibilities

simple commits

incremental progress

Never add large features without testing.

---

# Ultimate Algorithm

Current approach:

Generate candidates

↓

Score candidates

↓

Choose highest score

↓

Move

Future scoring criteria:

distance from existing path

boundary safety

even spacing

open space preference

dead-end avoidance

smoothness

motif opportunities

The planner should eventually create
beautiful continuous fills rather than
random walks.

---

# Lessons Learned

Reactive steering improves movement quality
but does not solve space filling.

Planning ahead is the correct direction.

Candidate-based architecture is significantly
cleaner than continually adding steering
behaviours.

---

# Next Sprint

Implement:

DirectionPlanner.choose_turn()

Process:

1. Generate candidates.

2. Score candidates.

3. Select the highest scoring candidate.

Initially use Python's max() function.

No movement engine changes yet.

Only prove that the planner can
choose the highest scoring candidate.

---

# Long-Term Goals

Create embroidery-quality fills comparable
to commercial quilting software.

Later support:

butterflies

birds

cats

dogs

seasonal motifs

custom SVG motifs

without changing the planning engine.

The planner should remain generic while
motifs become plug-in components.

---

# Project Motto

Every beautiful path begins with one thoughtful step.