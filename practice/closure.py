#closer is function having access to scope of this its parent
#function after the parent function has returned



def parent_function(person, coins):
    #coins = 3
    
    def play_game():
        nonlocal coins
        coins -= 1
        
        if coins > 1:
            print("\n"+ person + " has " + str(coins) + " coinsleft.")
        elif coins == 1:
             print("\n"+ person + " has " + str(coins) + " coinsleft.")
        else:
             print("\n"+ person + "is out of coins.")
    return play_game

tommy = parent_function("Tommy", 8)
jenney = parent_function("Jenney", 5)

tommy()
jenney()

tommy()

tommy()
jenney()



def mom(milk,tea):
    
    def child():
        nonlocal tea
        tea -=1
        
        if tea > 1:
           print("\n"+ milk + " be " + str(tea) + " jamag")
        elif tea == 1:
           print("\n"+ milk + " be " + str(tea) + " jamag")
        else:
            print("\n" + milk + " out of the child")
            
    return child

khan = mom("usman", 3)  
jjag = mom("jage", 3) 


khan() 
jjag()

khan() 
jjag()
khan() 
jjag()


def A(a,b):
    def B():
        nonlocal b
        
        b +=1
        if b > 10:
            print("\n" + a + str(b) + " win")
        elif b == 1:
             print("\n" + a + str(b) + " tie")
        else:
            print("\n" + a + " you lose")
        
    return B
    
AA = A("khalid ", 3) 
BB = A("khalidu ", 3) 

AA()
BB()
AA()
BB()
AA()
BB()
AA()
BB()
AA()
BB()
AA()
BB()
AA()
BB()
AA()
BB()
            