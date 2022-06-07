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
        return self.ave

    def cal_ave(self):
        for player in self.players:
            self.sum += player.get_num()
        self.ave = self.sum * 0.8 / len(self.players)

    def end_match(self):
        # min is for compare with average, player mins to store the smalles player value
        min = 100
        player_min = 100
        player_num = []

        for player in self.players:
            if player.locked == False:
                return False

        self.cal_ave()

        for player in self.players:
            temp_min = player.get_num()
            player_num.append(temp_min)
            if min > abs(self.ave - temp_min):
                min = abs(self.ave - temp_min)
                player_min = temp_min

        duplicates = [number for number in player_num if player_num.count(number) > 1]
        unique_duplicate = list(set(duplicates))

        # New rule when there are 3 player left
        if len(self.players) <= 3 and unique_duplicate != []:
            duplicate = unique_duplicate[0]
            for player in self.players:
                if player.get_num() == duplicate:
                    player.point -= 1
                else:
                    self.winners.append(player)
            return True
                    
        # player_num is list of player number, 5 of them
        # num is index, m is value
        for num, m in enumerate(player_num):
            # Go through the list of player nums and find the one who is the closest
            cur_player = self.players[num]
            if player_min != m :
                if 0 in player_num:
                    if cur_player.get_num() == 100:
                        self.winners.append(cur_player)
                    else:
                        cur_player.point -= 1
                else:
                    cur_player.point -= 1

            # Found the one closest
            elif player_min == m:
                if 100 in player_num:
                    if player_min == 0:
                        cur_player.point -=1
                    else:
                        self.winners.append(cur_player)
                else:
                    self.winners.append(cur_player)

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
        
    def kill_player(self):
        for player in self.players:
            if player.dead():
                self.players.remove(player)

    def check_death(self):
        for player in self.players:
            if player.dead():
                return True
        return False