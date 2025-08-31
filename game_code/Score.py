from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from game_code.Const import SCORE_POS, C_VERMELHO, C_AMARELO, MENU_OP
from game_code.DBProxy import DBProxy


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/Score.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode: str, player_score: list[int]):
        self.window.blit(source=self.surf, dest=self.rect)
        db_proxy = DBProxy('DBSScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(70, 'YOU WIN!!', C_VERMELHO, SCORE_POS['Title'])
            self.score_text(68, 'YOU WIN!!', C_AMARELO, SCORE_POS['Title'])
            score = player_score[0]
            if game_mode == MENU_OP[0]:
                self.score_text(30, 'Insira seu nome com (5 caracteres):', C_VERMELHO, SCORE_POS['EnterName'])
                self.score_text(30, ' Insira seu nome com (5 caracteres):', C_AMARELO, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 5:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 5:
                            name += event.unicode
            self.score_text(70, name, C_VERMELHO, SCORE_POS['Name'])
            self.score_text(68, name, C_AMARELO, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show(self):
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(70, '    TOP 5', C_VERMELHO, SCORE_POS['Title'])
        self.score_text(68, '    TOP 5', C_AMARELO, SCORE_POS['Title'])
        self.score_text(35, 'NAME     SCORE            DATA', C_VERMELHO, SCORE_POS['Label'])
        self.score_text(36, 'NAME     SCORE            DATA', C_AMARELO, SCORE_POS['Label'])
        db_proxy = DBProxy('DBSScore')
        list_score = db_proxy.retrieve_top5()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(24, f' {name}     -     {score:05d}     -     {date}', C_VERMELHO,
                            SCORE_POS[list_score.index(player_score)])
            self.score_text(24, f'  {name}     -     {score:05d}      -    {date}', C_AMARELO,
                            SCORE_POS[list_score.index(player_score)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Impact", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime('%H:%M')
    current_date = current_datetime.strftime('%Y-%m-%d')
    return f'{current_time} - {current_date}'
