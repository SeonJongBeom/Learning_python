####
#반복문
#형식 for i in "": ->in 뒤에 여러형태의 배열에서 하나씩 들고옴.

for i in range(0, 10001, 2): #start와 step은 0과 1의 값이 기본적으로 주어져 있어서 stop만 적어도 됨.
	print(i, end=" ") #print()에서 end = ""를 사용하면 사동줄넘김이 사라지고 ""안의 내용으로 대체됨.

####
#터틀그래픽으로 별찍기
import turtle
star = turtle.Turtle()

for i in range(5):
	star.forward(200)
	star.right(144)

####
#터틀그래픽으로 다각형 찍기
import turtle

p = turtle.Turtle()

num_sides = int(input("몇각형을 그릴까요 : "))
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
	p.forward(side_length)
	p.right(angle)

####
#while 조건식:
i = 0;
while i <5:
	print("안녕")
	i += 1
	if i == 3:
		break

####
#구구단
number = int(input("단을 입력하세요: "))
i =1
while i < 11:
	print(number,"*",i,"=",number*i)
	i+=1

####
#3의 배수의 합
sum = 0
for i in range(0, 101, 3):
	sum += i
print(sum)

####
#리스트의 합
list_a = []

for i in range(1,101):
	list_a.append(i)

print(sum(list_a))
