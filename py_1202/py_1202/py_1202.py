####
#배치 관리자

#격자 배치 관리자는 위젯을 테이블 형태로 배치한다.

from tkinter import*
window = Tk()

b1 = Button(window, text = "One")
b2 = Button(window, text = "Two")
b3 = Button(window, text = "Three")
b4 = Button(window, text = "Four")

b1.grid(row = 0, column = 0)
b2.grid(row = 1, column = 0)
b3.grid(row = 0, column = 1)
b4.grid(row = 1, column = 1)

window.mainloop()

from tkinter import*

window = Tk()

Label(window, text = "박스 #1", bg = "red", fg="white").pack()
Label(window, text = "박스 #2", bg = "green", fg="black").pack()
Label(window, text = "박스 #3", bg = "blue", fg="white").pack()

window.mainloop()

from tkinter import*

#i번쨰 버튼을 누를 수 있는지 겁사한다, 누를 수 있으면 x나o를 표시한다.
def checked(i):
	global player
	button = list[i] #리스트에서 i번째 버튼 객체를 가져온다.

	#버튼이 초기항태가 아니면 이미 누른 버튼이므로 아무것도 하지 않고 리턴한다.

	if button["text"] != "		":
		return
	button["text"] = "	"+ player + "	"
	button["bg"] = "yellow"
	if player =="X":
		player = "O"
		button["bg"] = "yellow"
	else:
		player = "X"
		button["bg"] = "lightgreen"

window = Tk()		#윈도우를 생성
player = "X"		#시작은 플레이어 X이다.
list = []
#9개의 버튼을 생성하여 격자 형태로 윈도우에 배치한다.
for i in range(9):
	b = Button(window, text = "		", command = lambda k = i: checked(k))
	b.grid(row = i//3, column = i%3)
	list.append(b)

window.mainloop()

import tkinter as tk

def startTimer():
	if (running):
		global timer
		timer += 1
		timeText.configure(text = str(timer))
	window.after(10,startTimer)

def start():
	global running
	running = True

def stop():
	global running
	running = False

running = False

window = tk.Tk()

timer = 0

timeText = tk.Label(window, text = "0", font = ("Helvetica", 80))
timeText.pack()

startButton = tk.Button(window, text = "시작", bg = "yellow", command = start)
startButton.pack(fill = tk.BOTH)

stopButton = tk.Button(window, text = "중지", bg = "yellow", command = stop)
stopButton.pack(fill = tk.BOTH)

startTimer()

window.mainloop()

####
#이벤트 처리

from tkinter import*
window = Tk()

def callback(event):
	print(event.x, event.y, "에서 마우스 이벤트 발생")

frame = Frame(window, width = 100, height = 100)
frame.bind("<Button-1>", callback)
frame.pack()

window.mainloop()


from tkinter import*
window = Tk()

def key(event):
	print(repr(event.char),"가 눌렀습니다.")

def callback(event):
	frame.focus_set()
	print(event.x, event.y, "에서 마우스 이벤트 발생")

frame = Frame(window, width = 100, height = 100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

window.mainloop()
