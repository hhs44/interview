list1 = [7, -8, 5, 4, 0, -2, -5]

print(sorted(list1, key=lambda x: (abs(x))))
print(sorted(list1, key=lambda x: (x < 0, abs(x))))
