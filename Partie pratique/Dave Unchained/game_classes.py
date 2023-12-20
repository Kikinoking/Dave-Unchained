import pygame, sys, random, math
from pygame.locals import *
from game_constantes import*
from random import randint


# classe speciale pour l'animation du menu principal
class Perso_menu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
#coorodonnees de depart
        self.x = -100
        self.y = scr_height -163
# index et images
        self.index = 0
        self.image = move_menu_img[self.index]
        self.rect =self.image.get_rect()
# pour tirer
        self.shoot_delay = 400
        self.last_shot = pygame.time.get_ticks()

# delai entre chaque animation + timer
# meme temps utilise comme delai entre chaque deplacement
        self.animation_time = 10/3
        self.current_time = 0

# affiche son image et fait son animation + son deplacement
    def display(self):
        self.images = move_menu_img
        self.image = move_menu_img[self.index]
        self.rect = self.image.get_rect()
        now = pygame.time.get_ticks()
        self.current_time +=1
# check si il doit changer d'animation et se deplacer
        if self.current_time >= self.animation_time:
                self.current_time = 0
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]
                self.x +=3
# si il atteint le bord de l'ecran, reprend au debut
                if self.x > scr_width -10:
                    self.x = -100
        scr.blit(self.image,(self.x,self.y))
    def shoot(self):
# la balle apparait au bon endroit
        now = pygame.time.get_ticks()
# check si le delai de tir est depasse; le cas echeant cree une balle  et l'ajoute e la liste des balles
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet_menu = Bullet_menu()
            bullet_menu.add(bullets_menu)
            shoot_sound.play()

    def update(self):
        self.display()

# classe pour les balles tirees dans le menu
class Bullet_menu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
# position en fonction de mon perso
        for perso_menu in perso_menu_group:
            self.x = perso_menu.x + perso_menu.image.get_width()/2 + 7
            self.y = perso_menu.y + 43
        self.speedx = bulletspeed
        self.image = bullet_menu_img
        self.image.set_colorkey(WHITE)

    def move(self):
#se deplace horizontalement
        self.x += bulletspeed
    def display(self):
        scr.blit(self.image, (self.x,self.y))
    def update(self):
        self.move()
        self.display()
        if self.x > scr_width:
            self.kill()
# classe pour gerer les explosions de mes ennemis
class Explosion(pygame.sprite.Sprite):
# prends 2 parametres a l'initialisation: la position x et y de l'ennemi ou le boss tue
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
#duree qu'il reste avant de disparaitre de l'ecran
        self.timeleft = 16
# temps entre chaque animation
        self.animation_time = 23/6
# timer et index de base
        self.current_time = 0
        self.index = 0
# controle si il est encore en vie, sinon, le detruit
    def timebomb(self):
        self.timeleft -= 1
        if self.timeleft == 0:
            self.kill()

# pour son affichage
    def display(self):
#dictionnaire de ses frames
        self.images = explosion_img
        self.image = explosion_img[self.index]
        now = pygame.time.get_ticks()
        self.current_time +=1
# regarde si il doit changer son animation; principe analogue comme plus haut ou plus bas
        if self.current_time >= self.animation_time:
                self.current_time = 0
                self.index = (self.index + 1) % len(self.images)
# defini son image en fonction de son index
                self.image = self.images[self.index]
#oblitere son image
        scr.blit(self.image,(self.x,self.y))
    def update(self):
        self.timebomb()
        self.display()



# classe speciale pour l'explosion du boss, idem a Explosion, juste plus grande


class BigExplosion(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.timeleft = 22
        self.animation_time = 25/6
        self.current_time = 0
        self.index = 0
    def timebomb(self):
        self.timeleft -= 1
        if self.timeleft == 0:
            self.kill()
    def display(self):
# seule difference avec Explosion
        self.images = big_explosion_img
        self.image = big_explosion_img[self.index]
        now = pygame.time.get_ticks()
        self.current_time +=1
        if self.current_time >= self.animation_time:
                self.current_time = 0
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]
        scr.blit(self.image,(self.x,self.y))
    def update(self):
        self.timebomb()
        self.display()


# Powerup special pour tuer le boss
class BossPowerup(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
# choisi au hasard une position d'apparition
        self.x = random.choice(range(10, scr_width - 50))
        if self.x < 190 or self.x > scr_width -170:
# y en fonction de mes coins innateignables
            self.y = random.choice(range(200, scr_height-190))
        else: self.y = random.choice(range(50,scr_height - 150))
# temps restant avant de disparaitre de l'ecran si pas pris
        self.timeleft = 200
# pour les collisions
        self.rect = pygame.Rect((self.x, self.y, 64, 64))
# memes roles que plus haut
        self.animation_time = 5
        self.current_time = 0
        self.index = 0
# defini son attribut buff, afin de savoir ce qu'il fait concretement
        self.buff = 'bosspowerup'
# verifie si il est encore en vie, sinon, le tue
    def timebomb(self):
        self.timeleft-=1
        if self.timeleft == 0:
            self.remove(boss_powerups)
# oblitere son image et l'anime
    def display(self):
        self.images = bossbullet_img
        self.image = bossbullet_img[self.index]

        now= pygame.time.get_ticks()
        self.current_time += 1
        if self.current_time >= self.animation_time:
                self.current_time = 0
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]
        scr.blit(self.image,(self.x,self.y))

    def update(self):

            self.timebomb()
            self.display()

# Powerups
class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
# choisi une coorodonnee horizontale d'apparition au hasard tenant compte de mes coins innateignables
        self.x = random.choice(range(10, scr_width - 50))
# defini sa position au hasard en y en fonction de la position en x choisie
        if self.x < 190 or self.x > scr_width -170:
            self.y = random.choice(range(200, scr_height-230))
        else: self.y = random.choice(range(50,scr_height - 150))
# choisi un type de powerup aleatoirement
        self.buff = random.choice(['RoF','SpeedUp','invincibility','BigBullet',])
# temps avant la disparition sur l'ecran
        self.timeleft = 200
# rectangle pour les collisions
        self.rect = pygame.Rect((self.x, self.y, 64, 64))
# temps entre chaque frame , timer et index d'animation de base
        self.animation_time = 5
        self.current_time = 0
        self.index = 0

# verifie si il meurt ou non
    def timebomb(self):
        self.timeleft-=1
        if self.timeleft == 0:
            self.remove(powerups)
# affiche son image animee en fonction de son buff
    def display(self):
# buff 1: tire plus vite
        if self.buff == 'RoF':
            self.images = RoF_img
            self.image = RoF_img[self.index]
            now= pygame.time.get_ticks()
            self.current_time += 1
            if self.current_time >= self.animation_time:
                self.current_time = 0
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]
# buff 2: vitesse du personnage accrue
        if self.buff == 'SpeedUp':
            self.images = SpeedUp_img
            self.image = SpeedUp_img[self.index]

            self.current_time += 1
            if self.current_time >= self.animation_time:
                self.current_time = 0
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]
# buff 3: invincibilite
        if self.buff == 'invincibility':
            self.images = invincible_img
            self.image = invincible_img[self.index]

            self.current_time += 1
            if self.current_time >= self.animation_time:
                self.current_time = 0
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]



# buff 4: des balles plus grosses
        if self.buff == 'BigBullet':
            self.image = BigBullet_img

# oblitere l'image correspondante a sa position
        scr.blit(self.image,(self.x,self.y))




    def update(self):
        if powerups.has(self):
            self.timebomb()
            self.display()


        else: pass








