# MeanderGen Quilting Instincts

This document describes how a human quilter thinks while creating a
continuous stipple pattern.

It deliberately avoids describing programming techniques.

Every behaviour added to MeanderGen should represent a genuine quilting
instinct rather than a method of drawing a particular shape.

If an algorithm cannot be explained as a quilting instinct, it does not
belong in the engine.

MeanderGen Engine

Purpose

Generate continuous quilting paths.


# Core Principles

1. Keep the needle moving.

2. Prefer smooth flowing curves over long straight lines.

3. Continue generally forwards unless there is a good reason not to.

4. End a curve because it feels complete, not because of an arbitrary number.

5. The boundary should be treated like another line of stitching.

6. Empty space can usually be filled later.

7. Never deliberately create sharp points or abrupt changes of direction.

8. Small variations are natural. Predictability is not.


The engine does NOT know about
flowers
berries
butterflies
motifs
The engine DOES know about
flow
spacing
boundaries
empty space
rhythm
Every behaviour added to the engine must answer

What quilting instinct does this implement?

A quilting instinct should influence every stitch, not every few stitches.

## Instinct 1 – Keep Moving

Description

A quilter rarely travels in a perfectly straight line.
The hand is always making small, smooth adjustments.

Reason

Continuous movement creates a flowing path and avoids
mechanical-looking stitching.

Status

✔ Prototype implemented

## Core Principle

Prefer many small flowing curves over a few large curves.

A curve should naturally finish while it is still pleasing.

The engine should rarely produce large sweeping arcs unless
there is a good quilting reason to do so.

# Order of Quilting Decisions

The engine should think in the same order as a human quilter.

1. Create a pleasant flowing curve.
2. Decide when that curve has done its job.
3. Avoid travelling somewhere undesirable.
4. Fill remaining empty space later.

The engine should never try to solve all of these
problems simultaneously.

# Design Principles

Every behaviour added to the engine must represent a genuine
quilting instinct rather than a drawing technique.

The engine should make decisions using quilting concepts,
not mathematical ones.

Examples:

- "This curve feels big enough."
- "I don't want to head over there."
- "I'll keep generally moving forwards."
- "I can come back and fill that gap later."

- Following predefined arcs does not produce natural stippling.

- Continuous steering without knowing when to stop produces giant loops.

- Randomness should only add variation.
  It should never be the primary source of movement.

- Curves create the spaces.
  The engine should not chase empty spaces first.

- The engine must remember what it has been doing.

# The Tea Test

Before adding a new behaviour, ask:

"Is this something Mandy would naturally do while quilting?"

If the answer is no...

...don't add it.

# Development Rule

Every development session should satisfy all three of these conditions:

1. The behaviour being added must represent a genuine quilting instinct.

2. The expected effect on the generated stitching should be predictable before the code is run.

3. After running the engine, compare the prediction with the result and explain any differences before writing more code.

