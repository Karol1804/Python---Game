import sys
from playfield import print_playfield,playfield


entered_chatracter_player=["x" ,"o"]
player1 = "End of game,Player1 has won !!!"
player2 = "End of game,Player2 has won !!!"

y = True
while  y == True :
    player = 1
    while player == 1 or player == 2:

        print("On the move is Player" + str(player))

        #Enttering coordinate X
        def get_input1():
            print("Enter the X-axis coordinate (0,1,2)")
            while True:
                try:
                    number=int(sys.stdin.readline())
                except Exception:
                    print("Eror!!! Please insert integer value (0,1,2")
                    continue
    
                if number>2 and number<0 :
                    print(" Eror!!! You are entered a number out of range (0,1,2)")
                    continue
                break

            return number
        entered_number_X = get_input1()

        def get_input2():
            print("Enter the Y-axis coordinate (0,1,2)")
            while True:
                try:
                    number=int(sys.stdin.readline())
                except Exception:
                    print("Eror!!! Please insert integer value (0,1,2")
                    continue
    
                if number>2 and number<0 :
                    print(" Eror!!! You are entered a number out of range (0,1,2)")
                    continue
                break

            return number
        entered_number_Y = get_input2()
    
        

        #Control of entered coordinate,free playing field
        while playfield[entered_number_Y][entered_number_X] == "_" :
            if player == 1:
                playfield[entered_number_Y][entered_number_X] = entered_chatracter_player[0]
                print_playfield(3,3)
                player = 2
                break
                
            if player == 2 :
                playfield[entered_number_Y][entered_number_X] = entered_chatracter_player[1]
                print_playfield(3,3)
                player = 1
                break
    
        else :
            print("Error!!! There is alredy a character on the specified coordinates(x or o),please enter other coordinates")
            continue

        #Control playfield rows,columns diagonally
        rows = 3
        columns = 3
        x = 1
        #Rows
        for row in range(0,rows):
            if playfield[row][0] == entered_chatracter_player[0] and playfield[row][1] == entered_chatracter_player[0] and playfield[row][2] == entered_chatracter_player[0]  :
                print(player1)
                x = 0
            if playfield[row][0] == entered_chatracter_player[1] and playfield[row][1] == entered_chatracter_player[1] and playfield[row][2] == entered_chatracter_player[1]  :
                print(player2)
                x = 0
                
        #Columns
        for column in range(0,columns):
            if playfield[0][column] == entered_chatracter_player[0] and playfield[1][column] == entered_chatracter_player[0]  and playfield[2][column] == entered_chatracter_player[0]  :
                print(player1)
                x = 0
            if playfield[0][column] == entered_chatracter_player[1] and playfield[1][column] == entered_chatracter_player[1]  and playfield[2][column] == entered_chatracter_player[1]  :
                print(player2)
                x = 0

        
        #Diagonally
        if playfield[2][0] == entered_chatracter_player[0]: 
            if playfield[1][1] == entered_chatracter_player[0]:
                if playfield[0][2] == entered_chatracter_player[0] : 
                    print(player1)
                    x = 0
        
        if playfield[2][0] == entered_chatracter_player[1]:
            if playfield[1][1] == entered_chatracter_player[1]:
                if playfield[0][2] == entered_chatracter_player[1] : 
                    print(player2)
                    x = 0

            
            
        if playfield[2][2] == entered_chatracter_player[0] :
            if playfield[1][1] == entered_chatracter_player[0] :
                if playfield[0][0] == entered_chatracter_player[0] :
                    print(player1)
                    x = 0
        
        if playfield[2][2] == entered_chatracter_player[1] :
            if playfield[1][1] == entered_chatracter_player[1] :
                if playfield[0][0] == entered_chatracter_player[1] :
                    print(player2)
                    x = 0
        
        if x == 0 :
            y = False
            break
        
        #Playfiled control, free shelf
        arr = []
        for row in range(0,rows):
            for column in range(0,columns):
                arr.append(playfield[row][column])
        fields = arr.count("_")
        if fields <= 0 :
            print("End of game.Draw !!!")
            x = 0
        
                    
        if x == 0 :
            y = False
            break
            
            

        