####
#p. 105 3번
a = input("> 1번째 숫자: ")
b = input("> 2번째 숫자: ")
print()
print("{} + {} = {}".format(a, b, int(a)+int(b)))

####
#p. 105 4번
string = "hello"

string.upper()
print("A지점 : ",string)

print("B지점 : ",string.upper())

####
#p. 125 4번
a = int(input("> 1번째 숫자: "))
b = int(input("> 2번째 숫자: "))
print()

if a>b:
	print("첫번째로 입력했던 {}가 {}보다 더 큽니다.".format(a, b))
if a < b:
	print("두번째로 입력했던 {}가 {}보다 더 큽니다.".format(b, a))

####
#p. 137 4번
str_input = input("태어난 해를 입력해 주세요> ")
birth_year = int(str_input) % 12

if birth_year == 0:
	print("원숭이 띠입니다.")
elif birth_year == 1:
	print("닭 띠입니다.")
elif birth_year == 2:
	print("개 띠입니다.")
elif birth_year == 3:
	print("돼지 띠입니다.")
elif birth_year == 4:
	print("쥐 띠입니다.")
elif birth_year == 5:
	print("소 띠입니다.")
elif birth_year == 6:
	print("범 띠입니다.")
elif birth_year == 7:
	print("토끼 띠입니다.")
elif birth_year == 8:
	print("용 띠입니다.")
elif birth_year == 9:
	print("뱀 띠입니다.")
elif birth_year == 10:
	print("말 띠입니다.")
elif birth_year == 11:
	print("양 띠입니다.")