# Калькулятор в новой ветке
# Функция для сложения двух чисел
add = lambda x, y: x + y

# Функция для вычитания двух чисел
subtract = lambda x, y: x - y

# Функция для умножения двух чисел
multiply = lambda x, y: x * y

# Функция для деления двух чисел
divide = lambda x, y: x / y if y != 0 else "Ошибка: деление на ноль!"

# Теперь мы можем создать функцию для обработки ввода пользователя

def calculator():
    print("Добро пожаловать в калькулятор!")
    print("Введите 'exit' для выхода.")

    while True:
        # Запрашиваем у пользователя ввод
        user_input = input("Введите выражение (например, 5 + 3): ")

        if user_input.lower() == 'exit':
            print("Спасибо за использование калькулятора!")
            break

        try:
            # Разбиваем ввод на числа и оператор с помощью split
            num1, operator, num2 = user_input.split()
            num1 = float(num1)  # Преобразуем строку в число
            num2 = float(num2)  # Преобразуем строку в число

            # Выполняем операцию в зависимости от введенного оператора
            if operator == '+':
                result = add(num1, num2)
            elif operator == '-':
                result = subtract(num1, num2)
            elif operator == '*':
                result = multiply(num1, num2)
            elif operator == '/':
                result = divide(num1, num2)
            else:
                result = "Неизвестный оператор!"

            # Выводим результат
            print("Результат:", result)

        except ValueError:
            print("Ошибка: неверный ввод! Попробуйте еще раз.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

# Запускаем калькулятор
calculator()
