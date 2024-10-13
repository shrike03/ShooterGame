# __init__.py
# file combines the various modules of the package into a single namespace, allowing for easier access to the package's components.
import pygame
import sys
import random
from math import floor
from pathlib import Path
from .Background import Background
from .Button import Button
from .Collision_Object import Object
from .Counting import Counting
from .Physics import Physics
from .Shooting import Shoot
from .Player import Player
from .Target import Target
