# импорт модулей
import tkinter as tk
from tkinter import font
# Создание главного окна с его параметрами
win = tk.Tk()
win.geometry('400x550')
win['bg'] = '#242630'
win.resizable(height=False, width=False)
win.title('Calculate 0.1')

# Функция контролирующая ввод символов: 1234567890()


def inpt(num):
    value = entr.get()  # Получение содержимого entry
    open = 0  # Количество '(' в entry
    closed = 0  # Количество ')' в entry
    for i in value:  # Подсчет open и closed путем перебора знаков в строке value
        if i == '(':
            open += 1
        if i == ')':
            closed += 1

    if open == closed and num == ')':  # Нельзя ставить ')' больше, чем '('
        pass
    # Не допускается ввод данных типа:  (-)
    elif value[-1] in '-+/*' and num == ')':
        pass
    # Нельзя ставить цифры перед '(' без знака операции
    elif value[-1] in '1234567890' and num == '(' and value[0] != '0':
        pass
    else:
        if value == '0':  # Если в поле ввода только 0
            sp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            if num in sp or num == '(':  # Если вводимый знак это цифра или '('
                entr.delete(0, tk.END)  # То очищаем поле ввода
        # Если последний знак '(' то вводимым знаком не может быть ')'
        if value[-1] == '(' and num == ')':
            pass
        elif value[-1] in ')' and num in '()' and open == closed:  # Не допустимы значения: )(
            pass
        else:
            value = entr.get()  # Получаем строку из поля ввода
            entr.delete(0, tk.END)  # Очищаем поле ввода
            # Создаем строку из старой строки и вводимого знака
            value = str(value) + str(num)
            entr.insert(0, value)  # Добавлям новую строку в поле

# Функция добавления и выполнения операций


def inpt_oprc(operation):
    value = entr.get()  # Получаем строку из поля ввода
    open = 0  # количество '('
    closed = 0  # количество ')'
    if value == '0':  # Если строка ровна 0
        if operation in '-':  # Если знак операции равен '-'
            entr.delete(0, tk.END)  # Очистка поля ввода
            value = str(operation)  # Преобразовываем знак в строку
            # добавляем единственный знак стоящий в начале строки
            entr.insert(0, value)
        else:
            pass
    if value[0:] in '+-' and operation in '*/':
        pass
    # Если последний знак '(', то нельзя ставить знаки +/*
    elif value[-1] == '(' and operation in '/+*':
        pass
    # Если в конце строки стоит знак операции или точка то при добавлении нового знака старый удаляется
    elif value[-1] in '+-/*':
        if value[-2:] == '(-':#Нельзя заменять знак - на другие операции если это противоречит прередущему elif
            pass
        else:
            value = value[0:len(value)-1]+(operation)

            entr.delete(0, tk.END)
            entr.insert(0, value)
    else:
        for i in value:  # Подсчет open и closed путем перебора знаков в строке value
            if i in '(':
                open += 1
            if i in ')':
                closed += 1
        if open == closed:  # Если в строке одинаковое значение '(' и ')'
            # Исключаем ошибку при делении на 0
            try:
                value = eval(value)  # То считаем строку
            except:
                entr.delete(0, tk.END)  # При делении на 0 удаляем строку
                entr.insert(0, 0)  # И заменяем её на 0
        entr.delete(0, tk.END)  # Очистка поля
        value = str(value) + str(operation)  # Создание новой строки
        entr.insert(0, value)  # Добавление новой строки

# Функция заменяющая строку на 0 при нажатии на C


def inpt_del():
    entr.delete(0, tk.END)
    entr.insert(0, 0)

# Функция кнопки =


def rovn():
    value = entr.get()  # Получение строки из поля ввода
    if value[-1] in '+-/*':  # Если последний знак операция функция не выполняется
        pass
    else:  # При делении на 0
        try:
            entr.delete(0, tk.END)
            value = eval(value)
            entr.insert(0, value)
        except:
            entr.delete(0, tk.END)
            entr.insert(0, 0)  # Заменяем строку на 0

