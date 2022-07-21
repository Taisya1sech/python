# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

# вариант 1
n = int(input("Введите число: "))
while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
print("Число с цифрами в обратном порядке:", rev)

# вариант 2
n = input() #число сразу запоминается в строковом формате
rev = n[::-1] #строка инвертируется
print("Число с цифрами в обратном порядке:",rev)


# вариант 3
print("Число с цифрами в обратном порядке:", input()[::-1])