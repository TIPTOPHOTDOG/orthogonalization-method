def matrix(file_name='default.txt'):
    with open(file_name) as f:
        matrix_list = [
            [float(j) for j in (i[0] + i[1:].replace('=-', '+').replace('=', '-').replace('-', '+-')).split('+')] for i
            in f]
        matrix_list.append([0.0 if i != len(matrix_list) else 1.0 for i in range(len(matrix_list) + 1)])
        return matrix_list


def vector_len(vector: list):
    result = 0
    for i in range(len(vector)):
        result += vector[i] ** 2
    return result ** 0.5


def vector_multiplication(a: list, b: list):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result


def method(matrix: list = matrix()):
    print("Изначальная система уравнений:\n", end='')
    for i in matrix[:-1]:
        for j in range(len(i)-1):
            if i[j] != 0:
                print(f'{i[j] if i[j] < 0 else "+"+str(i[j]) if j != 0 else i[j]}x[{j+1}]', end='')
        print(f'= {-i[-1]}')
    k = len(matrix)
    u = [[0] * k for i in range(k)]
    u[0] = matrix[0]
    v = [[0] * k for i in range(k)]
    v[0] = [i / vector_len(u[0]) for i in u[0]]
    for i in range(1, k):
        for j in range(k):
            u[i][j] = matrix[i][j] - sum(vector_multiplication(matrix[i], v[n]) * v[n][j] for n in range(i))
        v[i] = [j / vector_len(u[i]) for j in u[i]]
    return [i / u[-1][-1] for i in u[-1][:-1]]


if __name__ == '__main__':
    result = method(matrix())
    print("Полученный результат: ")
    for i in range(len(result)):
        print(f"x[{i + 1}] = {result[i]}")
    print("Проверка:")
    for i in matrix()[:-1]:
        test = 0
        for j in range(len(result)):
            test += i[j] * result[j]
        test *= -1
        result_len = str(i[-1])
        while(result_len[1] != '.'):
            result_len = result_len[1:]
        result_len = len(result_len)
        print(f"{round(test, result_len)} = {round(i[-1], result_len)}")
