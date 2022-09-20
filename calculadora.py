from tkinter import *

"""variables"""
operations = ""

reset_screen = False

results = 0

counter_operation = 0

def number_presset(num):
	global operations
	global reset_screen


	if reset_screen != False:
		screen_number.set(num)
		reset_screen = False

	else:
		screen_number.set(screen_number.get() + num)

def addition(numb):
	global counter_operation
	global operations
	global results
	global reset_screen

	if counter_operation == 0:
		results = float(numb)

	elif counter_operation >= 1:
		results = float(results) + float(numb)
	

	screen_number.set(float(results))
	results = screen_number.get()

	counter_operation +=1
	operations = "suma"
	reset_screen = True

def subtraction(numb):
	global counter_operation
	global operations
	global results
	global reset_screen

	if counter_operation == 0:
		results = float(numb)

	elif counter_operation >= 1:
		results = float(results) - float(numb)
	

	screen_number.set(float(results))
	results = screen_number.get()

	counter_operation +=1
	operations = "resta"
	reset_screen = True

def multiply(numb):
	global counter_operation
	global operations
	global results
	global reset_screen

	if counter_operation == 0:
		results = float(numb)

	elif counter_operation >= 1:
		results = float(results) * float(numb)
	

	screen_number.set(float(results))
	results = screen_number.get()

	counter_operation +=1
	operations = "multiplica"
	reset_screen = True


root=Tk()
root.title("Andora")
#root.iconbitmap("logoico.ico")
root.config(bg="blue")
root.resizable(False,False)

my_frame=Frame(root)
my_frame.pack()
my_frame.config(bg="blue")
my_frame.config(cursor="hand2")



screen_number=StringVar() 
screen_calculator=Entry(my_frame, width=35, textvariable=screen_number)
screen_calculator.grid(row=1, column=1, padx=0, pady=20, columnspan=4) 
screen_calculator.config(background="white", fg="black", justify="right")

#------------fila de botones numero 1------------------------------------------------------------------------------------
CE_button=Button(my_frame, text="CE", width=5, height=2)
CE_button.config(bd=10)
CE_button.config(relief="groove")
CE_button.grid(row=2, column=1)

percentege_button=Button(my_frame, text="%", width=5, height=2)
percentege_button.config(bd=10)
percentege_button.config(relief="groove")
percentege_button.grid(row=2, column=2)

power_button=Button(my_frame, text="x²", width=5, height=2)
power_button.config(bd=10)
power_button.config(relief="groove")
power_button.grid(row=2, column=3)
 
root_button=Button(my_frame, text="√", width=5, height=2)
root_button.config(bd=10)
root_button.config(relief="groove")
root_button.grid(row=2, column=4)

#------------fila de botones numero 2------------------------------------------------------------------------------------
button7=Button(my_frame, text="7", width=5, height=2, command=lambda:number_presset("7"))
button7.config(bd=10)
button7.config(relief="groove")
button7.grid(row=3, column=1)

button8=Button(my_frame, text="8", width=5, height=2, command=lambda:number_presset("8"))
button8.config(bd=10)
button8.config(relief="groove")
button8.grid(row=3, column=2)

button9=Button(my_frame, text="9", width=5, height=2, command=lambda:number_presset("9"))
button9.config(bd=10)
button9.config(relief="groove")
button9.grid(row=3, column=3)
 
divisio_button=Button(my_frame, text="/", width=5, height=2)
divisio_button.config(bd=10)
divisio_button.config(relief="groove")
divisio_button.grid(row=3, column=4)

#----------------fila de botones numero 3------------------------------------------------------------------------
button6=Button(my_frame, text="6", width=5, height=2, command=lambda:number_presset("6"))
button6.config(bd=10)
button6.config(relief="groove")
button6.grid(row=4, column=3)

button5=Button(my_frame, text="5", width=5, height=2, command=lambda:number_presset("5"))
button5.config(bd=10)
button5.config(relief="groove")
button5.grid(row=4, column=2)

button4=Button(my_frame, text="4", width=5, height=2, command=lambda:number_presset("4"))
button4.config(bd=10)
button4.config(relief="groove")
button4.grid(row=4, column=1)
 
multiplication_button=Button(my_frame, text="x", width=5, height=2, command=lambda:multiply(screen_number.get()))
multiplication_button.config(bd=10)
multiplication_button.config(relief="groove")
multiplication_button.grid(row=4, column=4)

#----------------fila de botones numero 4------------------------------------------------------------------------
button3=Button(my_frame, text="3", width=5, height=2, command=lambda:number_presset("3"))
button3.config(bd=10)
button3.config(relief="groove")
button3.grid(row=5, column=3)

button2=Button(my_frame, text="2", width=5, height=2, command=lambda:number_presset("2"))
button2.config(bd=10)
button2.config(relief="groove")
button2.grid(row=5, column=2)

button1=Button(my_frame, text="1", width=5, height=2, command=lambda:number_presset("1"))
button1.config(bd=10)
button1.config(relief="groove")
button1.grid(row=5, column=1)
 
subtraction_button=Button(my_frame, text="-", width=5, height=2, command=lambda:subtraction(screen_number.get()))
subtraction_button.config(bd=10)
subtraction_button.config(relief="groove")
subtraction_button.grid(row=5, column=4)
#----------------fila de botones numero 5------------------------------------------------------------------------
comma_button=Button(my_frame, text=".", width=5, height=2, command=lambda:number_presset("."))
comma_button.config(bd=10)
comma_button.config(relief="groove")
comma_button.grid(row=6, column=1)

button0=Button(my_frame, text="0", width=5, height=2, command=lambda:number_presset("0"))
button0.config(bd=10)
button0.config(relief="groove")
button0.grid(row=6, column=2)

equal_button=Button(my_frame, text="=", width=5, height=2)
equal_button.config(bd=10)
equal_button.config(relief="groove")
equal_button.grid(row=6, column=3)
 
addition_button=Button(my_frame, text="+", width=5, height=2, command=lambda:addition(screen_number.get()))
addition_button.config(bd=10)
addition_button.config(relief="groove")
addition_button.grid(row=6, column=4)











root.mainloop()
