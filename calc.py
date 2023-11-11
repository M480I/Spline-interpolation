import numpy as np
import sympy


def divided_difference(left, right, f, x_list):
    if right == left:
        return f(x_list[left])
    return (divided_difference(left + 1, right, f, x_list) - divided_difference(left, right - 1, f, x_list)) / (
            x_list[right] - x_list[left])


def h(i, x_list):
    return x_list[i] - x_list[i - 1]


def mu(i, x_list):
    return h(i, x_list) / (h(i, x_list) + h(i + 1, x_list))


def lamda(i, x_list):
    return h(i + 1, x_list) / (h(i, x_list) + h(i + 1, x_list))


def p(i, m, f, x_list):
    return divided_difference(i, i + 1, f, x_list) + (h(i + 1, x_list) / 6) * (m[i] - m[i + 1])


def q(i, m, f, x_list):
    return f(x_list[i]) - ((h(i + 1, x_list) ** 2) / 6) * m[i]


def calc(f, x_list):
    n = len(x_list) - 1

    #   solving system of m_0 to m_n
    A_arr = []
    b_arr = []
    for i in range(1, n):
        arr = [0] * (n + 1)

        arr[i - 1] = mu(i, x_list)
        arr[i] = 2
        arr[i + 1] = lamda(i, x_list)

        A_arr.append(arr)
        b_arr.append(6 * divided_difference(i - 1, i + 1, f, x_list))

    arr = [1]
    arr.extend([0] * n)
    A_arr.append(arr)
    b_arr.append(0)

    arr = []
    arr.extend([0] * n)
    arr.append(1)
    A_arr.append(arr)
    b_arr.append(0)

    A = np.array(A_arr)
    b = np.array(b_arr)

    m = np.linalg.solve(A, b)  # m array is calculated and it's system is solved

    ans = []

    for i in range(n):
        string = f"(((x - {x_list[i]}) ** 3) / (6 * {h(i + 1, x_list)})) * {m[i + 1]}"
        string += " + "
        string += f"((({x_list[i + 1]} - x) ** 3) / (6 * {h(i + 1, x_list)})) * {m[i]}"
        string += " + "
        string += f"{p(i, m, f, x_list)} * (x - {x_list[i]}) + {q(i, m, f, x_list)}"

        x = sympy.symbols("x")
        expr = sympy.sympify(eval(string))  # simplifying the function

        ans.append(str(expr))

    return ans
