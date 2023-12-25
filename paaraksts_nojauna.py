from random import randint, shuffle
from time import sleep
class create:
    
    def __init__(self):
        self.copyGrid = []
        self.counter = 0
        self.grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def checkGrid(self):
        for row in range(0,9):
            for col in range(0,9):
                if self.grid[row][col]==0:
                    return False
        return True                 #We have a complete grid!  
    def solveGrid(self):
        self.counter = 1
        
        for i in range(0,81):       #Find next empty cell
            row=i//9
            col=i%9
            if self.grid[row][col]==0:
                for value in range (1,10):

                    if not(value in self.grid[row]):             #Check that this value has not already be used on this row
                    
                        if not value in (self.grid[0][col],self.grid[1][col],self.grid[2][col],self.grid[3][col],self.grid[4][col],self.grid[5][col],self.grid[6][col],self.grid[7][col],self.grid[8][col]):     #Check that this value has not already be used on this column
                            #Identify which of the 9 squares we are working on
                            square=[]
                            if row<3:
                                if col<3:
                                    square=[self.grid[i][0:3] for i in range(0,3)]
                                elif col<6:
                                    square=[self.grid[i][3:6] for i in range(0,3)]
                                else:  
                                    square=[self.grid[i][6:9] for i in range(0,3)]
                            elif row<6:
                                if col<3:
                                    square=[self.grid[i][0:3] for i in range(3,6)]
                                elif col<6:
                                    square=[self.grid[i][3:6] for i in range(3,6)]
                                else:  
                                    square=[self.grid[i][6:9] for i in range(3,6)]
                            else:
                                if col<3:
                                    square=[self.grid[i][0:3] for i in range(6,9)]
                                elif col<6:
                                    square=[self.grid[i][3:6] for i in range(6,9)]
                                else:  
                                    square=[self.grid[i][6:9] for i in range(6,9)]
                            
                            if not value in (square[0] + square[1] + square[2]):    #Check that this value has not already be used on this 3x3 square
                                self.grid[row][col]=value
                                if self.checkGrid():
                                    self.counter+=1
                                    break
                                else:
                                    if self.solveGrid():
                                        return True
                break
        self.grid[row][col]=0
    
    def fillGrid(self):
        numberList=[1,2,3,4,5,6,7,8,9]
        for i in range(0,81):
            row=i//9
            col=i%9
            if self.grid[row][col]==0:
                shuffle(numberList)      
                for value in numberList:
                    if not(value in self.grid[row]):
                        if not value in (self.grid[0][col],self.grid[1][col],self.grid[2][col],self.grid[3][col],self.grid[4][col],self.grid[5][col],self.grid[6][col],self.grid[7][col],self.grid[8][col]):
                            square=[]
                            if row<3:
                                if col<3:
                                    square=[self.grid[i][0:3] for i in range(0,3)]
                                elif col<6:
                                    square=[self.grid[i][3:6] for i in range(0,3)]
                                else:  
                                    square=[self.grid[i][6:9] for i in range(0,3)]
                            elif row<6:
                                if col<3:
                                    square=[self.grid[i][0:3] for i in range(3,6)]
                                elif col<6:
                                    square=[self.grid[i][3:6] for i in range(3,6)]
                                else:  
                                    square=[self.grid[i][6:9] for i in range(3,6)]
                            else:
                                if col<3:
                                    square=[self.grid[i][0:3] for i in range(6,9)]
                                elif col<6:
                                    square=[self.grid[i][3:6] for i in range(6,9)]
                                else:  
                                    square=[self.grid[i][6:9] for i in range(6,9)]
                            if not value in (square[0] + square[1] + square[2]):
                                self.grid[row][col]=value
                                if self.checkGrid():
                                    return True
                                else:
                                    if self.fillGrid():
                                        return True
                break
        self.grid[row][col]=0
    
    def generate(self):
        self.fillGrid()
        for _ in range(40):
            row = randint(0,8)
            col = randint(0,8)
            while self.grid[row][col]==0:
                row = randint(0,8)
                col = randint(0,8)
            self.grid[row][col] = 0
        return self.grid

x = create()
