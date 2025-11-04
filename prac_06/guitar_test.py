"""Test Guitar Class"""

from guitar import Guitar

# Build Guitars
g1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
g2 = Guitar("Another Guitar", 2005, 15000.99)

# Test get_age() function
print(g1, f"get_age() - Expected 103. Got {g1.get_age()}")
print(g2, f"get_age() - Expected 20. Got {g2.get_age()}")

# Test is_vintage() function
print(g1, f"is_vintage() - Expected True. Got {g1.is_vintage()}")
print(g2, f"is_vintage() - Expected False. Got {g2.is_vintage()}")
