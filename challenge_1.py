import math


def set_triangle_type():
    a = int(input("Digite o primeiro lado do triângulo: \n"))
    b = int(input("Digite o segundo lado do triângulo: \n"))
    c = int(input("Digite o terceiro lado do triângulo: \n"))

    condition_one = math.fabs(b - c) and a < b + c
    condition_two = math.fabs(a - c) and b < a + c
    condition_three = math.fabs(a - b) and c < a + b

    if (
        condition_one is False
        or condition_two is False
        or condition_three is False
    ):
        return "Triângulo inválido"
    elif a == b and b == c:
        return "Triângulo equilátero"
    elif a != b and b != c:
        return "Triângulo escaleno"
    else:
        return "Triângulo isósceles"


print(set_triangle_type())
