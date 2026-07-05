Sprint 1.2A - The First Path
New files
src/path.py
tests/test_path.py
examples/first_path.py
The Path class is now the central object in MeanderGen.
Everything else will eventually operate on a Path.
Sprint 1.2B - First Drawing
New:
src/svg_writer.py
examples/create_first_path.py
examples/first_path.svg
Milestone:
MeanderGen has created its first SVG.
Sprint 2.0A - The First Wander
Sprint 2.0B – The First Wander
New features:
Wander now has turn memory.
Added gallery.
Added first_wander example.
Added first_wander SVG.
Sprint 2.1 - The Long Walk
Longer 1000-step example
Smoother Wander
Gallery milestone 0003
Sprint 2.2 Part 2A
Added the first Boundary module.
This sprint introduces Rectangle geometry and edge-distance
calculations. No steering behaviour has been added yet.
Sprint 2.2 Part 2B
Added BoundaryGuide and integrated optional steering into PathFinder.
Sprint 2.3A
Improved Wander movement.
Introduces a slowly drifting target turn.
Produces longer, smoother arcs.
Deterministic with a fixed random seed.