# Возврвщение параметров кнопок 0123456789()


def btn_number(num):
    return tk.Button(text=num, bd=0, bg='#616652', fg='#ffffff', activebackground='#6166ff', font=('Harlow Solid Italic', 20), command=lambda: inpt(num))

# Возврвщение параметров кнопок операций


def btn_operacion(operation):
    return tk.Button(text=operation, bd=0, bg='#616652', fg='#ffffff', activebackground='#6166ff', font=('Harlow Solid Italic', 20), command=lambda: inpt_oprc(operation))

# Функция создания интерфейса


def interface():
    # Создание кнопок 1234567890
    btn_number(1).grid(row=1, column=0, sticky='wens', padx=2, pady=2)
    btn_number(2).grid(row=1, column=1, sticky='wens', padx=2, pady=2)
    btn_number(3).grid(row=1, column=2, sticky='wens', padx=2, pady=2)
    btn_number(4).grid(row=2, column=0, sticky='wens', padx=2, pady=2)
    btn_number(5).grid(row=2, column=1, sticky='wens', padx=2, pady=2)
    btn_number(6).grid(row=2, column=2, sticky='wens', padx=2, pady=2)
    btn_number(7).grid(row=3, column=0, sticky='wens', padx=2, pady=2)
    btn_number(8).grid(row=3, column=1, sticky='wens', padx=2, pady=2)
    btn_number(9).grid(row=3, column=2, sticky='wens', padx=2, pady=2)
    btn_number(0).grid(row=4, column=0, sticky='wens', padx=2, pady=2)
    # Создание кнопок +-*/
    btn_operacion('+').grid(row=1, column=3, sticky='wens', padx=2, pady=2)
    btn_operacion('-').grid(row=2, column=3, sticky='wens', padx=2, pady=2)
    btn_operacion('*').grid(row=3, column=3, sticky='wens', padx=2, pady=2)
    btn_operacion('/').grid(row=4, column=3, sticky='wens', padx=2, pady=2)
    # Создание кнопки очищения поля ввода
    tk.Button(text='C', bd=0, bg='#616652', fg='#ffffff', activebackground='#6166ff', font=(
        'Harlow Solid Italic', 20), command=lambda: inpt_del()).grid(row=5, column=0, columnspan=2, sticky='wens', padx=2, pady=2)
    # Создания кнопки =
    tk.Button(text='=', bd=0, bg='#616652', fg='#ffffff', activebackground='#6166ff', font=(
        'Harlow Solid Italic', 20), command=lambda: rovn()).grid(row=5, column=2, columnspan=2, sticky='wens', padx=2, pady=2)
    # Создания кнопок ( )
    btn_number('(').grid(row=4, column=1, sticky='wens', padx=2, pady=2)
    btn_number(')').grid(row=4, column=2, sticky='wens', padx=2, pady=2)
    # Создание кнопки √


# Создание поля ввода
entr = tk.Entry(bd=0, font=('Harlow Solid Italic', 20), justify='right')
entr.insert(0, 0)  # Изначаленое значение поля ввода 0
entr.grid(row=0, column=0, columnspan=4, sticky='wens',
          padx=2, pady=2)  # Упаковка поля
#Блокировка ввода данных с клавиатуры
entr.bind('<Key>', lambda e: 'break')
# Запуск создания интерфейса
interface()
# Регулировка размера строк
win.grid_rowconfigure(0, minsize=50)
win.grid_rowconfigure(1, minsize=100)
win.grid_rowconfigure(2, minsize=100)
win.grid_rowconfigure(3, minsize=100)
win.grid_rowconfigure(4, minsize=100)
win.grid_rowconfigure(5, minsize=100)
# Регулировка размера колон
win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)
win.grid_columnconfigure(2, minsize=100)
win.grid_columnconfigure(3, minsize=100)

win.mainloop()
