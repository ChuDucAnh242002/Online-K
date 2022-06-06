import pygame
import sys
# import os

from button import Button
from network import Network

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 750, 750

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Card game")

CLOCK = pygame.time.Clock()
FPS = 10

# Font
FONT1 = pygame.font.SysFont("comicsans", 48)
FONT1_1 = pygame.font.SysFont("comicsans", 60)
FONT2 = pygame.font.SysFont("comicsans", 24)


# POSITION
POSITION1_WIDTH, POSITION1_HEIGHT = WIDTH //2, HEIGHT *3//4
POSITION2_WIDTH, POSITION2_HEIGHT = 10, HEIGHT* 0.7//2
POSITION3_WIDTH, POSITION3_HEIGHT = 200, 0
POSITION4_WIDTH, POSITION4_HEIGHT = 450, 0
POSITION5_WIDTH, POSITION5_HEIGHT = 500, HEIGHT* 0.7//2

# Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 0, 255)

n = Network()

def draw_win(cur_player, players, p):

    WIN.fill(WHITE)
    for num, player in enumerate(players):
        player_text = f"Player {num}"
        if num == p:
            player_text = FONT1.render(player_text, 1, BLUE)
        else:
            player_text = FONT2.render(player_text, 1, BLUE)
        draw_player(player_text, num, p)

    draw_input(cur_player)
    draw_point(p, players)
    draw_locked(players, p)
    
        
def draw_player(player_text, num, p):

    pos = num - p
    # Current player
    if pos == 0:
        WIN.blit(player_text, (POSITION1_WIDTH - player_text.get_width() /2, POSITION1_HEIGHT - player_text.get_height() /2))

    elif pos == 1 or pos == -4:
        WIN.blit(player_text, (POSITION2_WIDTH, POSITION2_HEIGHT))
    elif pos == 2 or pos == -3:
        WIN.blit(player_text, (POSITION3_WIDTH, POSITION3_HEIGHT))
    elif pos == 3 or pos == -2:
        WIN.blit(player_text, (POSITION4_WIDTH, POSITION4_HEIGHT))
    elif pos == 4 or pos == -1:
        WIN.blit(player_text, (POSITION5_WIDTH, POSITION5_HEIGHT))

def draw_locked(players, p):

    for num, player in enumerate(players):
        if player.locked:
            pos = num - p
            lock_in_text = "Locked in"
            if pos == 0:
                lock_in_text = FONT1_1.render(lock_in_text, 1, BLACK)
                WIN.blit(lock_in_text, (450, HEIGHT - 100))
            else:
                lock_in_text = FONT2.render(lock_in_text, 1, BLACK)
                if pos == 1 or pos == -4:
                    WIN.blit(lock_in_text, (POSITION2_WIDTH, POSITION2_HEIGHT + 70))
                elif pos == 2 or pos == -3:
                    WIN.blit(lock_in_text, (POSITION3_WIDTH, POSITION3_HEIGHT + 70))
                elif pos == 3 or pos == -2:
                    WIN.blit(lock_in_text, (POSITION4_WIDTH, POSITION4_HEIGHT + 70))
                elif pos == 4 or pos == -1:
                    WIN.blit(lock_in_text, (POSITION5_WIDTH, POSITION5_HEIGHT + 70))

def handle_input(cur_player):
    global n
    keys = pygame.key.get_pressed()
    datas = ["input"]
    text = ""
    if len(cur_player.input) == 0 :
        if keys[pygame.K_0]:
            text = "0"
        elif keys[pygame.K_1]:
            text = "1"
        elif keys[pygame.K_BACKSPACE]:
            text = "back"

    elif cur_player.input[0] == '1' and len(cur_player.input) > 0:
        if keys[pygame.K_0]:
            text = "0"
        elif keys[pygame.K_BACKSPACE]:
            text = "back"
    else:
        if keys[pygame.K_0]:
            text = "0"
        elif keys[pygame.K_1]:
            text = "1"
        elif keys[pygame.K_2]:
            text = "2"
        elif keys[pygame.K_3]:
            text = "3"
        elif keys[pygame.K_4]:
            text = "4"
        elif keys[pygame.K_5]:
            text = "5"
        elif keys[pygame.K_6]:
            text = "6"
        elif keys[pygame.K_7]:
            text = "7"
        elif keys[pygame.K_8]:
            text = "8"
        elif keys[pygame.K_9]:
            text = "9"
        elif keys[pygame.K_BACKSPACE]:
            text = "back"

    datas.append(text)
    data = " ".join(datas)
    n.send(data)
        
