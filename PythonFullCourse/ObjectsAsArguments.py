# objects as arguments: Passing objects as arguments to functions
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def display_point(point):
    print(f"({point.x}, {point.y})")

p = Point(3, 4)
display_point(p)  # Output: (3, 4)
