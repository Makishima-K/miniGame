import tkinter as tk
import random

# Цвета и размеры
color_digits = "#F5F5DC"
color_functions = "#4682B4"
color_equals = "#FFD700"
background_color = "#a1c4b6"
button_relief = "raised"
text_color = "black"
Money_color = '#32CD32'
btn_good_color = '#7deb34'
btn_bad_color = '#eb4034'
bank_color = '#79db67'
btn_50_50_color = '#7cbfaa'
btn_end_color = '#bd3939'


size = 3
border_size = 3
font_size = ('Arial', 15)

# Размеры и позиции элементов
width1 = 400
top = 100
positionY = 100

AposX = width1 * 1
AposY = positionY * 6
BposX = width1 * 1
BposY = positionY * 7
CposX = width1 * 2
CposY = positionY * 6
DposX = width1 * 2
DposY = positionY * 7

MayPosXY = [(AposX, AposY), (BposX, BposY), (CposX, CposY), (DposX, DposY)]


btn5050= True


# Глобальные переменные
bank = 0
k = 0
hidenBank = 0
question1 = {}

# Функция для извлечения данных из файла
def extract_data_from_file(filename):
    results = []
    current_question = {}
    filename=filename+'.txt'
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()

            if line.startswith("Name:"):
                if current_question:
                    results.append(current_question)
                    current_question = {}
                current_question['Name'] = line.split(":")[1].strip()

            elif line.startswith("Questions:"):
                if current_question and 'question' in current_question:
                    results.append(current_question)
                    current_question = {}
                current_question['question'] = line.split(":")[1].strip()

            elif line.startswith("Answer Err1:"):
                current_question['answerERR1'] = line.split(":")[1].strip()

            elif line.startswith("Answer Err2:"):
                current_question['answerERR2'] = line.split(":")[1].strip()

            elif line.startswith("Answer Err3:"):
                current_question['answerERR3'] = line.split(":")[1].strip()

            elif line.startswith("Answer Correct:"):
                current_question['answerCor'] = line.split(":")[1].strip()

            elif line.startswith("Cost:"):
                current_question['money'] = line.split(":")[1].strip()

        if current_question:
            results.append(current_question)

    return results

# Функции для обработки ответов
def goodAnswer(money):
    global k, hidenBank, bank

    money = int(money)
    sosoN()
    bank += money
    hidenBank += money
    label_bank.config(text=f'Bank: {bank}$')
    k += 1
    if k == len(question1):
        End(bank, hidenBank,ee=True)
        return
    gameSet(question1[k])

def badAnswer(money):
    global k, hidenBank, bank
    
    
    sosoN()
    money = int(money)
    hidenBank += money
    k += 1
    if k == len(question1):
        End(bank, hidenBank)
        return
    End(bank, hidenBank,ee=False)
    return
    gameSet(question1[k])

# Функция для завершения игры
def End(bank, hidenBank,ee=False):
    color_victory = '#15ed93'
    lose_color = '#ed3615'
    draw_color = '#edc915'

    label_money.place_forget()
    label_1.place_forget()
    label_bank.place_forget()
    btn_1.place_forget()
    btn_2.place_forget()
    btn_3.place_forget()
    btn_4.place_forget()
    btn_50_50.place_forget()
    btn_end.place_forget()
    btn_Testgame.place_forget()
    btn_latTest.place_forget()
    btn_tri.place_forget()
    show()



    if ee:
        label_end.config(text=f'You win {bank}$', bg=color_victory)
        label_end.place(x=width1 * 1, y=positionY * 4, width=width1 * 2, height=top)
    else:
        label_end.config(text=f'You lost', bg=lose_color)
        label_end.place(x=width1 * 1, y=positionY * 4, width=width1 * 2, height=top)
   
