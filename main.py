print("Math Game!")
print()
multiple = int(input("Name your multiple: "))
score = 0

for i in range(1, 11):
  correct_answer = i * multiple
  print(i, "x", multiple,)
  answer = int(input("> "))
  if answer == correct_answer:
    print("Great job!")
    print()
    score += 1
  else:
    print(f"Sorry, that's not correct. The answer is {correct_answer}.")
    print()
    
if score == 10:
  print("Great job! You got a perfect score! 🥇")
else:
  print(f"You only scored {score} points out of 10. Time to practice!")