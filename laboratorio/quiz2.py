'''
realizar la suma de todos los números pares entre 10 y 5000 sin contemplar a 100 y 1000
'''

x = 8
y = 0
while x < 5001:
    if x == 100 or x == 1000:
        pass
    y = y + x
    x += 2

print(y)
