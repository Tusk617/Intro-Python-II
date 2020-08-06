class Items():
    def __init__(self, Iname, Idesc):
        self.Iname = Iname
        self.Idesc = Idesc
    def __repr__(self):
        return f"{self.Iname}"