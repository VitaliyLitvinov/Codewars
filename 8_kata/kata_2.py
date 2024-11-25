# There was a test in your class and you passed it. Congratulations!
#
# But you're an ambitious person. You want to know if you're better than the average student in your class.
#
# You receive an array with your peers' test scores. Now calculate the average and compare your score!
#
# Return true if you're better, else false!

def better_than_average(class_points, your_points):
    average_point_class = sum(class_points) / len(class_points)
    if average_point_class <= your_points:
        return True
    else:
        return False


print(better_than_average((3, 2),1))
