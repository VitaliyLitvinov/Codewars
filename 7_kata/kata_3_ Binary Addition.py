# Implement a function that adds two numbers together and
# returns their sum in binary. The conversion can be done before,
# or after the addition.

# The binary number returned should be a string.
def add_binary(a,b):
    bin = a + b
    return format(bin, 'b')
