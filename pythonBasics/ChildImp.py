from pythonBasics.OopsDemo import Calculator


class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = ChildImpl()
print("parent object method result: ", obj.Summation())

print("child object method result: ",obj.getCompleteData())
