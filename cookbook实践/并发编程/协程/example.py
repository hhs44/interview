def calc_avg():
    total, count = 0, 0
    avg_value = None
    while True:
        curr_value = yield avg_value
        total += curr_value
        count += 1
        avg_value = total / count
        

gen_obj = calc_avg()
gen_obj.send(None)

print(gen_obj.send(10))
print(gen_obj.send(20))
print(gen_obj)