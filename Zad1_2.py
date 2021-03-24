user_input = input("")
pl = ("ąęćśżźłóĄĘŻŹŚĆŁ")
basic = ("aecszzloAEZZSCL")
translator = str.maketrans(pl,basic)
print(user_input.translate(translator))


#zamiana liter w zdaniu wprowadzonym przez użytkownika