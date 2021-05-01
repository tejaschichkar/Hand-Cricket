import random as r

toss = r.randint(1, 2)

def bat():

	pn = True	ps = 0

	while(pn):

		n2 = (6,5,4,3,2,1)

		user = int(input("Choose any num from 1 to 6\n"))

		if user > 6 or user < 1:

			print("Please enter a number from 1 to 6 only")

			continue

		comp = r.choice(n2)

		print(comp)

		if user != comp:

			ps = ps + user

			print("Your score :"+str(ps))

		elif user == comp:

			print("You're out")

			print("!!!!!!!!Your total score is!!!!!!!!! :",ps)

			print("Now it's computer's turn for batting\nNow you'll do bowling")

			cn = True

			cs = 0

			while(cn):

				user = int(input("any num from 1 to 6\n"))

				if user > 6 or user < 1:

					print("Please enter a number from 1 to 6 only")

					continue

				comp = r.choice(n2)

				print(comp)

				if user != comp:

					cs = cs + comp

					print("Computer's score :"+str(cs))

				elif user == comp:

					print("Computer is out !")

					print("!!!!!!!!Computer's total score is!!!!!!!!! :",cs)

					

					if ps > cs:

						print("Congratulations!!! \nYou've won the match")

					elif ps < cs:

						print("Better luck next time : ) \nYou've lost the match")

					return cs

					return ps

					cn=False

					pn= False

def bowl():

	cn = True

	cs = 0

	while(cn):

		n2 = (6,5,4,3,2,1)

		user = int(input("any num from 1 to 6\n"))

		if user > 6 or user < 1:

			print("Please enter a number from 1 to 6 only")

			continue

		comp = r.choice(n2)

		print(comp)

		if user != comp:

			cs = cs + comp

			print("Computer's score :"+str(cs))

		elif user == comp:

			print("Computer is out !")

			print("!!!!!!!!Computer's' total score is!!!!!!!!! :",cs)

			print("Computer is out !!! Now its your turn for batting")

			pn = True

			ps = 0

			while(pn):

				user = int(input("any num from 1 to 6\n"))

				if user > 6 or user < 1:

					print("Please enter a number from 1 to 6 only")

					continue

				comp = r.choice(n2)

				print(comp)

				if user != comp:

					ps = ps + comp

					print("Your score :"+str(ps))

				elif user == comp:

					print("You are out !")

					print("!!!!!!!!Your total score is!!!!!!!!! :",ps)

					

					if ps > cs:

						print("Congratulations!!! \nYou've won the match")

					elif ps < cs:

						print("Better luck next time : ) \nYou've lost the match")

					return cs

					return ps

					cn=False

					pn= False

if toss == 1:

	print('You have won toss and You will bat first')

	bat()

elif toss == 2:

	print("Computer has won the toss and you will bowl first")

	bowl()
