def better_than_average(class_points, your_points):
    sum = 0
    for i in class_points:
        sum += i
    sum = sum / len(class_points)
    return sum < your_points

print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50)) # False