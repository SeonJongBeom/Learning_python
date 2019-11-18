#####
##얕은 복사
#LIST_A = [1,2,3,4,5]
#LIST_B = LIST_A #이렇게 복사하면 두 리스트는 같은 메모리 공간을 공유하게됨(C에서의 배열도 마찬가지)
#				#다라서 LIST_B의 값이 바뀌면 LIST_A의 값도 바뀜!

##깊은 복사
#LIST_A = [1,2,3,4,5]
#LIST_B = LIST(LIST_A) #이렇게 넣으면 두 리스트는 서로다른 메모리 공간을 공유하게됨
#					  #따라서 LIST_B의 값이 바뀌어도 LIST_A의 값은 바뀌지 않음!

##리스트는 참조에 의한 호출임

#####
##값을 반환하는 함수
#def get_sum(start, end):
#	sum = 0
#	for i in range(start, end+1):
#		sum += i
#	return sum

#value = get_sum(1, 10)
#print(value)
##함수는 무조건 위에 다 선언해야됨 인터프리터 언어라!

####
#가변 인수
def asterisk_test(a,b, *c):
	return a + b + sum(c)

print(asterisk_test(1,2,3,4,5,6,7,8,9,4,5,6,8,1,2,5,6,8,7,6,2,1,5,6,5,1))