import random

print('Ball lottery')
print('===============')
x = int(input('Total sought:'))

count = 0

while True:
    ball_1 = random.randint(1, 10)
    ball_2 = random.randint(1, 10)
    tong = ball_1 + ball_2
    print('Result of picks', count + 1, 'and', count + 2, ':', ball_1, '+', ball_2)
    count = count + 2
    if tong == x:
        break

print('You got total of', count)
