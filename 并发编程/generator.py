

def create_num(all_num):
    a, b = 0, 1

    current_num = 0
    while current_num < all_num:
        # print(a)
        ret = yield a
        a, b = b, a + b
        current_num += 1




nums = create_num(100)
for num in nums:
    print(num)





