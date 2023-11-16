#hangman extension
import random
string = ""
with open('textfile.txt', 'r') as f:
    for i in f:
        string = string + i
    string = [x.strip() for x in string.split(",")]
print(string[random.randint(0,len(string))])
