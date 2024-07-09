import tkinter as tk 


calculation = ''

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
    
    


def eval_calculate():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, calculation)

    except:
        clear_field()
        text_result.insert(1.0, 'Erro')


def clear_field():
    global calculation
    calculation = ''
    text_result.delete(1.0, 'end')

root = tk.Tk()


root.title('Calculadora')
root.geometry('400x415')

text_result = tk.Text(root, height=2, width=16, font=('Arial', 16), bg='#eee', bd=5, relief=tk.SUNKEN)
text_result.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

btn_params = {'padx': 10,
              'pady':10,
              'bd' : 3,
              'fg':'white',
              'bg':'#333',
              'font': ('Arial', '18'),
              'width': 5
              }

btn_1 = tk.Button(root, text='1', **btn_params, command= lambda: add_to_calculation(1))
btn_1.grid(row=1, column=0)

btn_2 = tk.Button(root, text='2', **btn_params, command= lambda: add_to_calculation(2))
btn_2.grid(row=1, column=1)

btn_3 = tk.Button(root, text='3', **btn_params, command= lambda: add_to_calculation(3))
btn_3.grid(row=1, column=2)

btn_4 = tk.Button(root, text='4', **btn_params, command= lambda: add_to_calculation(4))
btn_4.grid(row=2, column=0)

btn_5 = tk.Button(root, text='5', **btn_params, command= lambda: add_to_calculation(5))
btn_5.grid(row=2, column=1)

btn_6 = tk.Button(root, text='6', **btn_params, command= lambda: add_to_calculation(6))
btn_6.grid(row=2, column=2)

btn_7 = tk.Button(root, text='7', **btn_params, command= lambda: add_to_calculation(7))
btn_7.grid(row=3, column=0)

btn_8 = tk.Button(root, text='8', **btn_params, command= lambda: add_to_calculation(8))
btn_8.grid(row=3, column=1)

btn_9 = tk.Button(root, text='9', **btn_params, command= lambda: add_to_calculation(9))
btn_9.grid(row=3, column=2)

btn_0 = tk.Button(root, text=0, **btn_params, command= lambda: add_to_calculation(0))
btn_0.grid(row=4, column=1)


btn_plus = tk.Button(root, text='+', **btn_params, command = lambda: add_to_calculation('+'))
btn_plus.grid(row=1, column=3)


btn_minus = tk.Button(root, text='-', **btn_params, command= lambda:add_to_calculation('-'))
btn_minus.grid(row=2, column=3)


btn_multi = tk.Button(root, text='x', **btn_params, command= lambda: add_to_calculation('*'))
btn_multi.grid(row=3, column=3)

btn_div = tk.Button(root, text='/', **btn_params, command= lambda: add_to_calculation('/'))
btn_div.grid(row=4, column=3)

btn_equal = tk.Button(root, text='=', **btn_params, command=eval_calculate)
btn_equal.grid(row=5, column=3)

btn_clean = tk.Button(root, text='C', **btn_params, command=clear_field)
btn_clean.grid(row=4, column=0)

btn_dot = tk.Button(root, text='.', **btn_params, command= lambda: add_to_calculation('.'))
btn_dot.grid(row=4, column=2)

btn_right_parent = tk.Button(root, text=')', **btn_params, command= lambda: add_to_calculation(')'))
btn_right_parent.grid(row=5, column=2)

btn_left_parent = tk.Button(root, text='(', **btn_params, command= lambda: add_to_calculation('('))
btn_left_parent.grid(row=5, column=1)



root.mainloop()