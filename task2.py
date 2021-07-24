user_input = input('List: ')

input_list = user_input.split(' ')

for i in range(len(input_list) // 2):
    k1, k2 = 2 * 1, 2 * i + 1
    input_list[k1], input_list[k2] = input_list[k2], input_list[k1]

print(input_list)
