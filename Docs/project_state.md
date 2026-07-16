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

v0.6 – Arc-Based Planning (planned)

Vision

Movement should be described in terms of graceful arcs rather than independent headings.

New Components
Arc
ArcFollower
Planner chooses arcs.
ArcFollower converts arcs into headings.
PathFinder executes movement.
Philosophy

The planner decides artistic intent.

The ArcFollower performs graceful motion.

The engine should use quilting language wherever practical.


Hand over document
MeanderGen – Project State

Last Updated: End of Prototype A / Beginning of Prototype B
Authors: Mandy Lord & Winston

Vision

MeanderGen is a Python application that generates beautiful continuous-line embroidery and quilting fill patterns.

The long-term goal is to produce designs that:

consist of one continuous path
avoid self-intersections
maintain even spacing
fill arbitrary shapes
produce quilting patterns comparable to commercial stipple software

This is a quilting engine that happens to output geometry, not a generic path planner.

Current Status

Prototype A is complete.

Prototype A successfully demonstrated:

continuous path generation
smooth curved movement
modular project architecture
SVG generation
geometry and path handling
movement abstraction using sweeps

However it does not produce recognisable stipple quilting.

The current output is essentially a gently wandering line.

The conclusion reached is that the movement algorithm itself must change, not simply be refined.

Keep

The following parts of the project are considered solid foundations and should remain.

Geometry
Point
LineSegment
Geometry utilities
Path
Path
nearest_distance()
segment handling
SVG
svg_writer
development SVG output
State

Current State contains

position
heading
step_number
path
previous_turn
step_length
phase

This structure remains useful.

Arc

Represents one quilting sweep.

Contains

direction
curvature
remaining_steps
finished

Advance() now decrements correctly only once.

ArcFollower

Responsible only for following an existing sweep.

Future responsibility:

convert a Sweep into headings
know when a sweep has finished

Not responsible for deciding which sweep comes next.

Replace

The following concept is considered complete and should no longer drive development.

Current movement model:

heading
↓

heading
↓

heading
↓

heading

This has reached its limits.

The project should no longer evolve this algorithm.

New Direction

The engine should work at the quilting level rather than the heading level.

The important objects become

Patch

↓

Sweep

↓

Companion Sweep

↓

Neighbouring Patch

Movement is driven by space filling, not heading generation.

Quilting Knowledge (from Mandy)

These are now considered requirements rather than observations.

Q1

Start from an edge.

If the shape has corners, start in a corner.

Q2

Priority while quilting

Boundary
Empty space
Previous stitching line
Current direction
Q3

A local area is considered full when

no remaining gap is wide enough to accommodate another sweep.

Q4

Tiny gaps

Ignore them.

Noticeable gaps

Fill immediately if it flows naturally.

Otherwise return later.

Q5

Companion sweeps should naturally lead into the next area whenever possible.

Deliberate travel movements are acceptable when necessary.

New Development Rule

Every coding session must introduce one visible quilting behaviour.

Examples:

hugs boundary
creates companion sweep
fills first patch
leaves patch naturally

If a coding session cannot be expected to produce a visibly different SVG, reconsider the implementation before writing code.

Development Philosophy

The project will now proceed by implementing quilting behaviours, not by tuning parameters.

Every proposed code change should answer:

What quilting behaviour does this implement?
Why does it belong in the final engine?
What visible difference should appear in the SVG?
Immediate Goal

Milestone: First Ugly Stipple

Success is defined as:

A continuous path that an experienced quilter would recognise as attempting to fill space rather than simply wandering.

It does not need to be beautiful.

It does need to be recognisably different from the current output.

Winston's Commitments
No more tuning constants unless there is a clear behavioural reason.
No more refactoring that cannot affect visible output.
Each session begins by defining a single quilting behaviour.
Code only after agreeing what visible change should result.
Build the real engine, not demonstrations or shortcuts.
Mandy's Development Rule

"Every new piece of code should make a noticeable difference."

This is now considered a core project principle.

Personal Note

Tonight was probably the most important design discussion we've had.

Not because of the code we wrote, but because we agreed to change how MeanderGen is developed.

Prototype A taught us how to generate smooth continuous movement.

Prototype B will teach MeanderGen how to quilt.

I think this is a good place to close this chapter.

And tomorrow (this time I mean our next chat, not while we're apart! 😄), we'll start with one clear objective:

Teach MeanderGen its first genuine quilting behaviour and produce the first ugly stipple.

I'm looking forward to it, Mandy. I have a good feeling that this next chapter is where MeanderGen will really begin to come alive.


