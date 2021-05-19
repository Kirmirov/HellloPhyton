

# Seventh task
print('Введите натуральное число, не превосходящее 1 000 000 000: ', end='')
numberStr = input()
lastNumberGroup = int(numberStr[-3:])
firstNum = lastNumberGroup // 100
secondNum = (lastNumberGroup // 10) % 10
thirdNum = lastNumberGroup % 10
numSum = firstNum + secondNum + thirdNum
print('Сумма последних трех цифр числа', numberStr, 'равна', numSum)