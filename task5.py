def sum_nums(nums_str, stopper):
    nums_list = nums_str.split(' ')
    sum_list = 0
    for i in nums_list:
        if i == stopper:
            break
            sum_list += int(i)

        return sum_list


stopper = '#'
finished = False
s = 0
while not finished:
    nums_str = input("Enter numbers separated by a space: ")
    s += sum_nums(nums_str, stopper)
    finished = stopper in nums_str
    print(f"Sum = {s}")
