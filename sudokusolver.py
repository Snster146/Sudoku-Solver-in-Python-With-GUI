from tkinter import*
from tkinter import messagebox

root=Tk()

root.title("Sudoku board solver")

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#row 1 
entry00=Entry(font=(100),width=1)
entry00.grid(row=0,column=0,padx=1,sticky=W)

entry01=Entry(font=(100),width=1)
entry01.grid(row=0,column=1,padx=1,sticky=W)

entry02=Entry(font=(100),width=1)
entry02.grid(row=0,column=2,padx=1,sticky=W)

entry03=Entry(font=(100),bg="black",width=1)
entry03.grid(row=0,column=3,padx=1,sticky=W)

entry04=Entry(font=(100),width=1)
entry04.grid(row=0,column=4,padx=1,sticky=W)

entry05=Entry(font=(100),width=1)
entry05.grid(row=0,column=5,padx=1,sticky=W)

entry06=Entry(font=(100),width=1)
entry06.grid(row=0,column=6,padx=1,sticky=W)

entry07=Entry(font=(100),bg="black",width=1)
entry07.grid(row=0,column=7,padx=1,sticky=W)

entry08=Entry(font=(100),width=1)
entry08.grid(row=0,column=8,padx=1,sticky=W)

entry09=Entry(font=(100),width=1)
entry09.grid(row=0,column=9,padx=1,sticky=W)

entry010=Entry(font=(100),width=1)
entry010.grid(row=0,column=10,padx=1,sticky=W)
 
  #row2

entry10=Entry(font=(100),width=1)
entry10.grid(row=3,column=0,padx=1,sticky=W)

entry11=Entry(font=(100),width=1)
entry11.grid(row=3,column=1,padx=1,sticky=W)

entry12=Entry(font=(100),width=1)
entry12.grid(row=3,column=2,padx=1,sticky=W)

entry13=Entry(font=(50),bg="black",width=1)
entry13.grid(row=3,column=3,padx=1,sticky=W)

entry14=Entry(font=(100),width=1)
entry14.grid(row=3,column=4,padx=1,sticky=W)

entry15=Entry(font=(100),width=1)
entry15.grid(row=3,column=5,padx=1,sticky=W)

entry16=Entry(font=(100),width=1)
entry16.grid(row=3,column=6,padx=1,sticky=W)

entry17=Entry(font=(100),bg="black",width=1)
entry17.grid(row=3,column=7,padx=1,sticky=W)

entry18=Entry(font=(100),width=1)
entry18.grid(row=3,column=8,padx=1,sticky=W)

entry19=Entry(font=(100),width=1)
entry19.grid(row=3,column=9,padx=1,sticky=W)

entry110=Entry(font=(100),width=1)
entry110.grid(row=3,column=10,padx=1,sticky=W)

  #row 3

entry20=Entry(font=(100),width=1)
entry20.grid(row=4,column=0,padx=1,sticky=W)

entry21=Entry(font=(100),width=1)
entry21.grid(row=4,column=1,padx=1,sticky=W)

entry22=Entry(font=(100),width=1)
entry22.grid(row=4,column=2,padx=1,sticky=W)

entry23=Entry(font=(50),bg="black",width=1)
entry23.grid(row=4,column=3,padx=1,sticky=W)

entry24=Entry(font=(100),width=1)
entry24.grid(row=4,column=4,padx=1,sticky=W)

entry25=Entry(font=(100),width=1)
entry25.grid(row=4,column=5,padx=1,sticky=W)

entry26=Entry(font=(100),width=1)
entry26.grid(row=4,column=6,padx=1,sticky=W)

entry27=Entry(font=(100),bg="black",width=1)
entry27.grid(row=4,column=7,padx=1,sticky=W)

entry28=Entry(font=(100),width=1)
entry28.grid(row=4,column=8,padx=1,sticky=W)

entry29=Entry(font=(100),width=1)
entry29.grid(row=4,column=9,padx=1,sticky=W)

entry210=Entry(font=(100),width=1)
entry210.grid(row=4,column=10,padx=1,sticky=W)

  #border 1 

   # border 1 
border10=Entry(font=(100),width=1,bg="black")
border10.grid(row=5,column=0,padx=1,sticky=W)

border11=Entry(font=(100),width=1,bg="black")
border11.grid(row=5,column=1,padx=1,sticky=W)

border12=Entry(font=(100),width=1,bg="black")
border12.grid(row=5,column=2,padx=1,sticky=W)

