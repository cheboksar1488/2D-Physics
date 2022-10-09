import pygame as software
from math import *
def settings():
    settings={
        'screen_size': (1080, 690),
        'gravity': 1,
        'air_resistance':1,
        'fps':60,
    }; return settings
class Software:
    def __init__(self):
        software.init()
        self.window=software.display.set_mode(settings()['screen_size'])
        self.circle=Object((100, 230), 16, 0.9, 25, ((300, 50), (1000, 350)))
        self.circle2=Object((300, 50), 13, 0.9, 13, ((100, 230), (1000, 350)))
        self.circle3=Object((1000, 350), -15, 0.5, 25, ((100, 230, 300, 50)))
    def run(self):
        while True:
            software.time.Clock().tick(settings()['fps'])
            for event in software.event.get():
                if event.type==software.QUIT:
                    exit()
                if event.type==software.MOUSEBUTTONDOWN:
                    print(f'click{event.pos}')
            self.window.fill((0,0,0))

            software.draw.circle(self.window, (255,0,0), self.circle.collision(), 25)
            software.draw.circle(self.window, (0, 255, 0), self.circle2.collision(), 13)
            software.draw.circle(self.window, (0, 0, 255), self.circle3.collision(), 25)

            software.display.flip()
class Object:
    def __init__(self, position, energy, stiffness_coefficient, radius, world_list_position_objects):
        self.agree=-pi/3
        x=energy*cos(self.agree)
        y=energy*sin(self.agree)
        self.position=position
        self.speed=energy
        self.size=radius
        self.stiffness_coefficient=stiffness_coefficient
        self.v_x=x
        self.v_y=y
        self.world_positions_objects=world_list_position_objects
        self.ticks=[]
    def collision(self):
        key=software.key.get_pressed()
        if key[software.K_SPACE]:
            self.position=software.mouse.get_pos()[0], software.mouse.get_pos()[1]
            self.v_x=software.mouse.get_pos()[0]-self.ticks[-1][0]
            self.v_y=software.mouse.get_pos()[1]-self.ticks[-1][1]
        self.x_x=self.v_x*settings()['air_resistance']
        self.x_y=self.v_y+settings()['gravity']*settings()['air_resistance']
        self.position=self.position[0]+self.v_x, self.position[1]+self.v_y
        if self.position[1]+self.size>=settings()['screen_size'][1] or self.position[1]-self.size<=0:
            self.position=self.position[0], self.position[1]-settings()['gravity']-settings()['air_resistance']
            self.v_y=-self.v_y*self.stiffness_coefficient
        if self.position[0]+self.size>=settings()['screen_size'][0] or self.position[0]-self.size<=0:
            self.v_x=-self.v_x*self.stiffness_coefficient
        self.position=self.position[0], self.position[1]
        #print(f'position: x={self.position[0]}; | y={self.position[1]}')
        self.ticks.append(software.mouse.get_pos())
        return (self.position)
Software().run()
