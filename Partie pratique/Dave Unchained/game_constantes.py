

# -*- coding: utf-8 -*-
import pygame, sys, random, math
from random import randint
from pygame.locals import *


pygame.init()

# definis quelques couleurs
WHITE = (255, 255, 255)
BLACK = (0,0,0)
# hauteur et largeur de l'ecran
scr_height = 650
scr_width = 1156
CharacterHeight = 48
#init horloge
clock=pygame.time.Clock()
scr=pygame.display.set_mode((scr_width,scr_height ))
# charge les images
images = pygame.image.load("images/perso.png").convert_alpha()
backgroundImage=pygame.image.load("images/fond_main_new.png").convert()
backgroundImage = pygame.transform.scale(backgroundImage,( scr_width*6, scr_height))
menu_rules_img = pygame.image.load("images/menu_rules.png").convert_alpha()
menu_rules_img = pygame.transform.scale(menu_rules_img, (scr_width,scr_height))
Gameover_Low_img = pygame.image.load("images/Gameover_low.png").convert()
Gameover_Low_img= pygame.transform.scale(Gameover_Low_img,( scr_width, scr_height))
Gameover_Medium_img = pygame.image.load("images/Gameover_Medium.png").convert()
Gameover_Medium_img = pygame.transform.scale(Gameover_Medium_img,( scr_width, scr_height))
Gameover_High_img = pygame.image.load("images/Gameover_High.png").convert()
Gameover_High_img = pygame.transform.scale(Gameover_High_img,( scr_width, scr_height))
fleche1_img = pygame.image.load("images/fleche.png").convert()
fleche1_img.set_colorkey(BLACK)
fleche1_img = pygame.transform.scale(fleche1_img, (128,64))
fleche2_img = pygame.image.load("images/fleche1.png").convert_alpha()
fleche2_img = pygame.transform.scale(fleche2_img, ( 128,64))
invincible1_img = pygame.image.load("images/invincible1.png").convert_alpha()
invincible2_img = pygame.image.load("images/invincible2.png").convert_alpha()

curseur_img = pygame.image.load("images/viseur.png").convert_alpha()
curseur_img = pygame.transform.scale(curseur_img,(16,16))
Shield_img = pygame.image.load("images/Shield.png").convert_alpha()
Shield_img = pygame.transform.scale(Shield_img,(72,72))
RoF1_img = pygame.image.load("images/RoF.png").convert_alpha()
RoF2_img = pygame.image.load("images/RoF1.png").convert_alpha()
RoF3_img = pygame.image.load("images/RoF2.png").convert_alpha()
BigBullet_img = pygame.image.load("images/BigBullet.png").convert_alpha()
SpeedUp1_img = pygame.image.load("images/SpeedUp.png").convert_alpha()
SpeedUp2_img = pygame.image.load("images/SpeedUp1.png").convert_alpha()
bossbullet1_img = pygame.image.load("images/boss_bullet_P.png").convert_alpha()
bossbullet2_img = pygame.image.load("images/boss_bullet_P1.png").convert_alpha()
bossbullet3_img = pygame.image.load("images/boss_bullet_P2.png").convert_alpha()
bossbullet4_img = pygame.image.load("images/boss_bullet_P3.png").convert_alpha()
bossbullet5_img = pygame.image.load("images/boss_bullet_P4.png").convert_alpha()
bossbullet6_img = pygame.image.load("images/boss_bullet_P5.png").convert_alpha()
bossbullet7_img = pygame.image.load("images/boss_bullet_P6.png").convert_alpha()
minotaure_right_1 = pygame.image.load("images/minotaure_right1.png")
minotaure_right_2 = pygame.image.load("images/minotaure_right2.png")
minotaure_left_1 = pygame.image.load("images/minotaure_left1.png")
minotaure_left_2 = pygame.image.load("images/minotaure_left2.png")
minotaure_init_img = pygame.image.load("images/minautore_init.png").convert_alpha()
minotaure_initright_img = pygame.transform.flip(minotaure_init_img, True, False)
Pelpe_left_img = pygame.image.load("images/Pelpe1.png").convert_alpha()
Pelpe1_left_img = pygame.image.load("images/Pelpe2.png").convert_alpha()
Pelpe2_left_img = pygame.image.load("images/Pelpe3.png").convert_alpha()
Pelpe_right_img = pygame.transform.flip(Pelpe_left_img, True, False)
Pelpe1_right_img = pygame.transform.flip(Pelpe1_left_img, True, False)
Pelpe2_right_img = pygame.transform.flip(Pelpe2_left_img, True, False)
Tear = pygame.image.load("images/Tear1.png").convert_alpha()
Tear = pygame.transform.scale(Tear,(12,12))


