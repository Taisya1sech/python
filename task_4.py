# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

a = ord(input('Введите любую букву латинского алфавита: '))
b = ord(input('Введите любую ДРУГУЮ букву латинского алфавита: '))
a = a - ord('a') + 1
b = b - ord('a') + 1
print('Буквы в алфавите стоят под номерами: %d и %d' % (a, b))
print('Между буквами символов:', abs(a-b)-1)
