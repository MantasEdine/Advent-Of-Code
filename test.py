
# вычитани = -
# сложение  = +
# умножение = *
# деление  = /
# возведение в степень = **
# остаток = %
# деление на целую часть = //
# приведение переменной = casting variable
# функция int() отрезает все после запятой 
# функция float() приводит к вещественному числу (Функция float() возвращает действительное число (десятичное число))





input_string = input("Enter numbers separated by spaces: ")


numbers = input_string.split()


negative_count = 0


for number in numbers:
   
    num = int(number)
   
    if num < 0:
        negative_count += 1


print("print neg count : ", negative_count)