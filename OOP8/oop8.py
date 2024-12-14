import numpy as np
import random


# Интерфейс для наблюдателя
class Observer:
    def update(self, matrix):
        raise NotImplementedError


# Наблюдатель для вывода матрицы и её характеристик
class MatrixObserver(Observer):
    def update(self, matrix):
        print("Матрица:")
        print(matrix)
        print(f"Максимум: {np.max(matrix)}")
        print(f"Сумма: {np.sum(matrix)}")
        if matrix.shape[0] == matrix.shape[1]:  # Квадратная матрица
            print(f"След: {np.trace(matrix)}")
            print(f"Определитель: {np.linalg.det(matrix)}")
        else:
            print("Определитель: Не определён (матрица не квадратная)")


# Абстрактный класс для матриц
class Matrix:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, matrix):
        for observer in self.observers:
            observer.update(matrix)


# Конкретные классы матриц
class IdentityMatrix(Matrix):
    def create(self, size):
        mat = np.eye(size)
        self.notify(mat)


class DiagonalMatrix(Matrix):
    def create(self, size, value):
        mat = np.diag([value] * size)
        self.notify(mat)


class RandomDiagonalMatrix(Matrix):
    def create(self, size):
        values = [random.randint(1, 10) for _ in range(size)]
        mat = np.diag(values)
        self.notify(mat)


class SquareMatrix(Matrix):
    def create(self, size):
        mat = np.random.randint(1, 10, size=(size, size))
        self.notify(mat)


# Функция для выбора матрицы
def main():
    observer = MatrixObserver()

    print("Выберите тип матрицы:")
    print("1: Единичная")
    print("2: Диагональная с определённым числом")
    print("3: Диагональная с случайными числами")
    print("4: Квадратная")

    choice = int(input("Введите номер типа матрицы: "))
    size = int(input("Введите размер матрицы: "))

    if choice == 1:
        matrix = IdentityMatrix()
        matrix.attach(observer)
        matrix.create(size)
    elif choice == 2:
        value = int(input("Введите значение для диагональной матрицы: "))
        matrix = DiagonalMatrix()
        matrix.attach(observer)
        matrix.create(size, value)
    elif choice == 3:
        matrix = RandomDiagonalMatrix()
        matrix.attach(observer)
        matrix.create(size)
    elif choice == 4:
        matrix = SquareMatrix()
        matrix.attach(observer)
        matrix.create(size)
    else:
        print("Некорректный выбор")


if __name__ == "__main__":
    main()
