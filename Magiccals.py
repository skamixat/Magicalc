import tkinter
import customtkinter as ctk 
import math

def add_digit(digit):
	value = entry.get() + str(digit)
	entry.delete(0,ctk.END)
	entry.insert(0, value)
	btn8.configure(state='active')
	btn12.configure(state='active')
	btn16.configure(state='active')
	btn21.configure(state='active')

def add_ambiguous(ambiguous):
	value = entry.get() + str(ambiguous)
	entry.delete(0,ctk.END)
	entry.insert(0, value)
	btn8.configure(state='active')
	btn12.configure(state='active')
	btn16.configure(state='active')
	btn21.configure(state='active')

def add_operation(operation):
	value = entry.get() + str(operation)
	if value[-1]=='+' or '-' or 'x' or '÷':
		entry.delete(0,ctk.END)
		entry.insert(0, value)
		btn8.configure(state='disabled', text_color='#FFFFFF')
		btn12.configure(state='disabled', text_color='#FFFFFF')
		btn16.configure(state='disabled', text_color='#FFFFFF')
		btn21.configure(state='disabled', text_color='#FFFFFF')
	else:
		entry.delete(0,ctk.END)
		entry.insert(0, value)   	
		btn8.configure(state='active')
		btn12.configure(state='active')
		btn16.configure(state='active')
		btn21.configure(state='active')

def fullerasing(fullerasing):
    entry.delete(0,ctk.END)

def erasing():   
    entry.delete(len(entry.get()) - 1)
def enter(event):
	if event.char.isdigit():
		add_digit(event.char)
	elif event.char in '+-*/':
		add_operation(event.char)
	elif event.char in '()*/':
		add_ambiguous(event.char)
	elif event.char == '\r':
		solution()
	elif event.char == '\b':
		erasing()
'''
def impossible():
	label = ctk.CTkLabel(entry, text="Вышел и зашел нормально", font=('Bahnschrift Bold', 20), fg_color="transparent", text_color='#FFFFFF')
	label. (pady= 15, anchor="center")
'''
def solution():
	textprimer = entry.get()
	silos = textprimer.replace('x','*').replace('÷','/').replace('²','**2').replace('%','/100').replace(',','.')
	if '√' in textprimer:	
		tep=list(silos)[silos.find("√"):]
		doljikova=''.join(tep)
		print(doljikova)
		if '√('in textprimer:
			rak=list(silos)
			rak[int(silos.find("√("))]="math.sqrt("
			rak[int(silos.find("√("))+(len(silos[(int(silos.find("√("))):(int(silos.find(")")))]))]=")"
			silos = ''.join(rak)
		elif '+' in tep:
			rak=list(silos)
			rak[int(silos.find("√"))]="math.sqrt("
			rak.insert(int(silos.find("√"))+(len(silos[(int(doljikova.find("√"))):(int(doljikova.find("+")))])), ")")
			silos = ''.join(rak)
			print(silos)
		elif '-' in tep:
			rak=list(silos)
			rak[int(silos.find("√"))]="math.sqrt("
			rak.insert(int(silos.find("√"))+(len(silos[(int(doljikova.find("√"))):(int(doljikova.find("-")))])), ")")
			silos = ''.join(rak)
		elif '+' in tep:
			rak=list(silos)
			rak[int(silos.find("√"))]="math.sqrt("
			rak.insert(int(silos.find("√"))+(len(silos[(int(doljikova.find("√"))):(int(doljikova.find("+")))])), ")")
			silos = ''.join(rak)
		elif '*' in tep:
			rak=list(silos)
			rak[int(silos.find("√"))]="math.sqrt("
			rak.insert(int(silos.find("√"))+(len(silos[(int(doljikova.find("√"))):(int(doljikova.find("*")))])), ")")
			silos = ''.join(rak)
		elif '/' in tep:
			rak=list(silos)
			rak[int(silos.find("√"))]="math.sqrt("
			rak.insert(int(silos.find("√"))+(len(silos[(int(doljikova.find("√"))):(int(doljikova.find("/")))])), ")")
			silos = ''.join(rak)
		elif '**2' in tep:
			rak=list(silos)
			rak[int(silos.find("√"))]="math.sqrt("
			rak.insert(int(silos.find("√"))+(len(silos[(int(doljikova.find("√"))):(int(doljikova.find("**2")))])), ")")
			silos = ''.join(rak)
		elif '/100' in tep:
			rak=list(silos)
			rak[int(silos.find("√"))]="math.sqrt("
			rak.insert(int(silos.find("√"))+(len(silos[(int(doljikova.find("√"))):(int(doljikova.find("/100")))])), ")")
			silos = ''.join(rak)
		else:
			rak=list(silos)
			rak[int(silos.find("√"))]="math.sqrt("
			#rak.insert((len(silos[(int(silos.find("√"))):(int(silos.find("+")))])), ")")
			rak.append(")")
			silos = ''.join(rak)

	print(silos)
	try:
		ret = str(eval(silos))
		result=textprimer + " = " + ret
		entry.delete(0,ctk.END)
		entry.insert(0, result)
	except SyntaxError:
		
		kaban="Выйди и зайди нормально"
		entry.delete(0,ctk.END)
		entry.configure(font=('Bahnschrift', 25), justify=("right"))
		entry.insert(0,kaban)
	except NameError:
		kaban="Выйди и зайди нормально"
		entry.delete(0,ctk.END)
		entry.configure(font=('Bahnschrift', 25), justify=("right"))
		entry.insert(0,kaban)


