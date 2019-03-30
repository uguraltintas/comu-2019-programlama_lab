class oku():
    def __init__(self, dosya=""):
        f=open("C:\\Users\\asus\\Desktop\\file.txt","r")
        myContent=f.read()
        cümle = myContent.split(".")
        self.myWords=[]
        for sentence in cümle:
            WordsInTheSentence=sentence.split(" ")
            for word_1 in WordsInTheSentence:
                self.myWords.append(word_1)
        self.frek1()
        self.wfrek1()
        
        
    def frek1(self):
        self.freklist1={}
        for word in self.myWords:
            if(word in self.freklist1):
                self.freklist1[word]+=1
            else:
                self.freklist1[word]=1
        
    
    def wfrek1(self):
        for word1 in self.freklist1:
            print(word1+" "+str(self.freklist1[word1]))
    

myclass1=oku()
print(myclass1.freklist1['all'])