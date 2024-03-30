# Основаная функция выполняет вычислаения (умножение, деление, вычитание, сложение)  
# и возвращает результаты вычислений в виде целого числа.

def main(string):
    # Обработка ошибок и проверка строки
    if len(string.replace(" ", "")) > 1 and len(string.replace(" ", "")) < 5:
        try:
            result = int(eval(string))  # Функция eval вычисляет выражение в строке.
            output = f"{string} = {result}"  # Формируем строку с примером и ответом
            return output # Возвращаем результат
        except:  # Обработка ошибок
            return 'throws Exception'  # Сообщение об ошибке
    else:
        return 'throws Exception'  # Сообщение об ошибке

# Начало выполнения программы. Принимаем на вход строку, которая содержит вычисляемые операции.
if __name__ == '__main__':
    result = main(input())
    print(result)