calc = ctk.CTk()
calc.geometry("350x570")
calc.title("Максимкин калькулятор") 
calc.resizable(False, False)
calc.bind('<Key>', enter)

entry = ctk.CTkEntry(calc, width=330, height=100, corner_radius=10, font=('Bahnschrift', 25), justify=("right"))
entry.pack(pady= 15, anchor="center")


oneframe = ctk.CTkFrame(calc)
oneframe.pack(pady = 5, anchor="center")



btn1 = ctk.CTkButton(oneframe, text=f"C", width=75, height=50, fg_color="#7B68EE", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: fullerasing('C'))
btn1.grid(row=1, column=1, ipadx=0.02, ipady=6, padx=4, pady=4,)

btn2 = ctk.CTkButton(oneframe, text=f"⌫", width=75, height=50, fg_color="#7B68EE", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=erasing)
btn2.grid(row=1, column=2, ipadx=0.02, ipady=6, padx=4, pady=4,)

btn3 = ctk.CTkButton(oneframe, text=f"Х²", width=75, height=50, fg_color="#7B68EE", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: add_ambiguous('²'))
btn3.grid(row=1, column=3, ipadx=0.02, ipady=6, padx=4, pady=4,)

btn4 = ctk.CTkButton(oneframe, text=f"√Х", width=75, height=50, fg_color="#7B68EE", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: add_ambiguous('√'))
btn4.grid(row=1, column=4, ipadx=0.02, ipady=6, padx=4, pady=4,)


btn5 = ctk.CTkButton(oneframe, text=f"(", width=75, height=50, fg_color="#7B68EE", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: add_ambiguous('('))
btn5.grid(row=2, column=1, ipadx=0.02, ipady=6, padx=4, pady=4,)

btn6 = ctk.CTkButton(oneframe, text=f")", width=75, height=50, fg_color="#7B68EE", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: add_ambiguous(')'))
btn6.grid(row=2, column=2, ipadx=0.02, ipady=6, padx=4, pady=4,)

btn7 = ctk.CTkButton(oneframe, text=f"%", width=75, height=50, fg_color="#7B68EE", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: add_operation('%'))
btn7.grid(row=2, column=3, ipadx=0.02, ipady=6, padx=4, pady=4,)

