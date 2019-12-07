####
#과제 1번 숫자 맞추기 게임
#배치관리자는 하나만 샤용가능함.
from tkinter import *
#from math import*
import random

com_num = random.randint(0,101)

def check():
	if com_num > int(e.get()):
		result.configure(text = "사용자가 낮음!")
	elif com_num < int(e.get()):
		result.configure(text = "사용자가 높음!")
	else:
		result.configure(text = "같음!")

def reset():
	global com_num 
	com_num= random.randint(0,101)

window = Tk()

Frame(window, width = 300, height = 500)
l = Label(window, text = "숫자게임에 오신것을 환영합니다.")
e = Entry(window)
l.pack(side = TOP)
e.pack(side = LEFT, pady = 20)

Button(window, text = "시도", fg = "green", command = check).pack(side = LEFT)
Button(window, text = "초기화", fg = "red", command = reset).pack(side = LEFT)
result = Label(window, text = "", width = 20)
result.pack(side = LEFT)

window.mainloop()