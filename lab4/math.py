import math

#Convert degree to radian
degree = 15
radian = math.radians(degree)
print(f"Input degree: {degree}")
print(f"Output radian: {radian:.6f}")

#Calculate the area of a trapezoid
height = 5
base1 = 5
base2 = 6
area_trapezoid = ((base1 + base2) / 2) * height
print(f"\nHeight: {height}")
print(f"Base, first value: {base1}")
print(f"Base, second value: {base2}")
print(f"Expected Output: {area_trapezoid}")

#Calculate the area of a regular polygon
num_sides = 4
side_length = 25
area_polygon = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
print(f"\nInput number of sides: {num_sides}")
print(f"Input the length of a side: {side_length}")
print(f"The area of the polygon is: {area_polygon:.1f}")

#Calculate the area of a parallelogram
base_length = 5
height_parallelogram = 6
area_parallelogram = base_length * height_parallelogram
print(f"\nLength of base: {base_length}")
print(f"Height of parallelogram: {height_parallelogram}")
print(f"Expected Output: {area_parallelogram:.1f}")
