class Player:
    def __init__(self, id):
        self.id = id
        self.point = 10
        self.input = []
        self.locked = False
    
    def get_num(self):
        self.num = int("".join(self.input))
        return self.num

    def get_point(self):
        return self.point

    def reset(self):
        self.point = 10
        self.input = []
        self.locked = False

    def dead(self):
        if self.point == 0:
            return True
