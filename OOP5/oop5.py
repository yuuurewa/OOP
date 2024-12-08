my_list = [10, 20, 30, 40, 50]

while True:
    try:
        index = int(input("Введите индекс элемента (или отрицательное число для выхода): "))
        if index < 0:
            break

        if not 0 <= index < len(my_list):
            raise IndexError("Индекс за пределами списка!")

        value = my_list[index]
        print(f"Значение элемента с индексом {index}: {value}")
        
    except ValueError:
        print("Ошибка: Введите целое число.")
    except IndexError as e:
        print("Ошибка:", e)
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

print("Программа завершена.\n")
