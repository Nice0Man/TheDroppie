import pygame
import os
import random
import csv
import button


SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

FPS = 60
# define game variables
GRAVITY = 0.45
SCROLL_THRESH = 200
ROWS = 16
COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 21
MAX_LEVELS = 1
screen_scroll = 0
bg_scroll = 0
level = 0
start_game = False

# define colours
BLACK = (0, 0, 0)
BG = BLACK
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# define player action variables
moving_left = False
moving_right = False
shoot = False
grenade = False
grenade_thrown = False

