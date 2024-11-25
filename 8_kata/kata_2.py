# There was a test in your class and you passed it. Congratulations!
#
# But you're an ambitious person. You want to know if you're better than the average student in your class.
#
# You receive an array with your peers' test scores. Now calculate the average and compare your score!
#
# Return true if you're better, else false!

def better_than_average(class_points, your_points):
    average = (sum(class_points) + your_points) / (len(class_points) + 1)
    return your_points > average


print(better_than_average((3, 2),1))
