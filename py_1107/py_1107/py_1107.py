#1장
#기본 형식 : print(숫자), print('문자열') 여러개를 찍을려면 ','로 구분함.
#', ", 줄넘김, 탭 찍는 법 : \를 이용 ex) \', \", \n(줄넘김), \t(탭)
print(1+1)

print(52, 273, "Hello")							#print끼리 자동으로 줄넘김이됨
print("안녕하세요","저의","이름은","선종범입니다.")#띄어쓰기는 콤마를 쓰면 자동으로 됨

print(1,'\n',2, sep = "       ")				#sep으로 자동띄어쓰기양을 설정 가능
print('hello world')
print('\n \n \n \n')

#2장 자료형
#변수에 값을 할당하면 자동적으로 자료형이 정해짐
#정수 : 정수형, 실수 : 실수형, 문자 : 문자형
#주의 : 숫자는 숫자끼리 문자는 문자끼리 계산됨.
#자료형을 확신하려면 type(확인하기위한 값)을 사용하면 됨.
#문자형은 문자열 인덱스를 사용해서 출력이 가능함 이때 문자열 인덱스는 0부턱 시작함.
#연산의 종류 : +(더하기), -(빼기), *(곱하기), /(나누기), //(몫구하기), %(나머지 구하기), **(제곱)
a = 2
print(a)
a = "asdasdasd"
print(a)
a = 1.23456
print(a)
a = 'a'
print(a)
a = input()						#input의 기본형은 문자임
print(type(a))
print(a+'1234')
a =int(input())
print(a)
print(a + 1234)


print("'안녕하세요'라고 말했습니다.")		#따옴표를 서로 구분해서 따옴표 출력 가능
print('"안녕하세요"라고 말했습니다.')
print("\'배고파\'ㅁㄴㅇㄹ")				#혹은 \를 사용해서 출려가능
print("\"배고파\"ㅁㄴㅇㄹ")

print("asfd"*3)

print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])

alp = "abcdefghijklmnopqrstuvwxyz"

print(alp[5:11])
print(alp[18:26])
print(alp[-1:-8])
print(len(alp))

a = 15
b = 8
print(a+b, a-b, a*b, a%b, a/b, a//b, a**b)

a = input("숫자를 입력하세요 : ")