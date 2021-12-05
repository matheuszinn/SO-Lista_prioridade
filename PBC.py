import random
from datetime import datetime
import time

from my_colors import Color

import pygame
from pygame.constants import CONTROLLER_AXIS_LEFTX


class PCB:
    def __init__(
        self,
        pid: int,
        tempo_execucao: int,
        surface: pygame.Surface,
        font: pygame.font.Font,
    ):

        self.width: int = 145
        self.height: int = 120

        self.pid = pid
        self.name = f"Processo {self.pid}"
        self.prioridade = random.randint(0, 10)
        self.data_hora = datetime.now().strftime("%H:%M:%S:%f")
        self.endereco_inicial = tempo_execucao + random.randint(0, 10)
        self.endereco_final = tempo_execucao + self.pid

        self.tempo_restante = tempo_execucao

        self.terminou = False

        self.font: pygame.font.Font = font
        self.main_surface = surface

    def draw(self, x, y, active: bool):

        texts = [
            f"{self.name} ({self.tempo_restante}s)",
            f"pid: {self.pid}",
            f"prioridade: {self.prioridade}",
            f"hora: {self.data_hora}",
            f"addr inicial: {self.endereco_inicial}",
            f"addr final: {self.endereco_final}",
        ]

        label = [
            self.font.render(text, True, Color.processing_text if active else Color.normal_text)
            for text in texts
        ]

        for line in range(len(label)):
            self.main_surface.blit(label[line], (x + 5, y + 3 + (line * 20)))

        pygame.draw.rect(
            self.main_surface,
            Color.processing_box if active else Color.normal_text,
            pygame.Rect(x, y, self.width, self.height),
            2,
        )

    def process(self, quantum):
        while True:
            if quantum != 0 and self.tempo_restante != 0:
                time.sleep(1)
                quantum -= 1
                self.tempo_restante -= 1

                if self.tempo_restante == 0:
                    self.terminou = True
                    break

                if quantum == 0:
                    break
