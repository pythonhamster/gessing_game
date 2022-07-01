import random
countries = ["china", "us", "canada", "mexico", "brazil", "greenland", "iceland", "ecuador", "malawi", "italy", "ukraine"]

with open("countries.txt", "w") as f:
    string = "\n".join(countries)
    f.write(string)


def load(filename):
    with open(filename,"r") as f:
        contents = f.read()
        countries = contents.split("\n")
        return countries


load("countries.txt")
country = random.choice(countries)
present_list = ["_"] * len(country)
while True:
    print(*present_list)
    guess = input("please guess a letter\n>>>: ")
    if len(guess) == 1:
        if guess.isalpha():
            if guess in country:
                for i in country:
                    if i == guess:
                        index = country.find(guess)
                        present_list[index] = guess
                        country = country.replace(i, "!", 1)
            elif guess in present_list:
                print("you have already guessed this letter, try again.")
            else:
                print("wrong guess")
        else:
            print("letters only!")
    else:
        print("you have entered to many letters")
    if "_" not in present_list:
        win = "".join(present_list)
        print(f"YAY!!! {win.upper()} You won the game!!")
        break