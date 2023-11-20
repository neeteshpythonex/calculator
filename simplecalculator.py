#Example: A simple calculator
import tkinter as tk  
from functools import partial  
   
#function for sum
def call_sum(label_result, n1, n2):  
    num1 = (n1.get())  
    num2 = (n2.get())  
    result = int(num1)+int(num2)  
    label_result.config(text="Result = %d" % result)  
    return

#function for product
def call_multi(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)*int(num2)
    label_result.config(text="Result = %d" % result)

#function for division
def call_Div(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)/int(num2)
    label_result.config(text="Result = %d" % result)

#function for difference
def call_subt(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)-int(num2)
    label_result.config(text="Result = %d" % result)

#design the window
root = tk.Tk()  
root.geometry('400x200')  

#title of the window
root.title('Calculator')
   
number1 = tk.StringVar()  
number2 = tk.StringVar()  
  
labelNum1 = tk.Label(root, text="A").grid(row=1, column=0)  
labelNum2 = tk.Label(root, text="B").grid(row=2, column=0)  
  
labelResult = tk.Label(root)  
  
labelResult.grid(row=7, column=2)  

entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)  
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)  

#calling the sum function and created its button
call_result = partial(call_sum, labelResult, number1, number2)  
buttonCal = tk.Button(root, text="+", command=call_result).grid(row=3, column=1)

#calling the multi function and created its button
call_result = partial(call_multi, labelResult, number1, number2)
buttonCal = tk.Button(root, text="X", command=call_result).grid(row=3, column=2)

#calling the division function and created its button
call_result = partial(call_Div, labelResult, number1, number2)
buttonCal = tk.Button(root, text="/", command=call_result).grid(row=4, column=1)

#calling the difference function and created its button
call_result = partial(call_subt, labelResult, number1, number2)
buttonCal = tk.Button(root, text="-", command=call_result).grid(row=4, column=2)

root.mainloop()
