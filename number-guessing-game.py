from random import #randint by importing this module we are able to generate a random number
import sys # the use of this module is to exit out of program when the player chooses not to play again


#This is the welcome message the user is going to see when starting the game
print('''
	* ==== Welcome to the Number Guessing Game === *

	''')  

#this functions starts the whole game
def startGame():
	randomNumber = randint(1, 10)   #this variable is used to generate the random number between 1 and 10
	tries = 0 #the starter counter for the amount of tries the user has taken
	while True:
		try:
			guess = input('Please guess a number between 1 and 10: ')   #this input asks the user to input the number between 1 and 10
			if guess == randomNumber: # for this statement if the user guesses correctly, it congratulates the user and ask to start over or not along with the amount of tries the user has taken
				print('You got it!')
				print('It took you {} tries'.format(tries))
				while True:
					answer = raw_input('Would you like to start again? [y]es/[n]o :  ').lower() #this asks the user if they would like to start over again by answering yes or no
					if answer == 'y':
						print('''
Your Current high score is {}
							'''.format(tries))
						startGame()
					elif answer == 'n':
						sys.exit('Thanks, Come play again soon!') #  by using the sys module we are able to exit the program when the user does not want to play again
					else:
						print('Please enter y for yes or n for no')
			#all these statements are for incorrect guesses, it prints if the user should go higher or lower or if the value enter is incorrect
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
		# these exceptions are for the values that are entered incorrectly and also prompt a system error, instead they get a friendly error that helps them in the right direction
		except NameError: 
			print('Please enter a valid number between 1 and 10, Thank You')
			tries += 1
			continue
		except SyntaxError:
			print('Please enter a valid number between 1 and 10, Thank You')
			tries += 1
			continue


#this statment starts when the program is running in the repl or terminal

if __name__ == '__main__':
	startGame()












