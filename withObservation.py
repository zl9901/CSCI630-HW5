
from math import  *
from numpy import *
class markov():

    def __init__(self):
        self.meetingDic={"happy":0.1,"unhappy":0.1,"meh":0.8}
        self.workingDic={"happy":0.3,"unhappy":0.1,"meh":0.6}
        self.surfingDic={"happy":0.5,"unhappy":0.3,"meh": 0.2}
        """
        type the sequence of faces to be calaculated
        """
        # self.input = ["happy", "meh", "unhappy"]
        self.input=["unhappy", "meh", "happy","unhappy", "meh", "happy","unhappy", "meh", "happy","unhappy", "meh", "happy"]


        """
        already known conditions
        """
        #["WW","WM","WS"],["SS","SW","SM"],["MM","MW","MS"]
        self.transition= [[0.5, 0.25, 0.25], [0.25, 0.5, 0.25], [0.0, 1/3, 2/3]]
        #[working,surfing,meeting]
        self.states={"working":0.5,"meeting":0.25,"surfing":0.25}
        """
        return the final result
        """
        self.res=array([])


    def iteration(self):
        index=len(self.input)-1
        i=1
        """
        first row in the graph that needs to be calculated
        """
        w=self.states["working"]*(self.workingDic[self.input[i-1]])
        s=self.states["surfing"]*(self.surfingDic[self.input[i-1]])
        m=self.states["meeting"]*(self.meetingDic[self.input[i-1]])
        column=[]
        column.append(w)
        column.append(s)
        column.append(m)
        self.res=array(column)
        sum = 0
        for item in self.res:
            sum += item
        print(self.res[0]/sum,end=' ')
        print(self.res[1]/sum,end=' ')
        print(self.res[2]/sum)
        # print(self.res)
        while i<=index:
            """
            matrix operations
            do it recursively using while loop
            """
            matrix = []
            workingArray = []
            ww=self.workingDic[self.input[i]]*(self.transition[0][0])
            sw=self.workingDic[self.input[i]]*(self.transition[1][1])
            mw=self.workingDic[self.input[i]] * (self.transition[2][1])

            workingArray.append(ww)
            workingArray.append(sw)
            workingArray.append(mw)


            ws=self.surfingDic[self.input[i]]*(self.transition[0][2])
            ss=self.surfingDic[self.input[i]]*(self.transition[1][0])
            ms=self.surfingDic[self.input[i]]*(self.transition[2][2])
            surfingArray = []
            surfingArray.append(ws)
            surfingArray.append(ss)
            surfingArray.append(ms)


            wm=self.meetingDic[self.input[i]]*(self.transition[0][1])
            sm=self.meetingDic[self.input[i]]*(self.transition[1][2])
            mm=self.meetingDic[self.input[i]]*(self.transition[2][0])
            meetingArray = []
            meetingArray.append(wm)
            meetingArray.append(sm)
            meetingArray.append(mm)


            matrix.append(workingArray)
            matrix.append(surfingArray)
            matrix.append(meetingArray)
            matrixT=array(matrix)

            self.res=dot(matrixT,self.res)
            i+=1

            """
            print 12 steps result
            """
            sum = 0
            for item in self.res:
                sum += item
            print(self.res[0]/sum,end=' ')
            print(self.res[1]/sum,end=' ')
            print(self.res[2]/sum)
            # print(self.res)
        return self.res


def main():
    g=markov()
    g.iteration()



if __name__ == "__main__": main()
