from .loop_blueprint import LoopBlueprint


blueprint = LoopBlueprint()

points = blueprint.build()

print("Number of points:", len(points))

for point in points:
    print(point)