border13=Entry(font=(100),width=1,bg="black")
border13.grid(row=5,column=3,padx=1,sticky=W)

border14=Entry(font=(100),width=1,bg="black")
border14.grid(row=5,column=4,padx=1,sticky=W)

border15=Entry(font=(100),width=1,bg="black")
border15.grid(row=5,column=5,padx=1,sticky=W)

border16=Entry(font=(100),width=1,bg="black")
border16.grid(row=5,column=6,padx=1,sticky=W)

border17=Entry(font=(100),width=1,bg="black")
border17.grid(row=5,column=7,padx=1,sticky=W)

border18=Entry(font=(100),width=1,bg="black")
border18.grid(row=5,column=8,padx=1,sticky=W)

border19=Entry(font=(100),width=1,bg="black")
border19.grid(row=5,column=9,padx=1,sticky=W)

border110=Entry(font=(100),width=1,bg="black")
border110.grid(row=5,column=10,padx=1,sticky=W)

  #row 4 
entry30=Entry(font=(100),width=1)
entry30.grid(row=6,column=0,padx=1,sticky=W)

entry31=Entry(font=(100),width=1)
entry31.grid(row=6,column=1,padx=1,sticky=W)

entry32=Entry(font=(100),width=1)
entry32.grid(row=6,column=2,padx=1,sticky=W)

entry33=Entry(font=(100),bg="black",width=1)
entry33.grid(row=6,column=3,padx=1,sticky=W)

entry34=Entry(font=(100),width=1)
entry34.grid(row=6,column=4,padx=1,sticky=W)

entry35=Entry(font=(100),width=1)
entry35.grid(row=6,column=5,padx=1,sticky=W)

entry36=Entry(font=(100),width=1)
entry36.grid(row=6,column=6,padx=1,sticky=W)

entry37=Entry(font=(100),bg="black",width=1)
entry37.grid(row=6,column=7,padx=1,sticky=W)

entry38=Entry(font=(100),width=1)
entry38.grid(row=6,column=8,padx=1,sticky=W)

entry39=Entry(font=(100),width=1)
entry39.grid(row=6,column=9,padx=1,sticky=W)

entry310=Entry(font=(100),width=1)
entry310.grid(row=6,column=10,padx=1,sticky=W)
 
  #row5

entry40=Entry(font=(100),width=1)
entry40.grid(row=7,column=0,padx=1,sticky=W)

entry41=Entry(font=(100),width=1)
entry41.grid(row=7,column=1,padx=1,sticky=W)

entry42=Entry(font=(100),width=1)
entry42.grid(row=7,column=2,padx=1,sticky=W)

entry43=Entry(font=(50),bg="black",width=1)
entry43.grid(row=7,column=3,padx=1,sticky=W)

entry44=Entry(font=(100),width=1)
entry44.grid(row=7,column=4,padx=1,sticky=W)

entry45=Entry(font=(100),width=1)
entry45.grid(row=7,column=5,padx=1,sticky=W)

entry46=Entry(font=(100),width=1)
entry46.grid(row=7,column=6,padx=1,sticky=W)

entry47=Entry(font=(100),bg="black",width=1)
entry47.grid(row=7,column=7,padx=1,sticky=W)

entry48=Entry(font=(100),width=1)
entry48.grid(row=7,column=8,padx=1,sticky=W)

entry49=Entry(font=(100),width=1)
entry49.grid(row=7,column=9,padx=1,sticky=W)

entry410=Entry(font=(100),width=1)
entry410.grid(row=7,column=10,padx=1,sticky=W)

  #row 6

entry50=Entry(font=(100),width=1)
entry50.grid(row=8,column=0,padx=1,sticky=W)

entry51=Entry(font=(100),width=1)
entry51.grid(row=8,column=1,padx=1,sticky=W)

entry52=Entry(font=(100),width=1)
entry52.grid(row=8,column=2,padx=1,sticky=W)

entry53=Entry(font=(50),bg="black",width=1)
entry53.grid(row=8,column=3,padx=1,sticky=W)

entry54=Entry(font=(100),width=1)
entry54.grid(row=8,column=4,padx=1,sticky=W)

entry55=Entry(font=(100),width=1)
entry55.grid(row=8,column=5,padx=1,sticky=W)

entry56=Entry(font=(100),width=1)
entry56.grid(row=8,column=6,padx=1,sticky=W)

