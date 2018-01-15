def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("That's not a integer! Try again.")
            continue
            print("Test")
        else:
            return userInput
            break
age = inputNumber("How old are you?")
print(age)
