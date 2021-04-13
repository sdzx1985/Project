import re

p = re.compile("ca.e")
# . (ca.e) : one word > care, cafe, case | caffe
# ^ (^de) : start point > desk, destinatio | fade
# $ (se$) : end point > case, base | face

def print_match(m):
    if m:
        print(m.group()) # matchs string
        print(m.string) # inserted string
        print(m.start()) # matched string's starting index
        print(m.end()) # matched string's ending index
        print(m.span()) # matched string's starting / ending index
    else:
        print("No matching")

# 1.
# m = p.match("case") # match : check from the start
# print_match(m)

# 2.
# m = p.search("good care") # search : check among the string
# print_match(m)

# 3.
lst = p.findall("careless") # findall : return every matched as a list
print (lst)