btn8 = ctk.CTkButton(oneframe, text=f"÷", width=75, height=50, fg_color="#7B68EE", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: add_operation('÷'))
btn8.grid(row=2, column=4, ipadx=0.02, ipady=6, padx=4, pady=4,)


btn9 = ctk.CTkButton(oneframe, text=f"7", width=75, height=50, fg_color="#483D8B", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: add_digit(7))
btn9.grid(row=3, column=1, ipadx=0.02, ipady=6, padx=4, pady=4,)

btn10 = ctk.CTkButton(oneframe, text=f"8", width=75, height=50, fg_color="#483D8B", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: add_digit(8))
btn10.grid(row=3, column=2, ipadx=0.02, ipady=6, padx=4, pady=4,)

btn11 = ctk.CTkButton(oneframe, text=f"9", width=75, height=50, fg_color="#483D8B", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: add_digit(9))
btn11.grid(row=3, column=3, ipadx=0.02, ipady=6, padx=4, pady=4,)

btn12 = ctk.CTkButton(oneframe, text=f"x", width=75, height=50, fg_color="#7B68EE", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: add_operation('x'))
btn12.grid(row=3, column=4, ipadx=0.02, ipady=6, padx=4, pady=4,)


btn13 = ctk.CTkButton(oneframe, text=f"4", width=75, height=50, fg_color="#483D8B", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: add_digit(4))
btn13.grid(row=4, column=1, ipadx=0.02, ipady=6, padx=4, pady=4,)

btn14 = ctk.CTkButton(oneframe, text=f"5", width=75, height=50, fg_color="#483D8B", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: add_digit(5))
btn14.grid(row=4, column=2, ipadx=0.02, ipady=6, padx=4, pady=4,)

btn15 = ctk.CTkButton(oneframe, text=f"6", width=75, height=50, fg_color="#483D8B", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: add_digit(6))
btn15.grid(row=4, column=3, ipadx=0.02, ipady=6, padx=4, pady=4,)

btn16 = ctk.CTkButton(oneframe, text=f"-", width=75, height=50, fg_color="#7B68EE", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: add_operation('-'))
btn16.grid(row=4, column=4, ipadx=0.02, ipady=6, padx=4, pady=4,)


btn17 = ctk.CTkButton(oneframe, text=f"1", width=75, height=50, fg_color="#483D8B", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: add_digit('1'))
btn17.grid(row=5, column=1, ipadx=0.02, ipady=6, padx=4, pady=4,)

btn19 = ctk.CTkButton(oneframe, text=f"2", width=75, height=50, fg_color="#483D8B", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: add_digit('2'))
btn19.grid(row=5, column=2, ipadx=0.02, ipady=6, padx=4, pady=4,)

btn20 = ctk.CTkButton(oneframe, text=f"3", width=75, height=50, fg_color="#483D8B", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: add_digit('3'))
btn20.grid(row=5, column=3, ipadx=0.02, ipady=6, padx=4, pady=4,)

btn21 = ctk.CTkButton(oneframe, text=f"+", width=75, height=50, fg_color="#7B68EE", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: add_operation('+'))
btn21.grid(row=5, column=4, ipadx=0.02, ipady=6, padx=4, pady=4,)


btn22 = ctk.CTkButton(oneframe, text=f",", width=75, height=50, fg_color="#483D8B", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: add_operation(','))
btn22.grid(row=6, column=1, ipadx=0.02, ipady=6, padx=4, pady=4,)

btn23 = ctk.CTkButton(oneframe, text=f"0", width=75, height=50, fg_color="#483D8B", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: add_digit('0'))
btn23.grid(row=6, column=2, ipadx=0.02, ipady=6, padx=4, pady=4,)

btn24 = ctk.CTkButton(oneframe, text=f"=", width=75, height=50, fg_color="#8A2BE2", hover_color="#BA55D3", font=('Sofia Sans Bold', 20), command=lambda: solution())
btn24.grid(row=6, column=3, columnspan=2, ipadx=42, ipady=6, padx=4, pady=4,)


calc.mainloop()