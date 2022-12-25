import pygame
from sys import exit
import os

class Board():
    #   Custom Environment that follows gym interface
    def __init__(self) -> None:
        self.board = [0] * 9
        self.error_move = False
        self.end = False

    def game_over(self):
        if 0 not in self.board or self.check_if_winner() != None:
            return True
        else:
            return False

    def win_tie(self):
        if self.check_if_winner() == None and self.game_over():
            return 0
        else:
            return self.check_if_winner()

    def check_if_winner(self):
        for i in range(0,7,3):          #check row
            if self.board[i] == self.board[i+1] and self.board[i] == self.board[i+2] and self.board[i] != 0:
                return self.board[i]

        for i in range(0,3):            #check col
            if self.board[i] == self.board[i+3] and self.board[i] == self.board[i+6] and self.board[i] != 0:
                return self.board[i]

        #check cross
        if ((self.board[0] == self.board[4] and self.board[0] == self.board[8]) or (self.board[2] == self.board[4] and self.board[2] == self.board[6])) and self.board[4] != 0:
            return self.board[4]
        
        return None

    def player_turn(self):
        length = [x for x in self.board if x == 0]

        if len(length)%2 != 0:
            return 1.0  #   if there are an odd number of empty spots it is 1.0 aka X turn
        else:
            return -1.0 #   else the number of empty spots is even and it is -1.0 aka O turn

    # def error_move(self, error:bool):
    #     return error

    def fill_board(self, input):
        empty_space = [x+1 for x in range(0, len(self.board)) if self.board[x] == 0]
        num_range = [x for x in range(1, 10)]

        if input in empty_space and input in num_range:
            self.board[input-1] = self.player_turn()
            self.error_move = False
        else:
            self.error_move = True

    def render(self):
        pygame.init()

        locations = [(125, 90),(285,90),(450,90),
            (125,245),(285,245),(450,245),
            (125,415),(285,415),(450,415)]

        horizontal = 690
        vertical = 600
        screen = pygame.display.set_mode((horizontal, vertical))

        #   Title on the window
        pygame.display.set_caption("TicTacToe")

        #   fps
        clock = pygame.time.Clock()

        board_image = pygame.image.load('tictactoeboard.jpeg').convert()
        board_image_rect = board_image.get_rect(center = (345, 300))

        x_image = pygame.image.load('tictactoeX.jpeg').convert_alpha()
        o_image = pygame.image.load('tictactoeO.jpeg').convert_alpha()

        prompt_image = pygame.image.load('prompt.jpeg').convert_alpha()
        prompt_image_rect = prompt_image.get_rect(center = (348,20))

        prompt_yes = pygame.image.load('prompt_yes.jpeg').convert_alpha()
        prompt_yes_rect = prompt_yes.get_rect(center = (409,20))
        prompt_no = pygame.image.load('prompt_no.jpeg').convert_alpha()
        prompt_no_rect = prompt_no.get_rect(center = (462,20))

        blank = pygame.image.load('testSpace.jpeg').convert_alpha()
        blank_1_rect = blank.get_rect(center = (188, 140))
        blank_2_rect = blank.get_rect(center = (348,140))
        blank_3_rect = blank.get_rect(center = (510,140))
        blank_4_rect = blank.get_rect(center = (188,301))
        blank_5_rect = blank.get_rect(center = (348,301))
        blank_6_rect = blank.get_rect(center = (510,301))
        blank_7_rect = blank.get_rect(center = (188,460))
        blank_8_rect = blank.get_rect(center = (348,460))
        blank_9_rect = blank.get_rect(center = (510,460))

        ttt_font = pygame.font.Font(None, 30)

        tie_text = ttt_font.render('Tie', False, 'Red')
        tie_rect = tie_text.get_rect(center = (348, 575))
        x_wins_text = ttt_font.render('X Wins', False, 'Red')
        x_wins_rect = x_wins_text.get_rect(center = (352, 575))
        o_wins_text = ttt_font.render('O Wins', False, 'Red')
        o_wins_rect = o_wins_text.get_rect(center = (352, 575))

        error_text = ttt_font.render('Error try again!', False, 'Red')
        error_rect = error_text.get_rect(center = (352, 575))

        x_on_board = [x for x in range(0, len(self.board)) if self.board[x] == 1]        #Get index of all x positions on board
        o_on_board = [x for x in range(0, len(self.board)) if self.board[x] == -1]       #Get index of all o positions on board

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if blank_1_rect.collidepoint(event.pos):
                    self.fill_board(1)
                elif blank_2_rect.collidepoint(event.pos):
                    self.fill_board(2)
                elif blank_3_rect.collidepoint(event.pos):
                    self.fill_board(3)
                elif blank_4_rect.collidepoint(event.pos):
                    self.fill_board(4)
                elif blank_5_rect.collidepoint(event.pos):
                    self.fill_board(5)
                elif blank_6_rect.collidepoint(event.pos):
                    self.fill_board(6)
                elif blank_7_rect.collidepoint(event.pos):
                    self.fill_board(7)
                elif blank_8_rect.collidepoint(event.pos):
                    self.fill_board(8)
                elif blank_9_rect.collidepoint(event.pos):
                    self.fill_board(9)
                elif prompt_yes_rect.collidepoint(event.pos):
                    self.board = [0] * 9
                    self.error_move = False
                elif prompt_no_rect.collidepoint(event.pos):
                    self.end = True


        screen.blit(board_image, board_image_rect)

        if x_on_board:
            for i in x_on_board:
                screen.blit(x_image, locations[i])

        if o_on_board:
            for i in o_on_board:
                screen.blit(o_image, locations[i])

        if self.win_tie() == 1:
            screen.blit(x_wins_text, x_wins_rect)
            screen.blit(prompt_image, prompt_image_rect)
            screen.blit(prompt_yes, prompt_yes_rect)
            screen.blit(prompt_no, prompt_no_rect)
        elif self.win_tie() == -1:
            screen.blit(o_wins_text, o_wins_rect)
            screen.blit(prompt_image, prompt_image_rect)
            screen.blit(prompt_yes, prompt_yes_rect)
            screen.blit(prompt_no, prompt_no_rect)
        elif self.win_tie() == 0:
            screen.blit(tie_text, tie_rect)
            screen.blit(prompt_image, prompt_image_rect)
            screen.blit(prompt_yes, prompt_yes_rect)
            screen.blit(prompt_no, prompt_no_rect)

        if self.error_move:
            screen.blit(error_text, error_rect)

        pygame.display.update()
        clock.tick(60)  #   60 fps