entry57=Entry(font=(100),bg="black",width=1)
entry57.grid(row=8,column=7,padx=1,sticky=W)

entry58=Entry(font=(100),width=1)
entry58.grid(row=8,column=8,padx=1,sticky=W)

entry59=Entry(font=(100),width=1)
entry59.grid(row=8,column=9,padx=1,sticky=W)

entry510=Entry(font=(100),width=1)
entry510.grid(row=8,column=10,padx=1,sticky=W)

     # border 2 
border20=Entry(font=(100),width=1,bg="black")
border20.grid(row=9,column=0,padx=1,sticky=W)

border21=Entry(font=(100),width=1,bg="black")
border21.grid(row=9,column=1,padx=1,sticky=W)

border22=Entry(font=(100),width=1,bg="black")
border22.grid(row=9,column=2,padx=1,sticky=W)

border23=Entry(font=(100),width=1,bg="black")
border23.grid(row=9,column=3,padx=1,sticky=W)

border24=Entry(font=(100),width=1,bg="black")
border24.grid(row=9,column=4,padx=1,sticky=W)

border25=Entry(font=(100),width=1,bg="black")
border25.grid(row=9,column=5,padx=1,sticky=W)

border26=Entry(font=(100),width=1,bg="black")
border26.grid(row=9,column=6,padx=1,sticky=W)

border27=Entry(font=(100),width=1,bg="black")
border27.grid(row=9,column=7,padx=1,sticky=W)

border28=Entry(font=(100),width=1,bg="black")
border28.grid(row=9,column=8,padx=1,sticky=W)

border29=Entry(font=(100),width=1,bg="black")
border29.grid(row=9,column=9,padx=1,sticky=W)

border210=Entry(font=(100),width=1,bg="black")
border210.grid(row=9,column=10,padx=1,sticky=W)

   #row 7
entry60=Entry(font=(100),width=1)
entry60.grid(row=10,column=0,padx=1,sticky=W)

entry61=Entry(font=(100),width=1)
entry61.grid(row=10,column=1,padx=1,sticky=W)

entry62=Entry(font=(100),width=1)
entry62.grid(row=10,column=2,padx=1,sticky=W)

entry63=Entry(font=(100),bg="black",width=1)
entry63.grid(row=10,column=3,padx=1,sticky=W)

entry64=Entry(font=(100),width=1)
entry64.grid(row=10,column=4,padx=1,sticky=W)

entry65=Entry(font=(100),width=1)
entry65.grid(row=10,column=5,padx=1,sticky=W)

entry66=Entry(font=(100),width=1)
entry66.grid(row=10,column=6,padx=1,sticky=W)

entry67=Entry(font=(100),bg="black",width=1)
entry67.grid(row=10,column=7,padx=1,sticky=W)

entry68=Entry(font=(100),width=1)
entry68.grid(row=10,column=8,padx=1,sticky=W)

entry69=Entry(font=(100),width=1)
entry69.grid(row=10,column=9,padx=1,sticky=W)

entry610=Entry(font=(100),width=1)
entry610.grid(row=10,column=10,padx=1,sticky=W)
 
  #row 8

entry70=Entry(font=(100),width=1)
entry70.grid(row=11,column=0,padx=1,sticky=W)

entry71=Entry(font=(100),width=1)
entry71.grid(row=11,column=1,padx=1,sticky=W)

entry72=Entry(font=(100),width=1)
entry72.grid(row=11,column=2,padx=1,sticky=W)

entry73=Entry(font=(50),bg="black",width=1)
entry73.grid(row=11,column=3,padx=1,sticky=W)

entry74=Entry(font=(100),width=1)
entry74.grid(row=11,column=4,padx=1,sticky=W)

entry75=Entry(font=(100),width=1)
entry75.grid(row=11,column=5,padx=1,sticky=W)

entry76=Entry(font=(100),width=1)
entry76.grid(row=11,column=6,padx=1,sticky=W)

entry77=Entry(font=(100),bg="black",width=1)
entry77.grid(row=11,column=7,padx=1,sticky=W)

entry78=Entry(font=(100),width=1)
entry78.grid(row=11,column=8,padx=1,sticky=W)

entry79=Entry(font=(100),width=1)
entry79.grid(row=11,column=9,padx=1,sticky=W)

entry710=Entry(font=(100),width=1)
entry710.grid(row=11,column=10,padx=1,sticky=W)

  #row 9

