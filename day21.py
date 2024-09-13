print("Maths Game")
print()
print("Ready, set, Math! Pick a number, and then answer 10 questions to see how many you can get right.")
print()
number = int(input("Name your multiples: "))
print()
counter = 0
for i in range(1,11):
  print(i, "x", number, "=")
  answer = int(input(""))
  if answer == i*number:
    print("Great work!🥳")
    counter +=1
  elif answer != i*number:
    print("Nope!🙁 The answer was", i*number)
  elif answer < 0:
    print("You can't go below 0")
    exit()
  else:
    print("That's not a number")
    exit()
print("Thank you for playing! You got", counter, "out of 10 correct.")