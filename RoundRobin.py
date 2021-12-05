from random import randint, sample
import random
from typing import List
from PBC import PCB

from my_colors import Color

import pygame


class RoundRobin:
    def __init__(
        self,
        n_fila: int,
        n_processos: int,
        surface: pygame.Surface,
        font: pygame.font.Font,
    ):

        self.numbers = sample(range(0, 100), n_processos)
        self.n: int = n_fila
        self.processes: List[PCB] = [
            PCB(self.numbers.pop(), randint(2, 10), surface, font)
            for _ in range(n_processos)
        ]
        self.quantum = random.randint(1,5)

        self.prioridade: int = randint(1, 10)

        self.main_surface = surface
        self.font = font

        self.current_process: int = 0
        self.terminou: bool = False

    def process_queue(self) -> str:
        if len(self.processes) == 0:
            self.terminou = True
            return

        self.processes[self.current_process].process(self.quantum)

        if self.processes[self.current_process].terminou:
            self.processes.pop(self.current_process)

            if self.current_process == len(self.processes) and len(self.processes) != 0:
                # self.current_process = (self.current_process + 1) % len(self.processes)
                self.current_process = 0
            return

        if self.current_process == len(self.processes) and len(self.processes) != 0:
            self.current_process = (self.current_process + 1) % len(self.processes)
            return

        self.current_process = (self.current_process + 1) % len(self.processes)

    def __repr__(self) -> str:
        return f"Prioridade: {self.prioridade}"

    def draw(self, x, y, active):

        if active:
            self.main_surface.blit(
                self.font.render(
                    f"Fila {self.n} - Prioridade {self.prioridade}({self.quantum}s)",
                    True,
                    Color.queue_process
                ),
                [x, y - 15],
            )
        else:
            self.main_surface.blit(
                self.font.render(
                    f"Fila {self.n} - Prioridade {self.prioridade}({self.quantum}s)",
                    True,
                    Color.normal_text,
                ),
                [x, y - 15],
            )

        for i in range(len(self.processes)):
            if i == self.current_process and active:
                self.processes[i].draw(
                    x + ((self.processes[i].width + 30) * i), y, True
                )
            else:
                self.processes[i].draw(
                    x + ((self.processes[i].width + 30) * i), y, False
                )
