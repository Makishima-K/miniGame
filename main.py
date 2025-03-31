import tkinter as tk
#import math
import random


def extract_data_from_file(filename):
    

    results = []
    current_question = {}

    with open(filename, 'r',encoding='utf-8') as file:
        for line in file:
            line = line.strip()

            if line.startswith("Name:"):
                if current_question:
                    results.append(current_question)
                    current_question = {}
                current_question['Name'] = line.split(":")[1].strip()

            elif line.startswith("Questions:"):
                if current_question and 'question' in current_question: # Проверка, если уже есть вопрос в current_question
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

# Пример использования:
#filename = "lol.txt"  # Замените на имя вашего файла





question1={}
#question1 = extract_data_from_file(filename)

#print(question1)




color_digits = "#F5F5DC"  # Бежевый для цифр и точки
color_functions = "#4682B4"  # Томатный красный для функциональных кнопок
color_equals = "#FFD700"  # Оранжевый для кнопки "="
background_color = "#a1c4b6"  # Светло-бежевый фон калькулятора #32CD32
button_relief = "raised"  # Тип рельефа кнопок
text_color = "black" 
Money_color = '#32CD32'
btn_good_color = '#7deb34'
btn_bad_color = '#eb4034'
bank_color = '#79db67'


size = 3
border_size = 3  # Размер рамок

font_size = ('Arial', 15)  # Размер шрифта кнопок




window = tk.Tk()

window.geometry('1600x900')
window.resizable(False,False)

window.config(bg=background_color)


window.title('Minigame')
photo = tk.PhotoImage(file='png.png')
photo2 = tk.PhotoImage(file='png2.png')
window.iconphoto(False,photo)
width1 = 400
top = 100
positionY = 100


AposX = width1*1
AposY = positionY*6

BposX = width1*1
BposY = positionY*7

CposX = width1*2
CposY = positionY*6

DposX = width1*2
DposY = positionY*7

MayPosXY = [(AposX,AposY),(BposX,BposY),(CposX,CposY),(DposX,DposY)]

window.config(bg=background_color)

bank = 0
k = 0
hidenBank =0

def goodAnswer(money):
    global k
    global hidenBank
    global bank

    money = int(money)
    sosoN()
    bank +=money
    hidenBank += money
    label_bank.config(text=f'Bank: {bank}$')
    k+=1
    if k== len(question1):
        print(bank)
        End(bank,hidenBank)
        print('All')
        return
    gameSet(question1[k])
    print('Yes')

def badAnswer(money):
    global k
    global hidenBank
    global bank
    sosoN()
    money = int(money)
    hidenBank += money
    k+=1
    if k== len(question1):
        End(bank,hidenBank)
        print('All')
        return
    gameSet(question1[k])
    print('No')

def End(bank,hidenBank):
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
    print(bank/hidenBank)
    if bank/hidenBank > 0.5:
        label_end.config(text=f'{bank}/{hidenBank}',bg=color_victory)
        label_end.place(x=width1*1,y=positionY*4, width=width1*2, height=top)
    elif bank/hidenBank < 0.5:
        label_end.config(text=f'{bank}/{hidenBank}',bg=lose_color)
        label_end.place(x=width1*1,y=positionY*4, width=width1*2, height=top)
    else:
        label_end.config(text=f'{bank}/{hidenBank}',bg=draw_color)
        label_end.place(x=width1*1,y=positionY*4, width=width1*2, height=top)


    

def  start(a):
    global question1
    global k
    global hidenBank
    global bank
    bank = 0
    hidenBank = 0
    k = 0

    label_bank.config(text=f'Bank: {bank}$')
    label_bank.place(x=width1*1,y=positionY*4, width=width1, height=top)
    label_money.place(x=width1*2,y=positionY*4, width=width1*1, height=top)
    label_1.place(x=width1*1,y=positionY*5, width=width1*2, height=top)
    btn_1.place(x=width1*1,y=positionY*6, width=width1, height=top)
    btn_2.place(x=width1*1,y=positionY*7, width=width1, height=top)
    btn_3.place(x=width1*2,y=positionY*6, width=width1, height=top)
    btn_4.place(x=width1*2,y=positionY*7, width=width1, height=top)
    btn_50_50.place(x=width1*1,y=positionY*8, width=width1, height=top/2)
    btn_end.place(x=width1*2,y=positionY*8, width=width1, height=top/2)
    question1 = extract_data_from_file(a)
    name = question1[k]['Name']
    window.title(f'Minigame: {name}')
    gameSet(question1[k])

def end(bank,file):
    o =0
    for i in range(len(file)):
        o += int(file[i]['money'])

    End(bank,o)
    pass



