import sys

# Replace all ______ with rjust, ljust or center.

thickness = int(input())  # This must be an odd number

n = 5
c = 'H'

# Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

ht = int(thickness / 2)
# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).rjust(thickness * 2 - ht - 1) + (c * thickness).rjust(thickness * (n - 1)))

# Middle Belt
for i in range(int((thickness + 1) / 2)):
    print((c * (thickness * n)).rjust(thickness * n + ht))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).rjust(thickness * 2 - ht - 1) + (c * thickness).rjust(thickness * (n - 1)))

# Bottom Cone
for i in range(thickness):
    print(
        ((c * (thickness - i - 1)).rjust(thickness * n - 1) + c + (c * (thickness - i - 1)).ljust(thickness)).ljust(
            thickness * (n - 1)))
