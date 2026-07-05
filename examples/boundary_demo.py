from src.boundary import Rectangle
from src.geometry import Point

rect = Rectangle(0,0,200,150)
pt = Point(35,40)

print(rect.contains(pt))
print(rect.distances(pt))
