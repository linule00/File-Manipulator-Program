import sys
import random

"""
Guess the number game
"""

while True:
    sys.stdout.buffer.write(b'Please enter the minimum value: ')
    sys.stdout.flush()
    min_value = int(sys.stdin.buffer.readline().decode().strip())

    sys.stdout.buffer.write(b'Please enter the maximum value: ')
    sys.stdout.flush()
    max_value = int(sys.stdin.buffer.readline().decode().strip())

    if min_value <= max_value:
        break
    else:
        sys.stdout.buffer.write(b'Minimum value must be less than or equal to maximum value. Please try again.\n')
        sys.stdout.flush()

random_number = random.randint(min_value, max_value)
print(random_number)

for i in range(1, 6):
    sys.stdout.buffer.write(b'Guess the number (attempt ' + str(i).encode() + b'/5): ')
    sys.stdout.flush()

    input_number = int(sys.stdin.buffer.readline().decode().strip())

    if random_number == input_number:
        sys.stdout.buffer.write(b'Correct!! \n')
        sys.stdout.flush()
        break
    elif i == 5:
        sys.stdout.buffer.write(b'Game over! \n')
        sys.stdout.flush()
    else:
        sys.stdout.buffer.write(b'Incorrect. Try again! \n')
        sys.stdout.flush()