def times2(a): return a * 2
def div2(a): return a / 2
def exp2(a): return a ** 2

my_list = [2, 4] 

mapped_times2 = map(times2, my_list)
mapped_div2 = map(div2, my_list)
mapped_exp2 = map(exp2, my_list)

mapped_times2_list = list(mapped_times2)
mapped_div2_list = list(mapped_div2)
mapped_exp2_list = list(mapped_exp2)

print(mapped_times2_list)
print(mapped_div2_list)
print(mapped_exp2_list)

