with open("proverbs.txt", "r") as file:
	dic = {"disits" : 0, "spaces" : 0, "alpha" : 0}
	for i in file:
		for k in range(len(i)):
			if i[k].isdigit() == True:
				dic["disits"] += 1
			elif i[k].isspace() == True:
				dic["spaces"] += 1
			elif i[k].isalpha() == True:
				dic["alpha"] += 1
	print(dic)