# Функция для начала игры
def start(a):
    global question1, k, hidenBank, bank

    bank = 0
    hidenBank = 0
    k = 0

    label_bank.config(text=f'Bank: {bank}$')
    label_bank.place(x=width1 * 1, y=positionY * 4, width=width1, height=top)
    label_money.place(x=width1 * 2, y=positionY * 4, width=width1 * 1, height=top)
    label_1.place(x=width1 * 1, y=positionY * 5, width=width1 * 2, height=top)
    btn_1.place(x=width1 * 1, y=positionY * 6, width=width1, height=top)
    btn_2.place(x=width1 * 1, y=positionY * 7, width=width1, height=top)
    btn_3.place(x=width1 * 2, y=positionY * 6, width=width1, height=top)
    btn_4.place(x=width1 * 2, y=positionY * 7, width=width1, height=top)
    btn_50_50.config(state='normal')
    btn_50_50.place(x=width1 * 1+width1/4, y=positionY * 8+20, width=width1/2, height=top / 2)
    btn_end.place(x=width1 * 2+width1/4, y=positionY * 8+20, width=width1/2, height=top / 2)
    question1 = extract_data_from_file(a)
    name = question1[k]['Name']
    window.title(f'Minigame: {name}')
    btn_Testgame.place_forget()
    #btn_Testgame.place_forget()
    btn_latTest.place_forget()
    btn_tri.place_forget()
    gameSet(question1[k])

# Функция для завершения игры по кнопке
def end(bank, file):
    o = 0
    for i in range(len(file)):
        o += int(file[i]['money'])
    End(bank, o)

# Функции для подсказки 50/50
def sosoD():
    btn_50_50.config(state='disabled')
    btn_3.config(state='disabled')
    btn_2.config(state='disabled')

def sosoN():
    
    btn_3.config(state='normal')
    btn_2.config(state='normal')

# Функция для отображения элементов начала игры
def show():
    global AAA
    AAA = True
    label_start.place(x=width1 * 1, y=positionY * 6.5, width=width1 * 2, height=top/2)
    ent_start.place(x=width1 * 1, y=positionY * 7, width=width1, height=top / 2)
    btn_start.place(x=width1 * 2, y=positionY * 7, width=width1, height=top / 2)
    btn_tri.place(x=width1, y=positionY * 6.5, width=width1/6, height=top / 4)

# Создание элементов интерфейса
window = tk.Tk()
window.geometry('1600x900')
window.resizable(False, False)
window.config(bg=background_color)
window.title('Minigame')

photo = tk.PhotoImage(file='png.png')
PhotoBack = tk.PhotoImage(file='Back22.png')
window.iconphoto(False, photo)

label_Back = tk.Label(window, image=PhotoBack)
label_Back.place(x=-2, y=0)

label_start = tk.Label(window, font=font_size, text=f'Write file name your game', bg=bank_color, fg=text_color)
ent_start = tk.Entry(window, font=font_size, fg=text_color)
btn_start = tk.Button(window, command=lambda: start(ent_start.get()), text='Start', bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color, activebackground=btn_bad_color)
label_end = tk.Label(window, font=font_size, text=f' ', bg=bank_color, fg=text_color)
label_bank = tk.Label(window, font=font_size, text=f'Bank: {bank}$', bg=bank_color, fg=text_color)
label_1 = tk.Label(window, font=font_size, text='What', bg=color_equals, fg=text_color)
btn_1 = tk.Button(window, command=badAnswer, text='A', bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color, activebackground=btn_bad_color)
btn_2 = tk.Button(window, command=badAnswer, text='B', bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color, activebackground=btn_bad_color)
btn_3 = tk.Button(window, command=badAnswer, text='C', bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color, activebackground=btn_bad_color)
btn_4 = tk.Button(window, command=lambda: goodAnswer('0'), text='D', bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color, activebackground=btn_good_color)
btn_50_50 = tk.Button(window, command=sosoD, text='50/50', bg=btn_50_50_color, relief=button_relief, bd=border_size, font=font_size, fg=text_color, activebackground=btn_good_color)
btn_end = tk.Button(window, command=lambda: end(bank, question1), text='End', bg=btn_end_color, relief=button_relief, bd=border_size, font=font_size, fg=text_color, activebackground=btn_good_color)
label_money = tk.Label(window, font=font_size, text='Prize $', bg=Money_color, fg=text_color)

