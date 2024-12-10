# This time no story, no theory. The examples
# below show you how to write function accum:
#
# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
def accum(st):
    num = 0
    idx = 0
    text = ''
    for i in st:
        text += i.upper() + st[idx].lower() * num + '-'
        idx += 1
        num += 1
    return text[:-1]
print(accum('ZpglnRxqenU'))
