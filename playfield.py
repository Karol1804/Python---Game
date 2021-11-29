playfield = [["_" ,"_","_"],["_" ,"_","_"],["_" ,"_","_"]]
def print_playfield(rows,columns):
    print(" ",0,1,2," ","x")
    for row in range (0,rows):
        print(row ,end=" ")
        for column in range (0,columns):
            print(playfield[row][column] ,end=" " )
        print()
    print()
    print("y")    
print_playfield(3,3)