bullet_img = pygame.image.load("images/bullet.png").convert()
bullet_img = pygame.transform.scale(bullet_img, (7,7))
bullet_menu_img = pygame.image.load("images/bullet_menu.png").convert_alpha()
bullet_menu_img = pygame.transform.scale(bullet_menu_img,(7,7))
tadmorv1 = pygame.image.load("images/tadmorv1.png").convert_alpha()
tadmorv2 = pygame.image.load("images/tadmorv2.png").convert_alpha()
tadmorv3 = pygame.image.load("images/tadmorv3.png").convert_alpha()
tadmorv4 = pygame.image.load("images/tadmorv4.png").convert_alpha()
tadmorv5 = pygame.image.load("images/tadmorv5.png").convert_alpha()
tadmorv6 = pygame.image.load("images/tadmorv6.png").convert_alpha()
expl1_img = pygame.image.load("images/Expl1.png").convert_alpha()
expl2_img = pygame.image.load("images/Expl2.png").convert_alpha()
expl3_img = pygame.image.load("images/Expl3.png").convert_alpha()
expl4_img = pygame.image.load("images/Expl4.png").convert_alpha()
expl5_img = pygame.image.load("images/Expl5.png").convert_alpha()
expl6_img = pygame.image.load("images/Expl6.png").convert_alpha()
move_menu1_img = pygame.image.load("images/walk_ombre1.png").convert_alpha()
move_menu2_img = pygame.image.load("images/walk_ombre2.png").convert_alpha()
move_menu3_img = pygame.image.load("images/walk_ombre3.png").convert_alpha()
move_menu4_img = pygame.image.load("images/walk_ombre4.png").convert_alpha()
move_menu1_img = pygame.transform.scale(move_menu1_img,(164,164))
move_menu2_img = pygame.transform.scale(move_menu2_img,(164,164))
move_menu3_img = pygame.transform.scale(move_menu3_img, (164,164))
move_menu4_img = pygame.transform.scale(move_menu3_img, (164,164))
retrybutton = pygame.image.load("images/retrybutton.png").convert_alpha()
retrybutton = pygame.transform.scale(retrybutton, (256,80))
fond=pygame.image.load("images/fond_menu_new.png").convert()
fond = pygame.transform.scale(fond, (scr_width,scr_height))
img_intro = pygame.image.load("images/img_intro.png").convert()
img_intro = pygame.transform.scale(img_intro, (scr_width, scr_height* 5))
credits_img = pygame.image.load("images/Credits.png").convert()
credits_img = pygame.transform.scale(credits_img, (scr_width, 2876))

# init. les groupes
explosions = pygame.sprite.Group()
boss_powerups = pygame.sprite.Group()
ennemys_killed = pygame.sprite.Group()
ennemys_killed_score = pygame.sprite.Group()
ennemys_killed_oneup = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
perso_menu_group = pygame.sprite.GroupSingle()
Shield_group = pygame.sprite.GroupSingle()
ennemys = pygame.sprite.Group()
powerups = pygame.sprite.Group()
persos = pygame.sprite.GroupSingle()
ennemy_hit_list = pygame.sprite.Group()
bullets = pygame.sprite.Group()
ennemybullets = pygame.sprite.Group()
boss_group = pygame.sprite.GroupSingle()
bullets_menu = pygame.sprite.Group()

# listes et ajoute les elements correspondant
fleche_img = []
fleche_img.append(fleche1_img)
fleche_img.append(fleche2_img)

RoF_img = []
RoF_img.append(RoF1_img)
RoF_img.append(RoF2_img)
RoF_img.append(RoF3_img)

invincible_img = []
invincible_img.append(invincible1_img)
invincible_img.append(invincible2_img)

SpeedUp_img = []
SpeedUp_img.append(SpeedUp1_img)
SpeedUp_img.append(SpeedUp2_img)
bossbullet_img = []

bossbullet_img.append(bossbullet1_img)
bossbullet_img.append(bossbullet2_img)
bossbullet_img.append(bossbullet3_img)
bossbullet_img.append(bossbullet4_img)
bossbullet_img.append(bossbullet5_img)
bossbullet_img.append(bossbullet6_img)
bossbullet_img.append(bossbullet7_img)

minotaure_right = []

minotaure_right.append(minotaure_right_1)
minotaure_right.append(minotaure_right_2)
minotaure_left = []

minotaure_left.append(minotaure_left_1)
minotaure_left.append(minotaure_left_2)


Pelpe_imgs_right = []
Pelpe_imgs_right.append(Pelpe_right_img)
Pelpe_imgs_right.append(Pelpe1_right_img)
Pelpe_imgs_right.append(Pelpe2_right_img)
Pelpe_imgs_left = []
Pelpe_imgs_left.append(Pelpe_left_img)
Pelpe_imgs_left.append(Pelpe1_left_img)
Pelpe_imgs_left.append(Pelpe2_left_img)


tadmorv_img_right = []
tadmorv_img_right.append(tadmorv1)
tadmorv_img_right.append(tadmorv2)
tadmorv_img_right.append(tadmorv3)
tadmorv_img_left = []
tadmorv_img_left.append(tadmorv4)
tadmorv_img_left.append(tadmorv5)
tadmorv_img_left.append(tadmorv6)
explosion_img =[]
big_explosion_img = []

