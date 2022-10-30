import random 

questions = [] #questions list

def getRandomElement(input_array): #func get and return random element
	array_len = len(input_array)
	randEl = random.randint(0, array_len) - 1 

	resylt = f"""

			{questions[randEl]}

			"""

	return resylt

def welcomeMessage(): # simple welcome message :3
	message = """ 
	____                 _                                    _   _       _   _ 
	|  _ \ __ _ _ __   __| | ___  _ __ ___     __ _ _   _  ___| |_(_) ___ | \ | |
	| |_) / _` | '_ \ / _` |/ _ \| '_ ` _ \   / _` | | | |/ _ \ __| |/ _ \|  \| |
	|  _ < (_| | | | | (_| | (_) | | | | | | | (_| | |_| |  __/ |_| | (_) | |\  |
	|_| \_\__,_|_| |_|\__,_|\___/|_| |_| |_|  \__, |\__,_|\___|\__|_|\___/|_| \_|
	                                             |_|                             
			"""
	print(message)

def main(): 
	i = True
	while i:
		count = input("quest or !q: ") #get question
		if count == "!q":
			i = False
		else:
			questions.append(count) #add question in questions list
			print(f"added {count}")
			count = ""
	print(getRandomElement(questions)) 

if __name__ == '__main__':
	try:
		welcomeMessage()
		main()
	except Exception as e:
		print(f"oh no... this Err0r => {e}")

	print("++quiting++")