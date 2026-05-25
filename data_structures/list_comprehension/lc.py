
big_arr = [4,5,13,2,44,8,20,39,9,1,3,7,6,11]

# To find the lowest number, we can use built-in `min` function
l = min(big_arr)
print(l)

# Or, we can write the logic ourselves

my_array = [7, 12, 9, 4, 11, 8]
minVal = my_array[0]

for i in my_array:
  if i < minVal:
    minVal = i

print('Lowest value:', minVal)

print(tuple(big_arr))

for i in big_arr:
    i = i * i
    print(i)