def draw_point(p, players):
    for num, player in enumerate(players):
        pos = num -p
        point_text = f"Point: {str(player.get_point())}"
        if pos == 0:
            point_text = FONT1_1.render(point_text, 1, GREEN)
            WIN.blit(point_text, (0, HEIGHT -100))
        else:
            point_text = FONT2.render(point_text, 1, GREEN)
            if pos == 1 or pos == -4:
                WIN.blit(point_text, (POSITION2_WIDTH + 100, POSITION2_HEIGHT))
            elif pos == 2 or pos == -3:
                WIN.blit(point_text, (POSITION3_WIDTH + 100, POSITION3_HEIGHT))
            elif pos == 3 or pos == -2:
                WIN.blit(point_text, (POSITION4_WIDTH + 100, POSITION4_HEIGHT))
            elif pos == 4 or pos == -1:
                WIN.blit(point_text, (POSITION5_WIDTH + 100, POSITION5_HEIGHT))
            
def draw_input(cur_player):
    if cur_player.input == []:
        return
    for i, input in enumerate(cur_player.input):
        input = FONT1_1.render(input, 1, BLUE)
        WIN.blit(input, (250 + 100*i, HEIGHT - 150))

# Draw when end match
def draw_winner(winners):
    winner_text = "Winner:"
    for winner in winners:
        winner_text += (" " + str(winner.id))
    winner_text = FONT1_1.render(winner_text, 1, ORANGE)
    WIN.blit(winner_text, (WIDTH //2 - winner_text.get_width() /2, HEIGHT //2 - winner_text.get_height() /2 - 200))

def draw_ave(game):
    ave_text = f"Average: {game.get_ave():.2f}"
    ave_text = FONT1_1.render(ave_text, 1, YELLOW)
    WIN.blit(ave_text, (WIDTH //2 - ave_text.get_width() /2, HEIGHT //2 - ave_text.get_height() /2 + 50))
    
def draw_multi_num(players, p):

    for num, player in enumerate(players):
        pos = num - p
        input_text = str(player.get_num())
        if pos != 0:
            input_text = FONT2.render(input_text, 1, BLUE)
            if pos == 1 or pos == -4:
                WIN.blit(input_text, (POSITION2_WIDTH, POSITION2_HEIGHT  + 35))
            if pos == 2 or pos == -3:
                WIN.blit(input_text, (POSITION3_WIDTH, POSITION3_HEIGHT + 35))
            if pos == 3 or pos == -2:
                WIN.blit(input_text, (POSITION4_WIDTH, POSITION4_HEIGHT + 35))
            if pos == 4 or pos == -1:
                WIN.blit(input_text, (POSITION5_WIDTH, POSITION5_HEIGHT + 35))
            
def main():
    run = True
    input = True

    p = int(n.getP())
    print("You are player", p)

    while run:
        CLOCK.tick(FPS)

        try:
            game = n.send("get")
            players = game.get_players()
            cur_player = players[p]
        except:
            run = False
            print("Couldn't get game")
            break
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if cur_player.input != []:
                n.send("locked")

        if input:
            handle_input(cur_player)
        
        draw_win(cur_player, players, p)
        if game.end_match():

            draw_winner(game.winners)
            draw_ave(game)
            draw_multi_num(players, p)
            pygame.display.update()
            pygame.time.delay(2000)
            
            n.send("reset match")

        if game.end_game():
            pygame.time.delay(1000)
            n.send("reset")


        pygame.display.update()

def menu():
    run = True
    wait_button = Button(300, 300, "Click to play")

    while run:

        WIN.fill(WHITE)
        wait_button.draw(WIN)
        

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                main()
                break        

if __name__ == "__main__":
    while True:
        menu()