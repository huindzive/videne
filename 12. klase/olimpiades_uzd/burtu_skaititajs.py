vards = "tava mamma ir zaglis"

burti = {}

for char in vards:
    if char.isalpha():
        burti[char] = vards.count(char)

print(burti)
sorted_dic = sorted(burti, key=burti.get, reverse=True)
print(sorted_dic)