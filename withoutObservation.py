
from math import  *
from numpy import *
class markov():

    def __init__(self):
        """
        already known conditions
        """
        #["WW","WM","WS"],["SS","SW","SM"],["MM","MW","MS"]
        self.transition= [[0.5, 0.25, 0.25], [0.25, 0.5, 0.25], [0.0, 1/3, 2/3]]
        #[working,surfing,meeting]
        self.states={"working":0.5,"meeting":0,"surfing":0.5}
        """
        return the final result
        """
        self.res=array([])


    def iteration(self):
        """
        here how many steps should be given
        """
        # index = 2
        index=11
        i=1
        """
        first row in the graph that needs to be calculated
        """
        column=[]
        column.append(self.states["working"])
        column.append(self.states["surfing"])
        column.append(self.states["meeting"])
        self.res=array(column)
        while i<=index:
            """
            matrix operations
            do it recursively using while loop
            """
            matrix = []
            workingArray = []
            workingArray.append(self.transition[0][0])
            workingArray.append(self.transition[1][1])
            workingArray.append(self.transition[2][1])


            surfingArray = []
            surfingArray.append(self.transition[0][2])
            surfingArray.append(self.transition[1][0])
            surfingArray.append(self.transition[2][2])


            meetingArray = []
            meetingArray.append(self.transition[0][1])
            meetingArray.append(self.transition[1][2])
            meetingArray.append(self.transition[2][0])


            matrix.append(workingArray)
            matrix.append(surfingArray)
            matrix.append(meetingArray)
            matrixT=array(matrix)

            self.res=dot(matrixT,self.res)
            i+=1
            """
            print 12 steps result
            """
            print(self.res)
        return self.res


def main():
    g=markov()
    print(g.iteration())









if __name__ == "__main__": main()
