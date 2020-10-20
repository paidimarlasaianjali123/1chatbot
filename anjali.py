import random
def remainder(a):
  if (a>=6 and a<=9):
       return s
  elif(a>=11 and a<=13):
        return p
  elif(a>16 and a<=18):
        return n
  elif(a>=21 and a<=23):
        return c
  else:
        return d
s="it's time to breakfast"
p="it's time to lunch "
n="it's time to snacks"
c="it's time to dinner"
d="I don't understand"
def greet():
	l=["Hi i am a chat bot created by Anjali to help you to set your remainders"]
	print(random.choices(l))
def show_menu():
    print("1.time table")
    print("2.end chat")
    print("---------")
    try:
        return int(input("enter your choice [1-3]: "))
    except:
        print("only enter choice 1,2 and 3")
        return 0

def bot():
    greet()
    s=input("your name: ")
    choice =show_menu()
    while choice != 2:
        if choice == 1:
           a=int(input("enter the time in 24 hours format\n"))
           print(remainder(a))
        
        else:
            print("i dont understand that")
        choice = show_menu() 

bot()