def sosoD():
    btn_3.config(state='disabled')
    btn_2.config(state='disabled')
    
def sosoN():
    btn_3.config(state='normal')
    btn_2.config(state='normal')


def show():
    label_start.place(x=width1*1,y=positionY*5, width=width1*2, height=top)
    ent_start.place(x=width1*1,y=positionY*6, width=width1, height=top/2)
    btn_start.place(x=width1*2,y=positionY*6, width=width1, height=top/2)
    

label_start = tk.Label(window, font=font_size, text=f'Write file name your game', bg=bank_color, fg=text_color)

ent_start = tk.Entry(window,  font=font_size, fg=text_color)

btn_start = tk.Button(window, command=lambda: start(ent_start.get()), text='Start', bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color,activebackground=btn_bad_color)


label_end = tk.Label(window, font=font_size, text=f' ', bg=bank_color, fg=text_color)


label_bank = tk.Label(window, font=font_size, text=f'Bank: {bank}$', bg=bank_color, fg=text_color)



label_1 = tk.Label(window, font=font_size, text='What', bg=color_equals, fg=text_color)


btn_1 = tk.Button(window, command=badAnswer, text='A', bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color,activebackground=btn_bad_color)
#


btn_2 = tk.Button(window, command=badAnswer, text='B', bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color,activebackground=btn_bad_color)
#

btn_3 = tk.Button(window, command=badAnswer, text='C', bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color,activebackground=btn_bad_color)
#


btn_4 = tk.Button(window, command=lambda: goodAnswer('0'), text='D', bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color,activebackground=btn_good_color)
#
btn_50_50 = tk.Button(window, command=sosoD, text='50/50', bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color,activebackground=btn_good_color)

btn_end = tk.Button(window, command=lambda: end(bank,question1), text='End', bg=color_functions, relief=button_relief, bd=border_size, font=font_size, fg=text_color,activebackground=btn_good_color)



label_money = tk.Label(window, font=font_size, text='Prize $', bg=Money_color, fg=text_color)



def random_list():
    numbers = [0, 1, 2, 3]
    random.shuffle(numbers)
    return numbers




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


    # Apply theme to Entry widget
    label_1.config(text=question)
    label_money.config(text=f'Prize: ${s}')

    a = random_list()
    
    
    btn_1.config(text=f'{a[0]+1}. {answerERR1}',command=lambda: badAnswer(s))
    btn_1.place(x=MayPosXY[a[0]][0],y=MayPosXY[a[0]][1], width=width1, height=top)
    
    btn_2.config(text=f'{a[1]+1}. {answerERR2}',command=lambda: badAnswer(s))
    btn_2.place(x=MayPosXY[a[1]][0],y=MayPosXY[a[1]][1], width=width1, height=top)
    
    btn_3.config(text=f'{a[2]+1}. {answerERR3}',command=lambda: badAnswer(s))
    btn_3.place(x=MayPosXY[a[2]][0],y=MayPosXY[a[2]][1], width=width1, height=top)
    
    btn_4.config(text=f'{a[3]+1}. {answerCor}', command=lambda: goodAnswer(s))
    btn_4.place(x=MayPosXY[a[3]][0],y=MayPosXY[a[3]][1], width=width1, height=top)
    
#        b = random.randint(1,4)


show()
#bind

hover_color = '#15ed97'

def on_enter(event):
    event.widget.config(bg=hover_color)

def on_leave(event):
    event.widget.config(bg=color_functions)

label_img = tk.Label(window,image=photo2)

def photoPlace1(event):
    x = event.x
    y = event.y
    if x < width1:
        x = width1
    elif x > width1*3:
        x = width1*3
    else:
        x = event.x
    
    if y > positionY*4:
        y = positionY*4
    elif y < positionY:
        y = positionY
    else:
        y = event.y
    
    
    label_img.place(x=x,y=y)



btn_1.bind("<Enter>", on_enter)
btn_1.bind("<Leave>", on_leave)

btn_2.bind("<Enter>", on_enter)
btn_2.bind("<Leave>", on_leave)

btn_3.bind("<Enter>", on_enter)
btn_3.bind("<Leave>", on_leave)

btn_4.bind("<Enter>", on_enter)
btn_4.bind("<Leave>", on_leave)

btn_50_50.bind("<Enter>", on_enter)
btn_50_50.bind("<Leave>", on_leave)

btn_end.bind("<Enter>", on_enter)
btn_end.bind("<Leave>", on_leave)

btn_start.bind("<Enter>", on_enter)
btn_start.bind("<Leave>", on_leave)
#window.bind('<Motion>',photoPlace1)



window.mainloop()