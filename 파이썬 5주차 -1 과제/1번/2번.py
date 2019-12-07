from tkinter import *
def click(key):
	if key == '=': # “=” 버튼이면 수식을 계산하여 결과를 표시한다.
		try:
			result = eval(entry.get())		#엔트리로부터 수식을 받아와서 계산하고 result에 저장
			entry.delete(0, END)			#엔트리의 모든것을 지우고
			entry.insert(END, str(result))	#result값을 엔트리에 출력
		except:
			entry.insert(END, "오류!")		#엔트리 안에 이상한게 들어있으면 오류 출력
	elif key == 'C':
		entry.delete(0, END)				#버튼의 값이 C이면 엔트리의 모든 내용을 지움
	else:
		entry.insert(END, key)				#C나 =가아니면 버튼의 text내용을 엔트리에 출력
window = Tk()
window.title("간단한 계산기")
buttons = [				#반복문으로 버튼을 생성하기 위해 미리 리스트로 각 기호를 만듬
	'7', '8', '9', '+', 'C',
	'4', '5', '6', '-', ' ',
	'1', '2', '3', '*', ' ',
	'0', '.', '=', '/', ' ' ]
# 반복문으로 버튼을 생성한다.
i=0
for b in buttons:
	cmd = lambda x=b: click(x)
	b = Button(window,text=b,width=5,relief='ridge',command=cmd)
	b.grid(row=i//5+1,column=i%5)
	i += 1
# 엔트리 위젯은 맨 윗줄의 5개의 셀에 걸쳐서 배치된다.
entry = Entry(window, width=33, bg="yellow")
entry.grid(row=0, column=0, columnspan=5)
window.mainloop()