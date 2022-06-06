class Game:
    def __init__(self, id, players):
        self.id = id
        self.players = players
        self.sum = 0
        self.ave = 0
        self.winners = []

    def get_players(self):
        return self.players

    def cal_ave(self):
        for player in self.players:
            self.sum += player.get_num()
        self.ave = self.sum * 0.8 / len(self.players)

    def get_ave(self):
        return self.ave

    def end_match(self):
        min = 100
        player_min = 100
        temp_mins = []

        for player in self.players:
            if player.locked == False:
                return False

        self.cal_ave()
        for player in self.players:
            temp_min = player.get_num()
            temp_mins.append(temp_min)
            if min > abs(self.ave - temp_min):
                min = abs(self.ave - temp_min)
                player_min = temp_min

        for num, m in enumerate(temp_mins):
            if player_min != m :
                if 0 in temp_mins:
                    if self.players[num].get_num() == 100:
                        self.winners.append(self.players[num])
                    else:
                        self.players[num].point -= 1
                else:
                    self.players[num].point -= 1
            elif player_min == m:
                if 100 in temp_mins:
                    if player_min == 0:
                        self.players[num].point -=1
                    else:
                        self.winners.append(self.players[num])
                else:
                    self.winners.append(self.players[num])

        return True

    def reset_match(self):
        self.sum = 0
        self.ave = 0
        self.winners = []
        for player in self.players:
            player.input = []
            player.locked = False

    def reset(self):
        self.sum = 0
        self.ave = 0
        self.winner = []
        
        for player in self.players:
            player.reset()

    def end_game(self):
        count_0 = 0
        for player in self.players:
            if player.get_point() == 0:
                count_0 += 1
        if count_0 == len(self.players) - 1 and len(self.players) > 1:
            return True
        return False
        
    def check_death(self):
        for player in self.players:
            if player.dead():
                self.players.remove(player)