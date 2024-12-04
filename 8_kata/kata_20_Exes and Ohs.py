# Check to see if a string has the same amount of 'x's and 'o's.
# The method must return a boolean and be case insensitive.
# The string can contain any char.
def xo(s):
    sum_x = 0
    sum_o = 0
    for i in s:
        if i.lower() == 'o':
            sum_o += 1
        if i.lower() == 'x':
            sum_x += 1
    if sum_x == sum_o:
        return True
    else:
        return False


print(xo("ooXx"))