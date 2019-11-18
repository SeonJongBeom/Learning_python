####
#p.158 2번
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
	if number >= 100:
		print("- 100 이상의 수:", number)

####
#p.158 3번
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for i in numbers:
	if i % 2 == 0:
		print(i, "는 짝수입니다.")
	else:
		print(i, "는 홀수입니다.")
count = 0
for i in numbers:
	print(i,"는", len(str(i)), "자리수 입니다.")

####
#9.159 4번
list_of_list = [[1,2,3], [4,5,6,7], [8,9]]
for i in list_of_list:
	for j in i:
		print(j)

####
#9.159 5번
numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]
for number in numbers:
	output[(number+2)%3].append(number)

print(output)

####
#p.188 3번
limit = 10000
i = 1
sum_value = 0
while sum_value <= limit:
	sum_value += i
	i += 1
print("{}를 더할 때 {}를 넘으며 그때의 값은 {}입니다.".format(i, limit, sum_value))

####
#p.189 4번
max_value = 0
a = 0
b = 0

for i in range(1,100):
	j = 100 - i
	if i * j > max_value:
		max_value = i * j
		a = i
		b = j

print("최대가 되는 경우: {} * {} = {}".format(a,b,max_value))