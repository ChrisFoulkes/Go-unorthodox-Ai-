import json



class board: 
        def __init__ (self, move):
                
                self.rows = []
                self.move = "move no. " + str(move) 
          

                for y in range(19):
                        self.rows.append([]) 

                for i in self.rows:
                        for y in range(19):
                                i.append(0.0)
                        

                        
        def incrementposition(self, position):

                pos1 = position[0]-1
                pos2 = position[1]-1
                if pos1 < 19 and pos2 < 19 :
                        value = self.rows[pos1]
                        value[pos2] = value[pos2] + 1
                        self.rows[pos1] = value
        
        def outputmoves(self, filepath):
                outputfile = open(filepath, "a+")
                outputfile.write(self.move + "\n")
                outputfile.write("{ \n")
                for i in range(len(self.rows)):
                        outputfile.write(str(self.rows[i]) + "\n")
                       
                outputfile.write("} \n")
                outputfile.close()
        def loadmoves (self, movelist):
                self.rows = []   
                for y in range(19):
                         self.rows.append(movelist[y]) 
                        
        


#generate the moves board position list
moves = []
for i in range (411):
        moves.append(board(i+1))
#---

print "loading values!"


"""
for files in range(5673, 9981):
        f = open("sgf/val/0000" + str(files)  + ".sgf", "r")
        f= f.read()
        split_f = f.split(";")
        promoves = []

        for i in range (2, len(split_f)):
            x = split_f[i]
            y = x[x.find("[")+1:x.find("]")]
            y =  [ord(x)%32 for x in y]  
            promoves.append(y)

        for i in range (len(promoves)):     
            moves[i].incrementposition(promoves[i])
            




"""
#example boardposition output
        
#open('boardpositions.txt', 'w').close()

#moves[0].outputmoves("boardpositions.txt")
#moves[1].outputmoves("boardpositions.txt")

#-----


#loading boardpositions from text file
def loadboardpositions():        
        boards = open('boardpositions.txt', 'r')
        positions = False
        move = 0
        loadmove = [] 
        for x in boards:
                x = x.strip()
                if x == "}":
                        positions = False
                        moves[move].loadmoves(loadmove)
                        move += 1

                        loadmove = [] 
                    
                
                if positions == True:
                        z = json.loads(x)
                        loadmove.append(z)

                
                if x == "{":
                        positions = True
                

loadboardpositions()

for i in range(len(moves[0].rows)):
       print moves[0].rows[i]

        
#open('boardpositions.txt', 'w').close()

#for i in range (len(moves)):
#        moves[i].outputmoves("boardpositions.txt")



input("halt!")
