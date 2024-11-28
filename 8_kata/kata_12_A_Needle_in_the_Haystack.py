# Can you find the needle in the haystack?
#
# Write a function findNeedle() that takes an array full of
# junk but containing one "needle"
#
# After your function finds the needle it should return a message (as a string)
# that says:
#
# "found the needle at position " plus the index it found the needle,

x = ['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]

def find_needle(haystack):
    index = haystack.index('needle')
    print("found the needle at position", str(index))

find_needle(x)
