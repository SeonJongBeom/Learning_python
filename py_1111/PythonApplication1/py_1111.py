#동전 주는 프로그램
price = int(input("물건값을 입력하시오: "))

thou_em = int(input("1000원 지폐개수:"))
f_hund_em = int(input("500원 동전개수:"))
hund_em = int(input("100원 동전개수:"))

price = (1000*thou_em + 500*f_hund_em + 100*hund_em) - price

thou = price // 1000
price = price % 1000
f_hund = price // 500
price = price % 500
hund = price // 100
price = price % 100
ten = price // 10
price = price % 10

print("1000원:", thou)
print("500원:", f_hund)
print("100원:", hund)
print("10원:", ten)

print("나머지 :", price)
####
a = 10
b = 20
c = 30
d = 40

a,b = b,a			#c는 안되는디 파이썬은 됨! (서로 교환해줌, 별다른 변수를 넣어줄 필요가 없음)
a,b,c,d = d,c,b,a
print(a,b,c,d)

####
a = 10
b = 20
c = 30
d = 40

if (a>b):
	print("a가 b보다 큽니다.")
else:
	print("b가 a보다 큽니다.")

####
#터틀 그래픽
import turtle
t = turtle.Pen()

while (True):
	direction = input("왼쪽 = left, 오른쪽 = right:")
	if (direction) == "left":
		t.left(60)
		t.forward(50)
	if (direction) == "right":
		t.right(60)
		t.forward(50)

####
#홀수 짝수 프로그램
count = 0
while(count < 10):
	number = int(input("정수를 입력하세요"))
	if (number % 2) == 0:
		print(number,"는 짝수입니다.")
	else:
		print(number,"는 홀수입니다.")
	count += 1

####
#물건값 계산
price = int(input("구입 금액을 입력하시오: "))
if (price > 100000):
	print("지불금액은", price - (price*(5/100)),"입니다.")
else:
	print("지불금액은", price,"입니다.")

####
#졸업 학점 검사하기
grade = int(input("이수한 학점수를 입력하시오: "))
score = float(input("평점을 입력하시오: "))

if (grade >= 140 and score >= 2):
	print("졸업할수 있습니다.")
else:
	print("졸업할수 없습니다.")

####
#책 p177 날짜/시간 출력하기
import datetime

now = datetime.datetime.now()

print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

if 3 <= now.month <= 5:
	print("이번달은", now.month, "월로 봄입니다.")

if 6 <= now.month <= 8:
	print("이번달은", now.month, "월로 여름입니다.")

if 9 <= now.month <= 11:
	print("이번달은", now.month, "월로 가을입니다.")

if now.month == 12 or 1 <= now.month <= 2:
	print("이번달은", now.month, "월로 겨울입니다.")
