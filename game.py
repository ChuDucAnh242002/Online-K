class Game:
    def __init__(self, id, players):
        self.id = id
        self.players = players
        self.sum = 0
        self.ave = 0
        self.winners = []

    def get_players(self):
        return self.players

    def get_ave(self):

        for player in self.players:
            self.sum += player.get_num()
        self.ave = self.sum * 0.8 / len(self.players)
        return self.ave

    def end_match(self):
        min = 100
        temp_mins = []

        for player in self.players:
            if player.locked == False:
                return False

        for player in self.players:
            temp_min = player.get_num()
            temp_mins.append(temp_min)
            if min > temp_min:
                min = temp_min

        for num, m in enumerate(temp_mins):
            if min == m :
                self.winners.append(self.players[num])
            if min != m :
                self.players[num].point -= 1
        return True

    def reset_match(self):
        self.sum = 0
        self.ave = 0
        for player in self.players:
            player.input = []
            player.locked = False

    def reset(self):
        self.sum = 0
        self.ave = 0

        for player in self.players:
            if player.point > 0:
                return False
        
        for player in self.players:
            player.reset()


        
