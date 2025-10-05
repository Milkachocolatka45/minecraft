from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager
from hero import Hero

class Game(ShowBase):
    def __init__ (self):
        super().__init__()
        base.camLens.setFov(90)
        land = MapManager()
        x, y = land.load_map('maps/land2.txt')
        self.hero = Hero((x // 2, y // 2, 1), land)

        start_snd = base.loader.loadSfx("sounds/background-music-405227.mp3")
        start_snd.set_volume(0.2)
        start_snd .set_loop(True)
        start_snd.play()
    
game = Game()
game.run()