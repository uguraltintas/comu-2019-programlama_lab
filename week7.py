from random import choice as rast
import pylab
import numpy
def rollDie():
    """Returns a random int between 1 and 6"""
    return rast([1,2,3,4,5,6])
    
def rollN(n):
    result=''
    for i in range(n):
        result=result+str(rollDie())+""
    print(result)

rollN(5)
def flip(numFlips):
    heads=0
    for i in range(numFlips):
        if rast(('H','T'))=='H':
            heads+=1
    return heads/numFlips
def flipSim(numFlipsPerTrial,numTrials):
    fracheads=[]
    for i in range(numTrials):
        fracheads.append(flip(numFlipsPerTrial))
        mean=sum(fracheads)/len(fracheads)
    return mean
print(flipSim(10,100))

def flipPlot(minExp, maxExp):
    ratios, diffs, xAxis = [], [], []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.choice(('H', 'T')) == 'H':
                numHeads += 1
                numTails = numFlips - numHeads
        try:
            ratios.append(numHeads/numTails)
            diffs.append(abs(numHeads - numTails))
        except ZeroDivisionError:
            continue
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.plot(xAxis, diffs, 'k')
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('#Heads/#Tails')
    pylab.plot(xAxis, ratios, 'k')
random.seed(0)
flipPlot(4, 20)