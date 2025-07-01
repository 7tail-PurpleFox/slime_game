import pygame
from . import tool
import sys
import os

def get_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.normpath(os.path.join(base_path, relative_path))

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Slime Vs Dragon")
pygame.display.set_icon(pygame.image.load(get_path("./resource/image/slime.png")))
pygame.mixer.music.load(get_path("./resource/bgm/Cutie 8bit.mp3"))
screen.fill((0,0,0))
fonts_36=tool.load_font(get_path("./resource/font"), 36)
img_list=tool.load_image(get_path("./resource/image"))
forest_img = img_list["forest"]
slime_imgs = [img_list["slime-"+str(i)] for i in range(1,6)]
dragon_imgs = [img_list["dragon-"+str(i)] for i in range(1,5)]
explode_imgs = [img_list["explode-"+str(i)] for i in range(1,9)]
sound_list = tool.load_sound(get_path("./resource/sound"))