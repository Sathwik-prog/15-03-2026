import random

class FruitQuiz:
    def __init__(self):
        self.fruits = {
            "apple": "red",
            "banana": "yellow",
            "grape": "purple",
            "orange": "orange",
            "watermelon": "green",
            "mango": "yellow"
        }

    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the color of", fruit)

            user_answer = input("Your answer: ")

            if user_answer.lower() == color:
                print("Correct answer")
            else:
                print("Wrong answer")

            option = int(input("Enter 1 to stop or 0 to continue: "))
            if option == 1:
                break

print("Welcome to fruit quiz")

fq = FruitQuiz()
fq.quiz()