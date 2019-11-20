####
#p.226 1-1
def f(x):
	return 2*x+1
print(f(10))

#p.226 1-2
def f(x):
	return x*x + 2*x + 1
print(f(10))

####
#p.227 2
def mul(*values):
	result = 1
	for i in values:
		result *= i
	return result
print(mul(5,7,9,10))

def factorial(n):
	if n == 0:
		return 1
	else:
		return n*factorial(n-1)

####
#p.243 1
def flatten(data):
	result = []
	for i in data:
		if type(i) == list:
			result += flatten(i)
		else:
			result.append(i)
	return result
example = [[1,2,3],[4,[5,6]],7,[8,9]]
print("원본:", example)
print("변환:", flatten(example))

####
#p.268 1
numbers = [1,2,3,4,5,6]
print("::".join([str(i)for i in numbers]))

####
#p. 269 2
numbers = list(range(1, 10+1))

print("#홀수만 추출하기")
print(list(filter(lambda x : x % 2 == 1, numbers)))
print()

print("#3 이상, 7미만 추출하기")
print(list(filter(lambda x : x >= 3 and x < 7, numbers)))
print()

print("# 제곱해서 50 미만 추출하기")
print(list(filter(lambda x : (x ** 2) < 50, numbers)))


####
#과제 1번 주사위 값 리스트 만들기
dice = []
for i in range(1,7):
	tmp = []
	for k in range(1,7):
		tmp.append(i+k)
	dice.append(tmp)
print(dice)

####
#과제 2번 리스트 함축
#2-1 30이하의 수 중 짝수의 제곱만 출력
print([x**2 for x in range(1,31) if x % 2 == 0])

#2-2 50이하의 수 중 1의 자리의 수가 3,6,9인 것만 출력
print([x for x in range(1, 50) if x%10 == 3 or x % 10 == 6 or x % 10 == 9])

####
#과제 3번 섭씨 화씨 변환
while True:
	print("'C' 섭씨온도에서 화씨온도로 변환")
	print("'F' 화씨온도에서 섭씨온도로 변환")
	print("'Q' 종료")
	choice = input("메뉴에서 선택하세요.")
	if choice == "c" or choice == "C":
		c = int(input("섭씨온도: "))
		print("화씨온도: ",c * 9 / 5 + 32)
	elif choice == "f" or choice == "F":
		f = int(input("화씨온도: "))
		print("섭씨온도: ",(f-32) / 5 / 9)
	elif choice == "q" or choice == "Q":
		print("프로그램을 종료합니다.")
		break
	else:
		print("다시 입력해 주세요")

####
#과제 3번 비밀번호 생성기
import string
import random
for k in range(3):
	password = ""

	for i in range(6):
		if random.randrange(1,3) % 2 == 0:
			password += string.ascii_letters[random.randrange(0, len(string.ascii_letters))]
		else:
			password += string.digits[random.randrange(0, len(string.digits))]

	print(password)

####
#과제 4번 람다를 이용한 계산기
while True:
	cnt = 0
	print("1.덤셈")
	print("2.뺄셈")
	print("3.곱셈")
	print("4.나눗셈")
	print("5.종료")

	choice = input("계산을 선택하세요: ")

	if choice == '1':
		sum = lambda x,y: x+y
		x  = input("첫번째 수를 입력하세요: ")
		for i in x:
			if not(ord(i) >= 48 and ord(i) <= 57):
				cnt += 1
		y  = input("두번째 수를 입력하세요: ")
		for i in y:
			if not(ord(i) >= 48 and ord(i) <= 57):
				cnt += 1
		if cnt > 0:
			print("다시 입력해주세요")
			continue
		x, y = int(x), int(y)

		print("정수의 합: ", sum(x,y))

	elif choice == '2':
		diff = lambda x,y: x-y
		x  = input("첫번째 수를 입력하세요: ")
		for i in x:
			if not(ord(i) >= 48 and ord(i) <= 57):
				cnt += 1
		y  = input("두번째 수를 입력하세요: ")
		for i in y:
			if not(ord(i) >= 48 and ord(i) <= 57):
				cnt += 1
		if cnt > 0:
			print("다시 입력해주세요")
			continue
		x, y = int(x), int(y)
		print("정수의 차: ", diff(x,y))

	elif choice == '3':
		mul = lambda x,y: x*y
		x  = input("첫번째 수를 입력하세요: ")
		for i in x:
			if not(ord(i) >= 48 and ord(i) <= 57):
				cnt += 1
		y  = input("두번째 수를 입력하세요: ")
		for i in y:
			if not(ord(i) >= 48 and ord(i) <= 57):
				cnt += 1
		if cnt > 0:
			print("다시 입력해주세요")
			continue
		x, y = int(x), int(y)
		print("정수의 곱: ", mul(x,y))

	elif choice == '4':
		div = lambda x,y: x/y
		x  = input("첫번째 수를 입력하세요: ")
		for i in x:
			if not(ord(i) >= 48 and ord(i) <= 57):
				cnt += 1
		y  = input("두번째 수를 입력하세요: ")
		for i in y:
			if not(ord(i) >= 48 and ord(i) <= 57):
				cnt += 1
		if cnt > 0:
			print("다시 입력해주세요")
			continue

		x, y = int(x), int(y)
		print("정수의 나누기: ", div(x,y))
	elif choice == '5':
		print("종료합니다.")
		break
	else:
		print("다시 입력해주세요")
