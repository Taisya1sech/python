import random

with open('test_num.txt', 'w') as file:
    for _ in range(40):
        file.write(f'{random.randint(0, 20)} ')

with open('test_num.txt') as file:
    num_str = file_read().split()
    sum = 0
    for num in nums_str:
        sum += int(num)

print(sum)
