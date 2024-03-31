# Основаная функция выполняет вычислаения (умножение, деление, вычитание, сложение)  
# и возвращает результаты вычислений в виде целого числа.
import re
def main(numbs):
    string = ""
    for i in numbs:
        string += str(i)
        string += " "
    dost = re.findall(r"\d+", string)
    if len(string.replace(" ", "")) > 1 and len(string.replace(" ", "")) < 5 and int(dost[0]) < 11 and int(dost[1]) < 11:
        try:
            result = int(eval(string))  # Функция eval вычисляет выражение в строке.
            output = f"{string} = {result}"  # Формируем строку с примером и ответом
            return output # Возвращаем результат
        except:  # Обработка ошибок
            return 'throws Exception'  # Сообщение об ошибке
    else:
        return 'throws Exception'  # Сообщение об ошибке




if __name__ == '__main__':
    numbs = [x for x in input().split(" ")]
    result = main(numbs)
    print(result)
