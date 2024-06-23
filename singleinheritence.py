class parent:
    def __init__(self):
        self.x=500
class child(parent):
    def __init__(self):
        super().__init__()
        self.y=100
c1=child()
total=c1.x+c1.y
print("From Parent:",c1.x)
print("From Parent:",c1.y)
print("Total:",total)