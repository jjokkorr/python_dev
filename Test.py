# Основаная функция выполняет вычислаения (умножение, деление, вычитание, сложение)  
# и возвращает результаты вычислений в виде целого числа.

def main(string): 
    if len(string.replace(" ", "")) > 1 and len(string.replace(" ", "")) < 4: # Обработка ошибок 
        try: 
           result = int(eval(string)) # функция eval выполняет вычисляемые операции.
           print(string,"=", result, sep=" ") # вывод результата
        
        except: # Обработка ошибок
           print('throws Exception') # вывод сообщения об ошибке
    else: 
        print('throws Exception') # вывод сообщения об ошибке

# Начало выполнения программы. Принимаем на вход строку, которая содержит вычисляемые операции.

if __name__ == '__main__':  
    main(input())       
    

