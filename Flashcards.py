class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        
        # we will return a string
        return self.words+' ('+self.meaning+')'
    
flash = []
print("welcome to flashcard application")

# the following loop will be repeated until
# user stops to add the flashcards
while (True):
    word = input("enter the name you want to add in flashcard : ")
    meaning = input("enter the meaning of the word : ")
    
    flash.append(Flashcard(word, meaning))
    option = int(input("enter 0, if you want to add more flashcards otherwise enter 1 : "))
    
    if(option):
        break
    
# printing the flashcards
print("\n\nYour flashcards are : ")
for i in flash:
    print(">",i)