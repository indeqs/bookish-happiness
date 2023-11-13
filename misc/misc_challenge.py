#! /usr/bin/python3

def readflag():
	try:
		with open('./flag.txt','r') as r:
			flag=r.read()
			r.close()
	except Exception as error:
		print(f"Could not read flag file.Error {error}. Create a flag.txt file locally.")
		exit(-1)
	return flag


while (1):
	print("\n\n\n")
	print("                                  ****  Welcome to the hacker Interview. ***")
	print("I was told you are good with computers, let's see how good you really are. This should be a simple challenge for you\n\n")

	string1=str(input("Enter the first string: "))
	string2=str(input("Enter the second string: "))

	string1=string1.lower().strip() 
	string2=string2.lower().strip() 

	if string1 == string2:
		print("\nYou can't even play by the rules. The strings should be different !!!")
		continue

	if (string1.upper().strip() == string2.upper().strip()):
		flag=readflag()
		print(f"\nFine, fine, You are good as they claim. Here is the flag {flag}")
		exit(0)
	else:
		print("\nJust like i thought, you are an imposter")