# Функция для генерации случайного порядка ответов
def random_list():
    numbers = [0, 1, 2, 3]
    random.shuffle(numbers)
    return numbers

# Функция для установки вопроса и ответов
def gameSet(question1):
    btn_1.place_forget()
    btn_2.place_forget()
    btn_3.place_forget()
    btn_4.place_forget()
    question = question1['question']
    answerERR1 = question1["answerERR1"]
    answerERR2 = question1["answerERR2"]
    answerERR3 = question1["answerERR3"]
    answerCor = question1["answerCor"]
    s = question1['money']

    label_1.config(text=question)
    label_money.config(text=f'Prize: ${s}')

    a = random_list()

    btn_1.config(text=f'{a[0] + 1}. {answerERR1}', command=lambda: badAnswer(s))
    btn_1.place(x=MayPosXY[a[0]][0], y=MayPosXY[a[0]][1], width=width1, height=top)

    btn_2.config(text=f'{a[1] + 1}. {answerERR2}', command=lambda: badAnswer(s))
    btn_2.place(x=MayPosXY[a[1]][0], y=MayPosXY[a[1]][1], width=width1, height=top)

    btn_3.config(text=f'{a[2] + 1}. {answerERR3}', command=lambda: badAnswer(s))
    btn_3.place(x=MayPosXY[a[2]][0], y=MayPosXY[a[2]][1], width=width1, height=top)

    btn_4.config(text=f'{a[3] + 1}. {answerCor}', command=lambda: goodAnswer(s))
    btn_4.place(x=MayPosXY[a[3]][0], y=MayPosXY[a[3]][1], width=width1, height=top)

# Отображение элементов начала игры
AAA = True

def frame():
    global AAA
    if AAA:
        btn_Testgame.place(x=width1 * 1, y=positionY * 6, width=width1, height=top / 2)
        btn_latTest.place(x=width1 * 2, y=positionY * 6, width=width1, height=top / 2)

        AAA =False
        
    else:
        btn_Testgame.place_forget()
        btn_latTest.place_forget()
        AAA = True
        

    

btn_Testgame = tk.Button(window, command=lambda: start('test'), text='Test', bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color, activebackground=btn_bad_color)

btn_latTest = tk.Button(window, command=lambda: start('Matemātikas viktorīna'), text='Matemātikas viktorīna', bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color, activebackground=btn_bad_color)

btn_tri = tk.Button(window, command=lambda: frame(), text='△', bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color, activebackground=btn_bad_color)











# Обработка событий наведения мыши
hover_color = '#15ed97'

def on_enter(event):
    event.widget.config(bg=hover_color)

def on_leave(event):
    event.widget.config(bg=color_functions)

btn_1.bind("<Enter>", on_enter)
btn_1.bind("<Leave>", on_leave)
btn_2.bind("<Enter>", on_enter)
btn_2.bind("<Leave>", on_leave)
btn_3.bind("<Enter>", on_enter)
btn_3.bind("<Leave>", on_leave)
btn_4.bind("<Enter>", on_enter)
btn_4.bind("<Leave>", on_leave)

btn_start.bind("<Enter>", on_enter)
btn_start.bind("<Leave>", on_leave)

btn_latTest.bind("<Enter>", on_enter)
btn_Testgame.bind("<Enter>", on_enter)

btn_latTest.bind("<Leave>", on_leave)
btn_Testgame.bind("<Leave>", on_leave)

btn_tri.bind("<Enter>", on_enter)
btn_tri.bind("<Leave>", on_leave)



def on_enter1(event):
    event.widget.config(bg=hover_color)

def on_leave1(event):
    event.widget.config(bg=btn_50_50_color)

def on_enter2(event):
    event.widget.config(bg=hover_color)

def on_leave2(event):
    event.widget.config(bg=btn_end_color)


btn_50_50.bind("<Enter>", on_enter1)
btn_50_50.bind("<Leave>", on_leave1)
btn_end.bind("<Enter>", on_enter2)
btn_end.bind("<Leave>", on_leave2)
show()
window.mainloop()