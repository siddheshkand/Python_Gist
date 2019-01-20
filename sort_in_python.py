# Sort all different types of object
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
tu = (9, 1, 8, 2, 7, 3, 6, 4, 5)  # tuple does not have sort() method
s_li = sorted(li, reverse=True)

print("Unsorted list " + str(li))
print("Sorted list " + str(s_li))

# Sort without creating new variable

print("li Before" + str(li))
li.sort(reverse=True)  # inplace modify i.e. it sort li in same array do not return sorted list
print("li After" + str(li))
