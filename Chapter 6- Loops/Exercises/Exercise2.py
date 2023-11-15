question_1 = "How old are you?"
question_2= "Enter 'quit' when you are finished. "

while True:
    age = input(question_1)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("free ticket!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")