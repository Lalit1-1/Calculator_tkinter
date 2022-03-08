from tkinter import *
from tkinter.messagebox import *

# some useful variable
font=('Verdana',22, 'bold')

#important functions
def clear():
    ex = textField.get()
    ex = ex[0:len(ex) -1]
    textField.delete(0,END)
    textField.insert(0,ex)


def all_clear():
    textField.delete(0,END)

def click_btn_function(event):
    print("btn clicked")
    b = event.widget
    text=b['text']
    print(text)

    if text == 'x':
        textField.insert(END,"*")
        return

    if text == '=':
        try:
            ex = textField.get()
            answer = eval(ex)
            textField.delete(0, END)
            textField.insert(0, answer)
        except Exception as e:
            print("Error..", e)
            showerror("Error",e)
        return

    textField.insert(END,text)

# creating a window
window = Tk()
window.title('My Calculator')
window.geometry('480x520')

# picture label
pic=PhotoImage(file='img/cal1.png')
# headingLabel = Label(window,text="my label")
headingLabel = Label(window,image=pic)
headingLabel.pack(side=TOP, pady=10)


# heading Label
heading = Label(window, text='My Calculator', font=font)
heading.pack(side=TOP)

#textfield
textField  = Entry(window,font=font,justify=RIGHT)
textField.pack(side=TOP, pady=10, fill=X, padx=10)

# button

buttonFrame = Frame(window)
buttonFrame.pack(side=TOP,padx=10)

# adding button
temp = 1;
for i in range(0,3):
    for j in range(0,3):
        btn = Button(buttonFrame, text=str(temp), font=font, width=5, relief='ridge',activebackground='skyblue',activeforeground='yellow')
        # btn.grid(row=i,column=j, padx=3, pady=5)
        btn.grid(row=i,column=j)
        temp += 1
        btn.bind('<Button-1>', click_btn_function)

zeroBtn = Button(buttonFrame, text= '0', font=font, width=5, relief='ridge',activebackground='blue',activeforeground='yellow')
zeroBtn.grid(row=3,column=0)

dotBtn = Button(buttonFrame, text= '.', font=font, width=5, relief='ridge',activebackground='blue',activeforeground='yellow')
dotBtn.grid(row=3,column=1)

equalBtn = Button(buttonFrame, text= '=', font=font, width=5, relief='ridge',activebackground='blue',activeforeground='yellow')
equalBtn.grid(row=3,column=2)

plusBtn = Button(buttonFrame, text= '+', font=font, width=5, relief='ridge',activebackground='blue',activeforeground='yellow')
plusBtn.grid(row=0,column=3)

minusBtn = Button(buttonFrame, text= '-', font=font, width=5, relief='ridge',activebackground='blue',activeforeground='yellow')
minusBtn.grid(row=1,column=3)

multBtn = Button(buttonFrame, text= '*', font=font, width=5, relief='ridge',activebackground='blue',activeforeground='yellow')
multBtn.grid(row=2,column=3)

divideBtn = Button(buttonFrame, text= '/', font=font, width=5, relief='ridge',activebackground='blue',activeforeground='yellow')
divideBtn.grid(row=3 ,column=3)

clearBtn = Button(buttonFrame, text= 'clr', font=font, width=11, relief='ridge',activebackground='blue',activeforeground='yellow',command=clear)
clearBtn.grid(row=4 ,column=0, columnspan=2)

allClearBtn = Button(buttonFrame, text= 'allClr', font=font, width=11, relief='ridge',activebackground='blue',activeforeground='yellow', command=all_clear)
allClearBtn.grid(row=4 ,column=2, columnspan=2)

# binding all buttons
plusBtn.bind('<Button-1>', click_btn_function)
minusBtn.bind('<Button-1>', click_btn_function)
multBtn.bind('<Button-1>', click_btn_function)
divideBtn.bind('<Button-1>', click_btn_function)
dotBtn.bind('<Button-1>', click_btn_function)
equalBtn.bind('<Button-1>', click_btn_function)



window.mainloop()