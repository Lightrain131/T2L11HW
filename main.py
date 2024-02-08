# Import library
import matplotlib.pyplot as p
import numpy as n

# 0 <= x <= 10
x = n.linspace(0, 10, 400)

# Define the function
y = n.exp(-x) * n.cos(x)

# Adjust the size of window
p.figure(figsize=(10, 5))

# Draw
p.plot(x, y)
p.title("Plot of e^(-x) cos(x) from x=0 to x=10")
p.xlabel("x")
p.ylabel("f(x)")
p.grid()
p.axhline(color='black')
p.axvline(color='black')
p.show()

# QUIT
quit()
