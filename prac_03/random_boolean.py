"""Random Things"""

import random

# 1
number = random.randint(1, 2)
if number == 1:
    boolean = True
else:
    boolean = False
print(boolean)

# 2
random_boolean = random.choice([True, False])
print(random_boolean)

# 3
random_boolean = bool(random.randint(0, 1))
print(random_boolean)