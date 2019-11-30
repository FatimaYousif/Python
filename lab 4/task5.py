#task5
my_num=5
for i in range(1,4):
    guess_num=int(input("guess a number="))
    if(guess_num==my_num):
        print("YOU GUESSED THE RIGHT NUMBER")
        break;
    elif(guess_num<my_num):
        print("the number is greater than "+str(guess_num))
    elif(guess_num>my_num):
        print("the number is less than "+str(guess_num))
    