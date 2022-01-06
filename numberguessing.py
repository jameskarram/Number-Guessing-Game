import random
numberBank = list(range(101))
user_score = 0
#----------------------------------------------#
#INTRODUCTION TO THE GAME
print("Hello World")
print("Welcome to my number guessing game")
want_to_play = input("Would you like to play the number guessing game?")
want_to_play = want_to_play.lower()

if want_to_play == "yes": 
  know_how_to_play = input("Do you know how to play?")
  know_how_to_play = know_how_to_play.lower()
  if know_how_to_play == "yes":
    print("Beginning Game.\nEnjoy.\n")
    runUserCode = True
  elif know_how_to_play == "no":
    print("\nFirst the computer will select a random number between 1 and 100.\nYou will then be provided with a series of 3 hints to help you guess the number.\nYou will be given the opportunity to guess a number after each hint.\nIf you reach the final hint without guessing the correct answer you lose.\nLess points will be awarded depending on how many hints are used.\n\n*Warning* This game is extremely difficult and frustrating and relies heavily on luck.\nPlay at your own risk.\n")
    print("Beginning Game.\nEnjoy.\n")
    runUserCode = True
  else:
    print("Invalid Entry.")
    runUserCode = False
elif want_to_play == "no":
  print("Didn't want you to play anyways.")
  runUserCode = False
else:
  print("Invalid Entry.")
  runUserCode = False
#----------------------------------------------#
#SELECTION OF RANDOM NUMBER BY SYSTEM
def number_selection():
  random_number = random.choice(numberBank)
  return random_number
random_number = number_selection()
#----------------------------------------------#
#DEFINING POSSIBLE HINTS
def greater_than_50(random_number):
  if random_number > 50:
    print("The number is greater than 50.")
  else:
    print("The number is not greater than 50.")

def divisible_by_two(random_number):
  two_check = random_number / 2 
  if two_check == int(two_check):
    print("The number is an even number.")
  else:
    print("The number is an odd number.")

def divisible_by_three(random_number):
  three_check = random_number / 3
  if three_check == int(three_check):
    print("The number is divisible by 3.")
  else:
    print("The number is not divisible by 3.")

def divisible_by_five(random_number):
  five_check = random_number / 5
  if five_check == int(five_check):
    print("The number is divisible by 5.")
  else:
    print("The number is not divisible by 5.")

def ends_in_zero(random_number):
  if random_number % 10 == 0:
    print("The number ends with a 0.")
  else:
    print("The number doesn't end with a 0.")

def single_digit(random_number):
  if random_number < 10:
    print("The number is a single digit number.")
  else:
    print("The number is a double digit number.")
#----------------------------------------------#
while runUserCode:
  hint_list = [greater_than_50, divisible_by_two, divisible_by_three, divisible_by_five, ends_in_zero, single_digit]
  #--------------------------------------------#
  random_number = number_selection()
  print("A number has been selected!\n")
  #--------------------------------------------#
  #FUNCTION FOR RANDOMIZING HINTS
  def randomize_hints():
    first_hint = random.choice(hint_list)
    hint_list.remove(first_hint)
    second_hint = random.choice(hint_list)
    hint_list.remove(second_hint)
    third_hint = random.choice(hint_list)
    hint_list.remove(third_hint)
    return first_hint, second_hint, third_hint
  random_hints = randomize_hints()
  first_hint = random_hints[0]
  second_hint = random_hints[1]
  third_hint = random_hints[2]
  #--------------------------------------------#
  #FIRST HINT AND QUESTION
  print(f"Your first hint is...")
  first_hint = first_hint(random_number)
  first_guess = input("What is your first guess.\n3 points will be awarded for the correct answer.\n")
  first_guess = int(first_guess)
  if first_guess == random_number:
    print("WOW, You guessed the correct number on your first try!\nCongratulations, you will be awarded 3 points!")
    user_score = user_score + 3
    play_again = input("Would you like to play another round?")
    play_again = play_again.lower()
    if play_again == "yes":
      print("\nA new number will be randomly chosen.")
      continue
    elif play_again == "no":
      print(f"Your final score is {user_score}.\nThank you for playing.")
      runUserCode = False
    else:
      print("Invalid Entry.")
      print(f"Your final score is {user_score}.\nThank you for playing.")
      runUserCode = False
  else:
    print("You did not guess the correct number.\n \nGenerating the second hint.")
    #--------------------------------------------#
    #SECOND HINT AND QUESTION
    print(f"Your second hint is...")
    second_hint = second_hint(random_number)
    second_guess = input("What is your first guess.\n2 points will be awarded for the correct answer.\n")
    second_guess = int(second_guess)
    if second_guess == random_number:
      print("Congratulations! You guessed the correct number after the second hint!\nYou've earned 2 points!")
      user_score = user_score + 2
      play_again = input("Would you like to play another round?")
      play_again = play_again.lower()
      if play_again == "yes":
        print("\nA new number will be randomly chosen.")
        continue
      elif play_again == "no":
        print(f"Your final score is {user_score}.\nThank you for playing.")
        runUserCode = False
      else:
        print("Invalid Entry.")
        print(f"Your final score is {user_score}.\nThank you for playing.")
        runUserCode = False
    else:
      print("You did not guess the correct number.\n \nGenerating the your third and final hint.")
      #--------------------------------------------#
      #THIRD HINT AND QUESTION
      print(f"Your final hint is...")
      third_hint = third_hint(random_number)
      final_guess = input("What is your final guess.\n1 point will be awarded for the correct answer.\n")
      final_guess = int(final_guess)
      if final_guess == random_number:
        print("Congrats! You guessed the correct answer with your final guess!\n1 point will be awarded.")
        user_score = user_score + 1
        play_again = input("Would you like to play another round?")
        play_again = play_again.lower()
        if play_again == "yes":
          print("\nA new number will be randomly chosen.")
          continue
        elif play_again == "no":
          print(f"Your final score is {user_score}.\nThank you for playing.")
          runUserCode = False
        else:
          print("Invalid Entry.")
          print(f"Your final score is {user_score}.\nThank you for playing.")
          runUserCode = False
      else:
        print(f"I'm sorry, you did not guess the correct number.\nThe correct number was {random_number}.\nNo points were awarded for this round.")
        play_again = input("Would you like to play another round?")
        play_again = play_again.lower()
        if play_again == "yes":
          print("A new number will be randomly chosen.")
          continue
        elif play_again == "no":
          print(f"Your final score is {user_score}.\nThank you for playing.")
          runUserCode = False
        else:
          print("Invalid Entry.")
          print(f"Your final score is {user_score}.\nThank you for playing.")
          runUserCode = False
