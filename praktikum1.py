class person:
    def __init__(self, fname, lname):
        self.fristname = fname
        self.lastname = lname

    def printname(self):
        print(self.fristname,self.lastname)

class student(person):
    pass
m = student ("kaesang", "pangarep")
n = student ("muhammad", "hamzah")

m.printname()
n.printname()