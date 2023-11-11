import matplotlib.pyplot as plt
import numpy as np


def plot_graph(f_func, s_func, x_list):
    x = np.linspace(x_list[0], x_list[-1], 1000)
    y = eval(f_func)

    plt.subplot(1, 2, 1)
    plt.plot(x, y, 'b')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of f(x)')
    plt.grid(True)

    def S(x):
        for i in range(len(x_list) - 1):
            if x_list[i] <= x <= x_list[i + 1]:
                return eval(s_func[i].replace("x", "(" + str(x) + ")"))

    y = np.array([S(xi) for xi in x])
    plt.subplot(1, 2, 2)
    plt.plot(x, y, 'b')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of S(x)')
    plt.grid(True)

    plt.show()

    def e(x):
        for i in range(len(x_list) - 1):
            if x_list[i] <= x <= x_list[i + 1]:
                return (eval(f_func.replace("x", "(" + str(x) + ")"))) - (eval(s_func[i].replace("x", "(" + str(x) + ")")))

    y = np.array([e(xi) for xi in x])
    plt.plot(x, y, 'r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of e(x)')
    plt.grid(True)

    plt.show()
