
import random
from typing import List, Tuple

Point = Tuple[float, float]

def point_in_polygon(x: float, y: float, poly: List[Point]) -> bool:
    # Ray casting algorithm
    inside = False
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        # Check if edge crosses horizontal ray to the right of (x, y)
        if ((y1 > y) != (y2 > y)):
            x_intersect = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x_intersect > x:
                inside = not inside
    return inside

def monte_carlo_area_polygon(poly: List[Point], samples: int = 200_000, seed: int = 42) -> float:
    random.seed(seed)

    xs = [p[0] for p in poly]
    ys = [p[1] for p in poly]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)

    box_area = (maxx - minx) * (maxy - miny)

    inside = 0
    for _ in range(samples):
        x = random.uniform(minx, maxx)
        y = random.uniform(miny, maxy)
        if point_in_polygon(x, y, poly):
            inside += 1

    return (inside / samples) * box_area

# Example polygon (replace with your irregular shape points)
polygon = [(0,0), (4,1), (3,4), (1,3), (-1,2)]

area_est = monte_carlo_area_polygon(polygon, samples=300_000)
print("Estimated area:", area_est)