expl1_img = pygame.transform.scale(expl1_img,(64,64))
expl2_img = pygame.transform.scale(expl2_img,(64,64))
expl3_img = pygame.transform.scale(expl3_img,(64,64))
expl4_img = pygame.transform.scale(expl4_img,(64,64))
expl5_img = pygame.transform.scale(expl5_img,(64,64))
expl6_img = pygame.transform.scale(expl6_img,(64,64))

big_expl1_img = pygame.transform.scale(expl1_img,(128,128))
big_expl2_img = pygame.transform.scale(expl2_img,(128,128))
big_expl3_img = pygame.transform.scale(expl3_img,(128,128))
big_expl4_img = pygame.transform.scale(expl4_img,(128,128))
big_expl5_img = pygame.transform.scale(expl5_img,(128,128))
big_expl6_img = pygame.transform.scale(expl6_img,(128,128))

big_explosion_img.append(big_expl1_img)
big_explosion_img.append(big_expl2_img)
big_explosion_img.append(big_expl3_img)
big_explosion_img.append(big_expl4_img)
big_explosion_img.append(big_expl5_img)
big_explosion_img.append(big_expl6_img)


explosion_img.append(expl1_img)
explosion_img.append(expl2_img)
explosion_img.append(expl3_img)
explosion_img.append(expl4_img)
explosion_img.append(expl5_img)
explosion_img.append(expl6_img)

move_menu_img = []
move_menu_img.append(move_menu1_img)
move_menu_img.append(move_menu2_img)
move_menu_img.append(move_menu3_img)
move_menu_img.append(move_menu4_img)

# Liste qui contient les powerups actifs
activepowerups = []

# aires delimitees
shoot_rect_Right1 = pygame.Rect(scr_width-300, 0, scr_width, scr_height)
shoot_rect_Left1 = pygame.Rect(0, 0, 300, scr_height)

# attention range va de (a jusqu'a b-1) Pour delimiter les zones de spawn d'ennemis
numbersx1 = range(0,20)
numbersx2 = range(200,1200)
numbersx3 = range(1200,1244)
numbersx = numbersx1 + numbersx3
numbersy1 = range(0,21)
numbersy2 = range(0,31) + range(scr_height -20,scr_height)
numbersy3 = range(1200,1244)


# polices d'ecriture
police = pygame.font.SysFont("helvetica", 16)
ScoreFont = pygame.font.SysFont("helvetica", 50)
startfont = pygame.font.SysFont("helvetica", 40)
gameOverFont = pygame.font.SysFont("monospace", 60)
highscorefont = pygame.font.SysFont("helvetica", 50)
intropolice = pygame.font.SysFont("Arial", 20, True)

# sons et musiques
explosionsound = pygame.mixer.Sound("sons/explosion.wav")
intro = pygame.mixer.Sound("sons/music_intro.wav")
music_menu = pygame.mixer.Sound("sons/music_menu.wav")
death_music = pygame.mixer.Sound("sons/death_music.wav")
ennemy_hit_sound = pygame.mixer.Sound("sons/ennemy_hit_sound.wav")
powerupsound = pygame.mixer.Sound("sons/Powerup_sound.wav")
shoot_sound = pygame.mixer.Sound("sons/shoot_sound.wav")
minotaure_spawn_sound = pygame.mixer.Sound("sons/Minotaure_spawn.wav")
minotaure_hit_sound = pygame.mixer.Sound("sons/Minotaure_hit.wav")
minotaure_death_sound = pygame.mixer.Sound("sons/Minotaure_death.wav")
music_main = pygame.mixer.Sound("sons/music_main.wav")
LifeUp_sound = pygame.mixer.Sound("sons/1Up.wav")
boss_powerup = pygame.mixer.Sound("sons/boss_powerup.wav")


# init les const type integer

last_spawn = 0
last_scroll = 0
last_bosspowerup = 0
spawn_delay = 2500
last_tick = 0
tick_delay = 50
last_fleche = 0
fleche_delay = 1000
gameover = 0
last_invincibility = 0
times_scrolled = 0
afterscroll_delay = 12000
score = 0
oneup = 0
scrollcount = 0
scrolltime = 0
fleche_img_index = 0
bulletspeed = 15
level = 1
intro_delay = 45
intro_last = 0
intro_time = 0
credits_time = 0
credits_last = 0

last_SpeedUp = 0
last_BigBullet = 0
last_RoF = 0
persospeed = 10
powerupduration = 12000
boss_powerupduration = 500

# constantes type booleen
scroll = False
boss_hiteable = False
ennemyspawn = True
flechedisplay = False
invincibility = False
minotaure_alive = False
minotaure_killed = False
afterscroll = False
boss_spawn = False
powerup_spawn = True

#au lancement
menu = "intro"

time = pygame.time.get_ticks