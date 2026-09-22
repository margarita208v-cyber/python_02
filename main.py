print('Hello, World!')

name = 'Магро'
age = 17
height = 170
is_student = True

print(name)
print(age)
print(height)
print(is_student)

first_name = ('Маргарита')
last_name = ('Гуляева')

age_raw = ('17')
print(age_raw, type(age_raw))

age = int(age_raw)
height = float('156')

print(first_name)
print(last_name)
print(age, type(age))
print(height, type(height))

a = 15
b = 4

x = a - b
x1 = a + b
x2 = a * b
x3 = a / b
x4 = a // b
x5 = a % b
x6 = a ** b

print(x, x1, x2, x3, x4, x5, x6)

m = 2 + 3 * 4
m1 = (2+3) * 4

print(m, m1)

for i in range(1,11):
    print(i)

for o in range(10,0,-1):
    print(o)

for t in range(0,21):
    print(t)

for u in range(0,21,5):
    print(u)

count = 10
print(count) 

while count >= 1:
    count -= 1
    print(count)
print('Цикл завершен')

import math

radius = 5

dlina = 2 * math.pi * radius
area = math.pi * radius ** 2

print(radius)
print(dlina)
print(area)

number = 16.0
sqrt_value = math.sqrt(number)
print(sqrt_value)

number = int(0)

# Определение знака
if number > 0:
    print("Число положительное")
elif number < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")

# Проверка чётности
if number % 2 == 0:
    print("Число чётное")
else:
    print("Число нечётное")

number = int(6)

# Определение знака
if number > 0:
    print("Число положительное")
elif number < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")

# Проверка чётности
if number % 2 == 0:
    print("Число чётное")
else:
    print("Число нечётное")

number = int(-8)

# Определение знака
if number > 0:
    print("Число положительное")
elif number < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")

# Проверка чётности
if number % 2 == 0:
    print("Число чётное")
else:
    print("Число нечётное")

age = 17
has_access = True

print(age)
print("Допуск имеется:", has_access)

if age >= 18 and has_access:
    print("Доступ разрешён")
else:
    print("Доступ запрещён")

age1 = 25
has_access1 = True

print(age1)
print("Допуск имеется:", has_access1)

if age1 >= 18 and has_access1:
    print("Доступ разрешён")
else:
    print("Доступ запрещён")

name = 'Магро'
age = 17
height = 170
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

name = 'Магро'
age = 67
height = 654
is_student = True

print(type(name), name)
print(type(age), age)
print(type(height), height)
print(type(is_student), is_student)

a = float(156)
b = float(4)
c = float(67589)
d = float(123)
print(type(a), type(b), type(c), type(d))

x = a - b
xr = c - d
x1 = a + b
xr1 = c + d
x2 = a * b
xr2 = c * d
x3 = a / b
xr3 = c / d

print(x, x1, x2, x3)
print(xr, xr1, xr2, xr3)

for u in range(0,21,5):
    print(u)

n = int(209)
x=0

for i in range(1,n):
    x += i
print(x)

n1 = int(86)
x1=0

for i1 in range(1,n1):
    x1 += i
print(x1)

n2 = int(1345)
x2=0

for i2 in range(1,n2):
    x2 += i
print(x2)

number = int(6)

n = int(8)

total = 0.0

for i in range(1, n + 1):
    value = float(67)
    total += value

sr_ar = total / n if n > 0 else 0.0

print(total)
print(sr_ar)