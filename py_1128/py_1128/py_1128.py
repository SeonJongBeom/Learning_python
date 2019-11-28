####
#tkinter사용
#* : 모든것
#? : 와일드 카드
#3* -> 3자리 아무거나
#* 모든것, ? 하나만

from tkinter import * #-> tkinter의 모든것을 가져옴.

window = Tk() # 루트 윈도우 생성
label = Label(window, text = "Hello World!") #레이블은 문자
label.pack() # 텍스트를 표시할 정도로만 레이블 위젯의 크기를 축소
#pack을 해야 윈도우에 찍힘

window.mainloop()

from tkinter import * #-> tkinter의 모든것을 가져옴.

window = Tk() # 루트 윈도우 생성
b1 = Button(window, text = "이것이 파이썬 버튼입니다.")
b1.pack()

window.mainloop()

from tkinter import *

window = Tk()
b1 = Button(window, text = "첫번째 버튼.")
b2 = Button(window, text = "두번째 버튼.")
b1.pack()
b2.pack()

window.mainloop()

from tkinter import *

window = Tk()
b1 = Button(window, text = "첫번째 버튼.")
b2 = Button(window, text = "두번째 버튼.")

b1.pack(side = LEFT)
b2.pack(side = LEFT)

window.mainloop()

from tkinter import *

window = Tk()
b1 = Button(window, text = "첫번째 버튼.")
b2 = Button(window, text = "두번째 버튼.")

b1.pack(side = LEFT, padx = 10)#왼쪽과 오른쪽에 픽셀을 추가 10만큼
b2.pack(side = LEFT, padx = 10)#pady는 상단과 하단에 픽셀을 추가x랑y가 방향임

window.mainloop()

from tkinter import *

window = Tk()
b1 = Button(window, text = "첫번째 버튼.")
b2 = Button(window, text = "두번째 버튼.")

b1.pack(side = LEFT, padx = 10)#왼쪽과 오른쪽에 픽셀을 추가 10만큼
b2.pack(side = LEFT, padx = 10)#pady는 상단과 하단에 픽셀을 추가x랑y가 방향임

b1["text"] = "One"#딕셔너리처럼 사용
b2["text"] = "Two"

window.mainloop()

from tkinter import *

def callback():
	button["text"] = "버튼이 클릭되었음!"#변수명이 같아야함!!!!!!button으로

window = Tk()
button = Button(window, text = "클릭", command = callback)
button.pack(side = LEFT)
window.mainloop()

from tkinter import *

class App:
	def __init__(self):
		window = Tk()
		helloB = Button(window, text = "Hello", command = self.hello, fg = "red")
		helloB.pack(side = LEFT)
		quitB = Button(window, text = "Quit", command = self.quit)
		quitB.pack(side = LEFT)
		window.mainloop()

	def hello(self):
		print("Hello 버튼이 클릭되었음!")

	def quit(self):
		print("Quit 버튼이 클릭되었음!")

App()

#배치관리자 Grid(2차원 배열처럼 넣음), pack, place(안씀)

from tkinter import *
window = Tk()
button = Button(window, text = "버튼을 클릭하세요")
button.pack()

button["fg"] = "yellow"
button["bg"] = "green"

window.mainloop()
#bg배경 fg전경

from tkinter import *
window = Tk()
coloer = colorchooser.askcolor()
print(color)
window.mainloop()

#("Times", 10, "bold")
#("Helvetica", 10, "bold italic")
#("Symbol", 8)

from tkinter import *
window = Tk()
w = Label(text = "Helvetica", font = "Helvetica 16")
w.pack()
window.mainloop()

#window = Tk()랑 배치자랑 window.mainploop()는 거의 세트

import tkinter as tk
import tkinter.font as font
#from과 *로 전부 가져오지 않아서 일일이 직접 넣어줘야됨 (tk. 이나 font.을 쓰는 이유!)
class App:
	def __init__(self):
		root = tk.Tk()

		self.customFont = font.Font(family = "Helvetica", size = 12)

		buttonframe = tk.Frame()
		label = tk.Label(root, text = "Hello, World!", font = self.customFont)
		buttonframe.pack()
		label.pack()

		bigger = tk.Button(root, text = "폰트를 크게", command = self.BigFont)
		smaller = tk.Button(root, text = "폰트를 작게", command = self.SmallFont)
		bigger.pack()
		smaller.pack()

		root.mainloop()

	def BigFont(self):
		size = self.customFont["size"]
		self.customFont.configure(size = size + 2)

	def SmallFont(self):
		size = self.customFont["size"]
		self.customFont.configure(size = size - 2)

app = App()

#label 텍스트를 표시하는 위젯

####
#레이블로 화면에 이미지 표시하기
from tkinter import *

