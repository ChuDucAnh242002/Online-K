class Player:
    def __init__(self, id):
        self.id = id
        self.point = 5
        self.input = []
        self.locked = False
    
    def get_num(self):
        self.num = int("".join(self.input))
        return self.num

    def get_point(self):
        return self.point

    def reset(self):
        self.point = 5
        self.input = []
        self.locked = False
