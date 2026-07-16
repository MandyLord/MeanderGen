from src.traveller import Traveller
from src.rectangle_boundary import RectangleBoundary
from src.boundary_query import BoundaryQuery


traveller = Traveller(
    x=20,
    y=30,
    heading=105,
)

boundary = RectangleBoundary(
    left=0,
    top=0,
    right=120,
    bottom=80,
)

distance = BoundaryQuery.distance_to_boundary(
    traveller,
    boundary,
)

print(f"Distance to boundary: {distance}")