####
#터틀 그래픽으로 사각형 그리기
import turtle

p = turtle.turtle()

for k in range(0,3):
	for i in range(4):
		p.forward(40)
		p.left(90)
	p.left(20)

####
#1부터 100까지 어떤 배수의 합 구하기(몇 배수인지는 입력받기)
step = int(input("어떤배수의 합을 구할까요?:"))
number = 0
for i in range(0, 101, step):
	number += i
print("1부터 100까지의 모든 ", step, "의 배수의 합은", number, "입니다.")

####
#자리수의 합 계산하기
number = input("정수를 입력하세요 : ")
num_sum = 0
for i in range(len(number)):
	num_sum += int(number[i])
print("자리수의 합은", num_sum,"입니다.")

####
#문자열 조사
string = input("문자열을 입력하세요 : ")
alpha = 0
num = 0
space = 0
for c in string:
	if c.isalpha():
		alpha += 1
	if c.isdigit():
		num += 1
	if c.isspace():
		space += 1

print("알파벳 문자의 개수=", alpha)
print("숫자 문자의 개수=", num)
print("스페이스 문자의 개수=", space)