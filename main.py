from random import randint
from typing import List
import pygame
from PBC import PCB

from my_colors import Color

from RoundRobin import RoundRobin


class App:
    def __init__(self):

        pygame.init()
        pygame.font.init()

        pygame.display.set_caption('Fila de prioridade')

        self.comecou = False

        self.main_surface = pygame.display.set_mode((1280, 700))
        self.font = pygame.font.SysFont("fantasquesansmononerdfontmono.ttf", 20)
        self.initFont = pygame.font.SysFont("fantasquesansmononerdfontmono.ttf", 30)

        self.bg = pygame.image.load("background.jpg").convert()
        self.clock = pygame.time.Clock()

        self.queues: List[RoundRobin] = []

        for i in range(4):
            self.queues.append(
                RoundRobin(i + 1, randint(1, 7), self.main_surface, self.font)
            )

        self.queues_sorted = sorted(
            self.queues, key=lambda a: a.prioridade, reverse=True
        )
        self.current_queue = 0


    def draw(self):
        self.main_surface.fill(Color.background)

        for i in range(len(self.queues)):
            if self.current_queue == i:
                self.queues_sorted[i].draw(30, 60 + (i * 145), True)
            else:
                self.queues_sorted[i].draw(30, 60 + (i * 145), False)

    def run(self):
        while True:

            if self.comecou:
                if self.queues_sorted[self.current_queue].terminou:
                    self.current_queue = (self.current_queue + 1) % len(self.queues_sorted)
                else:
                    self.queues_sorted[self.current_queue].process_queue()

            self.clock.tick(60)
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key == pygame.K_SPACE:
                        self.comecou = True
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()


App().run()
