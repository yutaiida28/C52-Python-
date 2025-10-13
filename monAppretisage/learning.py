import random


# 1.1  
'''

end = False
mistery_number = random.randrange(0,100)
TRY = 5
life = TRY
while not end:
    if life >= 0:
        result = input("try to guess the mistery number thats in between 1 to 100 you got " + str(life) + " life try to guess : ")
        if result.isdigit():
            number = int(result)
            if number == mistery_number:
                print("waw you got it")
                end = True
            else:
                if number < mistery_number:
                    print("the mistery number is bigger... you lost 1 life ")
                else:
                    print("the mistery number is smaller... you lost 1 life ")
                life = life - 1
    else:
        print("you lost hahahaha")
        end = True

'''