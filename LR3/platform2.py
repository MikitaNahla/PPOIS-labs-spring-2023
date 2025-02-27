import pygame as pg

from const import *


class Platform2(object):
    def __init__(self, x_pos, y_pos):
        self.image = pg.image.load('images/block_debris0.png').convert_alpha()
        self.rectangles = [
            pg.Rect(x_pos - 20, y_pos + 16, 16, 16),
            pg.Rect(x_pos - 20, y_pos - 16, 16, 16),
            pg.Rect(x_pos + 20, y_pos + 16, 16, 16),
            pg.Rect(x_pos + 20, y_pos - 16, 16, 16)
        ]
        self.yVel = -4
        self.rect = None

    def update(self, core):
        self.yVel += GRAVITY * FALL_MULTI
        for i in range(len(self.rectangles)):
            self.rectangles[i].y += self.yVel
            if i < 2:
                self.rectangles[i].x -= 1
            else:
                self.rectangles[i].x += 1
        if self.rectangles[1].y > core.get_map().mapSize[1] * 32:
            core.get_map().debris.remove(self)

    def render(self, core):
        for rect in self.rectangles:
            self.rect = rect
            core.screen.blit(self.image, core.get_map().get_camera().apply(self))
