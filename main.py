from plot import plot_graph
from calc import calc
import numpy as np

f_function = input("Enter the function:\n> ")
x_list = []
n = int(input("Enter n:\n> "))
for i in range(n + 1):
    x_list.append(int(input(f"Enter x_{i}:\n> ")))
x_list.sort()

s_function = calc(lambda x: eval(f_function), x_list)  # calculating the spline function

print("S(x) is:")
for i in range(n):
    print(f"\tfor {x_list[i]} ≤ x ≤ {x_list[i + 1]}:\n\t\t" + s_function[i] + "\n")

plot_graph(f_function, s_function, x_list)
