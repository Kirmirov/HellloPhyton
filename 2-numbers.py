

# Seventh task
print('������� ����������� �����, �� ������������� 1 000 000 000: ', end='')
numberStr = input()
lastNumberGroup = int(numberStr[-3:])
firstNum = lastNumberGroup // 100
secondNum = (lastNumberGroup // 10) % 10
thirdNum = lastNumberGroup % 10
numSum = firstNum + secondNum + thirdNum
print('����� ��������� ���� ���� �����', numberStr, '�����', numSum)