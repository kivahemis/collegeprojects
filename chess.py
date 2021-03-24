def pass_checking(password):
    counter = 0
    specials = ['$', '@', '#', "$", "%", '^', '&', '*', ')', ')', '-', '_', '=', '+']

    if len(password) < 6:
        print("Your password should be stronger!")
        counter = counter - 1
    if len(password) > 8:
        counter = counter + 1
    if any(char.isdigit() for char in password):
        counter = counter + 1
    if any(char.isupper() for char in password):
        counter = counter + 1
    if any(char.islower() for char in password):
        counter = counter + 1
    if any(char in specials for char in password):
        counter = counter + 2

    print(counter)
    print("\n")

    print("Deegres of password: ")
    print("0 - very weak")
    print("1 - weak")
    print("2 - avrage")
    print("3 - above avrage")
    print("4 - strong")
    print("5 - very strong")


password = input('enter the password : ')
print(pass_checking(password))

