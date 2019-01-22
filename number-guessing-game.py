from random import randint
import sys

print('''
	* ==== Welcome to the Number Guessing Game === *

	''')


def startGame():
	randomNumber = randint(1, 10)
	tries = 0
	while True:
		try:
			guess = input('Please guess a number between 1 and 10: ')
			if guess == randomNumber:
				print('You got it!')
				print('It took you {} tries'.format(tries))
				answer = raw_input('Would you like to start again? [y]es/[n]o :  ')
				if answer.lower() == 'y' or 'yes':
					print('''Your Current high score is {}'''.format(tries))
					startGame()
				elif answer.lower() == 'n' or 'no':
					sys.exit('Thanks, Come play again soon!')
				else:
					print('Please enter y for yes or n for no')
			elif guess > 10:
				print('Please enter a valid number between 1 and 10, Thank You')
				tries += 1
				continue
			elif guess > randomNumber:
				print('It is Lower!')
				tries += 1
				continue
			elif guess < randomNumber:
				print('It is Higher!')
				tries += 1
				continue
		except NameError:
			print('Please enter a valid number between 1 and 10, Thank You')
			tries += 1
			continue
		except SyntaxError:
			print('Please enter a valid number between 1 and 10, Thank You')
			tries += 1
			continue









# def startOver():
# 	answer = raw_input('Would you like to start again? [y]es/[n]o :  ').lower()
# 	if answer == 'y' or 'yes':
# 		print('''Your Current high score is {}'''.format(tries))
# 		startGame()
# 	elif answer.lower() == 'n' or 'no':
# 		sys.exit('Thanks, Come play again soon!')
# 	else:
# 		print('Please enter y for yes or n for no')




if __name__ == '__main__':
	startGame()












