from tkinter import *


def get_digit(digit):
    current = result_lable['text']
    new = current + str(digit)
    result_label.config(text=new)


def clear():
    result_label.config(text='')


def get_operators(op):
    global first_number,operator
    operator = op
    result_label.config(text='')


def get_result():
    global first_number,second_number,operator
    second_number = int(result_label['text'])
    if operator == '+':
        result_label.config(text=str(first_number+second_number))
    elif operator == '-':
        result_label.config(text=str(first_number-second_number))
    elif operator == '*':
        result_label.config(text=str(first_number*sucend_number))
    else:
        if second_number == 0:
            result_label.config(text='error')
        else:
            result_label.config(text=str(first_number/second_number))


root = Tk()
root.title("smart calculater")
root.geometry('560x760')
root.resizeable(0,0)
root.configure(background='black')




result_label = Label(root,text='', bg='black',fg='white')
result_label.grid(row=0,column=0,columnspan=5,pady=(100,50),sticky='e')
result_label.config(font=('vardana',60,'bold'))

btn7 = Button(root,text='7',bg='#00a65a',fg='white',width=10,height=4,command= lambda:get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('vardana',28))

btn8 = Button(root,text='8',bg='#00a65a',fg='white',width=10,height=4,command= lambda:get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('vardana',28))


btn9 = Button(root,text='9',bg='#00a65a',fg='white',width=10,height=4,command= lambda:get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('vardana',28))


btn_add = Button(root,text='+',bg='#00a65a',fg='white',width=10,height=4,command= lambda: get_operators('+'))
btn_add.grid(row=1,column=3)
btn_add.config(font=('vardana',28))


btn4 = Button(root,text='4',bg='#00a65a',fg='white',width=10,height=4,command= lambda:get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('vardana',28))

btn5 = Button(root,text='5',bg='#00a65a',fg='white',width=10,height=4,command= lambda:get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('vardana',28))


btn6 = Button(root,text='6',bg='#00a65a',fg='white',width=10,height=4,command= lambda:get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('vardana',28))


btn_sub = Button(root,text='-',bg='#00a65a',fg='white',width=10,height=4,command= lambda: get_operator('-'))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('vardana',28))


btn1 = Button(root,text='1',bg='#00a65a',fg='white',width=10,height=4,command= lambda:get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('vardana',28))

btn2 = Button(root,text='2',bg='#00a65a',fg='white',width=10,height=4,command= lambda:get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('vardana',28))


btn3 = Button(root,text='3',bg='#00a65a',fg='white',width=10,height=4,command= lambda:get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('vardana',28))


btn_multi = Button(root,text='*',bg='#00a65a',fg='white',width=10,height=4,command= lambda:get_operator('*'))
btn_multi.grid(row=3,column=3)
btn_multi.config(font=('vardana',28))


btn_clr = Button(root,text='C',bg='#00a65a',fg='white',width=10,height=4,command= lambda:clear())
btn_clr.grid(row=4,column=0)
btn_clr.config(font=('vardana',28))

btn0 = Button(root,text='0',bg='#00a65a',fg='white',width=10,height=4,command= lambda:get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('vardana',28))


btn_div = Button(root,text='/',bg='#00a65a',fg='white',width=10,height=4,command= lambda:get_operator('/'))
btn_div.grid(row=4,column=2)
btn_div.config(font=('vardana',28))


btn_equals = Button(root,text='+',bg='#00a65a',fg='white',width=10,height=4,command=get_result)
btn_equals.grid(row=1,column=0)
btn_equals.config(font=('vardana',28))



root.mainloop()