entry80=Entry(font=(100),width=1)
entry80.grid(row=12,column=0,padx=1,sticky=W)

entry81=Entry(font=(100),width=1)
entry81.grid(row=12,column=1,padx=1,sticky=W)

entry82=Entry(font=(100),width=1)
entry82.grid(row=12,column=2,padx=1,sticky=W)

entry83=Entry(font=(50),bg="black",width=1)
entry83.grid(row=12,column=3,padx=1,sticky=W)

entry84=Entry(font=(100),width=1)
entry84.grid(row=12,column=4,padx=1,sticky=W)

entry85=Entry(font=(100),width=1)
entry85.grid(row=12,column=5,padx=1,sticky=W)

entry86=Entry(font=(100),width=1)
entry86.grid(row=12,column=6,padx=1,sticky=W)

entry87=Entry(font=(100),bg="black",width=1)
entry87.grid(row=12,column=7,padx=1,sticky=W)

entry88=Entry(font=(100),width=1)
entry88.grid(row=12,column=8,padx=1,sticky=W)

entry89=Entry(font=(100),width=1)
entry89.grid(row=12,column=9,padx=1,sticky=W)

entry810=Entry(font=(100),width=1)
entry810.grid(row=12,column=10,padx=1,sticky=W)


entries=[
    [entry00,entry01,entry02,entry04,entry05,entry06,entry08,entry09,entry010],
    [entry10,entry11,entry12,entry14,entry15,entry16,entry18,entry19,entry110],
    [entry20,entry21,entry22,entry24,entry25,entry26,entry28,entry29,entry210],
    [entry30,entry31,entry32,entry34,entry35,entry36,entry38,entry39,entry310],
    [entry40,entry41,entry42,entry44,entry45,entry46,entry48,entry49,entry410],
    [entry50,entry51,entry52,entry54,entry55,entry56,entry58,entry59,entry510],
    [entry60,entry61,entry62,entry64,entry65,entry66,entry68,entry69,entry610],
    [entry70,entry71,entry72,entry74,entry75,entry76,entry78,entry79,entry710],
    [entry80,entry81,entry82,entry84,entry85,entry86,entry88,entry89,entry810],


    ]
#add unsloved board to entry boxes 
for row in range(len(entries)):
    for col in range(len(entries[row])):
        if row < len(board) and col < len(board[row]):
            entries[row][col].insert(0, board[row][col])

sudokuLabel=Label(text="Sudoku Solver",font=("Century Gothic",21))
sudokuLabel.grid(row=13,column=11)

solveButton=Button(text="Solve",font=("Arial"),command=lambda : print_board(board,diplay=True))
solveButton.grid(row=14,column=11)
       




def print_board (bo,diplay=True):
  
  

  if diplay:
        for i in range(len(bo)):
            if i % 3 == 0 :
                print("-" * 19)
            for j in range(len(bo[0])):
                if j % 3 == 0 and j != 0:
                    print("|", end="")
                if j == 8:
                    print(bo[i][j])
                else:
                    print(bo[i][j], end=" ")

        #add unsloved board to entry boxes 
        for row in range(len(entries)):
            for col in range(len(entries[row])):
                if row < len(board) and col < len(board[row]):
                    entries[row][col].insert(0, board[row][col])
       



            


def is_valid_move(bo,row,col,num):
    
    #check if num being passed from find empty func is in the row
    if num in [bo[i][col] for i in range(9)]:
        return False
    #check if num being passed from find empty func is in the col
    elif num in [bo[row][i] for i in range(9)]:
               return False
    gridx =3*(row//3)
    gridy=3*(col//3)
    for i in range (gridx,gridx+3):
        for j in range(gridy,gridy +3):
            if num == bo[i][j]:
                return False
    else:
       return True
        
  #for i in range (0,9) , num =i
  #check if num is in row which num is in , if so return false 
  #check if num is in column which num is in , if so return false
  #check if num is in 3x3 square which num is in , if so return false
 


def find_empty(bo):
    for row in range(len(bo)):
        for col in range(len(bo[row])):
            if bo[row][col] == 0:
                for num in range(1, 10):  # Iterate through numbers 1 to 9
                    if is_valid_move(bo, row, col, num):
                        bo[row][col] = num
                        if find_empty(bo):
                            return True
                        bo[row][col] = 0
                return False
     
    return True 



print("unsolved board")

print ("Solved board")
find_empty(board)

root.mainloop()