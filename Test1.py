# 21-Mar-2019
list = [1,5,9,3,7,3, 41, -2, 900]
# find largest number using rudimentary algo

y = range(len(list))
print (y)
max_value = 0
for i in y:
    if list[i] > max_value:
        max_value = list[i]
    #else:
    #    max_value = list[i+1]
    print (i, "|", list[i], "|", max_value)

print (f"Max value in give list = {max_value}")