dict1={'Welcome': 10, 'to': 2, 'my': 10, 'class': 10}
print("Dictionary: " + str(dict1))
x = 10
res = 0
for key in dict1:
    if dict1[key] == x:
        res = res+1
print("Frequency of 10 : " + str(res))