####
#두수중 큰수 출력
a = int(input("첫번째 수를 입력하세요: "))
b = int(input("두번째 수를 입력하세요: "))

if a > b:
	print("큰수는 ", a, "입니다.")
if a < b:
	print("큰수는 {}입니다.".format(b))

####
#중앙 글자 출력하기
string = input("문자열을 입력하시오 : ")
length = len(string)

if length % 2 == 1:
	print("중앙 글자는 ",string[length//2])
else:
	print("중앙 글자는 ",string[length//2-1], string[length//2])

####
#숫자 맞추기 게임
import random
c_number = random.randrange(1,100)
p_number = int(input("숫자를 맞춰보세요 : "))

if c_number < p_number:
	print("너무큼!")
elif c_number > p_number:
	print("너무 작음!")
else:
	print("같음")

####
import random
c_choice = random.randrange(0,2)
p_choice = input("(가위, 바위, 보)중에서 하나를 선택하세요: ")

if c_choice == 0:
	c_choice = "가위"
elif c_choice == 1:
	c_choice = "바위"
elif c_choice == 2:
	c_choice = "보"

print("컴퓨터", c_choice, "사용자", p_choice)

if c_choice == p_choice:
	print("무승부 입니다.")
elif c_choice == "가위" and p_choice == "바위":
	print("이겼습니다.")
elif c_choice == "가위" and p_choice == "보":
	print("졌습니다.")
elif c_choice == "바위" and p_choice == "보":
	print("이겼습니다.")
elif c_choice == "바위" and p_choice == "가위":
	print("졌습니다.")
elif c_choice == "보" and p_choice == "가위":
	print("이겼습니다.")
elif c_choice == "보" and p_choice == "바위":
	print("졌습니다.")

####
#면적 계산기
choice = int(input("도형을 선택 하시오(1:사각형, 2:삼각형, 3:원) : "))

if choice == 1:
	wide = int(input("가로 : "))
	hight = int(input("세로 : "))
	print("결과 : ", wide*hight)

elif choice == 2:
	wide = int(input("가로 : "))
	hight = int(input("세로 : "))
	print("결과 : ", wide*hight/2)

elif choice == 3:
	radius = int(input("반지름 : "))
	print("결과 : ", radius**2*3.14)