window = Tk()
photo =PhotoImage(file = "C:\\Users\\선종범\\source\\repos\\SeonJongBeom\\Learning_python\\py_1128\\py_1128\\1502411779659m0.jpg")
w = Label(window, image = photo)
w.photo = photo
w.pack()
window.mainloop()

####
#레이블의 색상과 폰트 변경하기
from tkinter import *

window = Tk()

Label(window, text = "Times Font 폰트와 빨강색을 사용합니다.", fg = "red", font = "Times 32 bold italic").pack()
Label(window, text = "Helvetica 폰트와 녹색을 사용합니다.", fg = "blue", bg = "yellow",font = "Helvetica 32 bold italic").pack()

window.mainloop()

from tkinter import *

window = Tk()
Label(window, text = "이름").grid(row = 0)
Label(window, text = "나이").grid(row = 1)

e1 = Entry(window)#그냥 빈칸 삽입
e2 = Entry(window)

e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)

window.mainloop()

from tkinter import *

def show():
	print("이름 : %s\n 나이: %s" % (e1.get(), e2.get()))

parent =Tk()
Label(parent, text = "이름").grid(row = 0)
Label(parent, text = "나이").grid(row = 1)

e1 = Entry(parent)#그냥 빈칸 삽입
e2 = Entry(parent)

e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)

Button(parent, text = "보이기", command = show).grid(row = 3, column=1, sticky = W, pady = 4)
Button(parent, text = "종료", command = parent.quit).grid(row = 3, column=0, sticky = W, pady = 4)

mainloop()

from tkinter import *

window = Tk()
T = Text(window, height = 5, width = 60)
T.pack()
T.insert(END, "테스트 위젯은 여러 줄의 \n 텍스트를 표시할 수 있습니다.")
mainloop()

from tkinter import *
from math import *

def calculate(event):
	label.configure(text = "결과:" + str(eval(entry.get())))#엔트리에서 값을 받아올때 get사용
	#eval()을 사용하면 문자열의 수식 계산, configure는 값을 바꿔서 넣어줌.
window = Tk()

Label(window, text = "파이썬 수식 입력:").pack()
entry = Entry(window)
entry.bind("<Return>", calculate)#bind 넣는다는 뜻 Return은 enter입력시
entry.pack()

label = Label(window, text = "결과")
label.pack()

window.mainloop()

import time
from tkinter import *
import random

window = Tk()
canvas = Canvas(window, width = 400, height = 300)
canvas.pack()
id = canvas.create_oval(10,100,50,150,fill = "#0000FF")

for i in range(100):
	canvas.move(id, 3, 0) #x,y 방향 이동거리
	window.update()
	time.sleep(0.005)

from tkinter import * 
window  = Tk()
canvas = Canvas(window, width = 400, height = 300)
canvas.pack()

id = canvas.create_oval(10,100,50,150, fill = "green")

def move_right(event):
	canvas.move(id, 5,0)
canvas.bind_all("<KeyPress-Right>", move_right)

window.mainloop()

from tkinter import *

window =Tk()
choice = IntVar()

Label(window, text = "가장 선호하는 프로그래밍 언어를 선택하시오", justify = LEFT, padx = 20).pack()
Radiobutton(window, text = "Python", padx = 20, variable = choice, value = 1).pack(anchor =W)#왼쪽에 붙인다.
Radiobutton(window, text = "C", padx = 20, variable = choice, value = 2).pack(anchor =W)#왼쪽에 붙인다.
Radiobutton(window, text = "Java", padx = 20, variable = choice, value = 3).pack(anchor =W)#왼쪽에 붙인다.
Radiobutton(window, text = "Swift", padx = 20, variable = choice, value = 4).pack(anchor =W)#왼쪽에 붙인다.

window.mainloop()

from tkinter import *

window =Tk()
choice = IntVar()

Label(window, text = "가장 선호하는 프로그래밍 언어를 선택하시오", justify = LEFT, padx = 20).pack()
Checkbutton(window, text = "Python", padx = 20, variable = choice, value = 1).pack(anchor =W)#왼쪽에 붙인다.
Checkbutton(window, text = "C", padx = 20, variable = choice, value = 2).pack(anchor =W)#왼쪽에 붙인다.
Checkbutton(window, text = "Java", padx = 20, variable = choice, value = 3).pack(anchor =W)#왼쪽에 붙인다.
Checkbutton(window, text = "Swift", padx = 20, variable = choice, value = 4).pack(anchor =W)#왼쪽에 붙인다.

window.mainloop()

from tkinter import *

window = Tk()
lb = Listbox(window, height = 1)#heigth을개수에 맞춰줘야됨
lb.pack()
lb.insert(END, "Python")
lb.insert(END, "C")
lb.insert(END, "Java")
lb.insert(END, "Swift")

window.mainloop()
