#! /usr/bin/python3
from Screen.GameScreen import *
from Screen.MainScreen import *
import View.Renderer as Renderer
from  Model.Ship import Ship
import random



class GameData:
    def __init__(self):
        self.WIDTH = 2000
        self.HEIGHT = 1500
        self.ship = Ship(self.WIDTH/2,self.HEIGHT/2);
        self.gameObjects = []
        self.gameObjects.append(self.ship)
        for i in range(20):
            self.gameObjects.append(Asteroid(random.random() * self.WIDTH, random.random() * self.HEIGHT))
        self.score = 0;

class App:
    def __init__(self):
        print("constructor")
        self.renderer = None;
        self.GameData = GameData()
        self.done = False
        self.init()

    def init(self):
        print("Game init")
        self.renderer=Renderer.VectorRenderer(self.GameData)
        if(pygame.joystick.get_count() >0):
            pygame.joystick.Joystick(0).init();
        self.done = False
        return True

    def cleanup(self):
        print("Cleanup")
        pygame.quit()

    def main(self):
        print("main-func")
        if not self.init():
            self.done = True

        while not self.done:

            delta = self.renderer.clock.tick(Renderer.FPS)/1000
            for event in pygame.event.get():
                if event.type  == pygame.QUIT:
                    self.done = True
                #self.current_screen.handleEvent(event)

            #self.current_screen.updateScreen(delta)
            self.renderer.render(self.GameData)
            #self.current_screen.renderScreen(self.screen,delta)

        self.cleanup()


#Start App
if __name__ =="__main__":
    app = App()
    app.main()