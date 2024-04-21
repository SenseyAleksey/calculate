def calculate(expression):
  """
  Функция принимает на вход строку с арифметическим выражением 
  и возвращает результат вычисления.

  Args:
      expression: Строка с арифметическим выражением.

  Returns:
      Результат вычисления.
  """

  try:
    # Разделяем выражение на числа и оператор
    parts = expression.split()
    if len(parts) != 3:
      raise ValueError("Неверный формат выражения.")
    a, operator, b = parts

    # Проверяем, что числа целые и в заданном диапазоне
    a = int(a)
    b = int(b)
    if not (1 <= a <= 10 and 1 <= b <= 10):
      raise ValueError("Числа должны быть в диапазоне от 1 до 10.")

    # Выполняем операцию
    if operator == "+":
      result = a + b
    elif operator == "-":
      result = a - b
    elif operator == "*":
      result = a * b
    elif operator == "/":
      # Деление с преобразованием делителя в десятичное число
      result = a / float(b)
    else:
      raise ValueError("Неизвестный оператор.")

    return result

  except ValueError as e:
    print(f"Ошибка: {e}")
    return None

while True:
  # Запрашиваем выражение у пользователя
  expression = input("Введите выражение (два числа и оператор, разделенные пробелами): ")

  # Вычисляем результат
  result = calculate(expression)

  # Выводим результат или сообщение об ошибке
  if result is not None:
    print(f"Результат: {result}")
  else:
    print("Некорректное выражение.")
