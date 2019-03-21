# 21-Mar-2019
list = [9,3,7,41,-2,90]
# find largest number using rudimentary algo
y = range(len(list))
max_value = 0
for i in list:
    if i > max_value:
        max_value = i
    print (i, "|", i, "|", max_value)
print (f"Max value in give list = {max_value}")