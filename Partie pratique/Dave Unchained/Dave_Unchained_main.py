

# -*- coding: utf-8 -*-
import pygame, sys, random, math
from random import randint
from pygame.locals import *
from game_constantes import*
from game_classes import*

pygame.init()
pygame.mixer.init(48000, -16, 1, 1024)


#Ces classes sont declarees ici car leur deplacement depend de perso.x et perso.y, qui ne sont pas constants (mis a jour dans ce module)
class Perso(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


# Dictionnaire de mes images en fonction de la direction
        self.image={K_DOWN:[images.subsurface(x,128,64,64) for x in range(0,192,64)],
                    K_LEFT:[images.subsurface(x,0,64,64) for x in range(0,192,64)],
                    K_RIGHT:[images.subsurface(x,64,64,64) for x in range(0,192,64)],
                    K_UP:[images.subsurface(x,192,64,64) for x in range(0,192,64)],
                    }






# delai entre chaque tir
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
# coordonees de depart au centre de l'ecran
        self.x = scr_width/2 -32
        self.y = scr_height/2 -32
# direction et index de depart
        self.index_img = 1
        self.direction = K_DOWN
# surface initiale
        self.surface = self.image[self.direction][self.index_img]

# vies de depart

        self.lives = 3
# rectangle et masque initial pour les collisions
        self.rect = pygame.Rect(self.x, self.y, 64, 64)
        self.mask = pygame.mask.from_surface(self.surface)


#oblitere l'image a l'initialisation
        scr.blit(self.image[self.direction][self.index_img],(self.x,self.y))

        pygame.display.update()
# obtiens le mask en fonction de la direction et de son index
    def get_mask(self):
        self.surface = self.image[self.direction][self.index_img]
        #cree un masque a partir de la surface corresp. pour collide avec ennemis

        self.mask = pygame.mask.from_surface(self.surface)
        #rect pour collide avec powerups
        self.rect = pygame.Rect(self.x+ 10,self.y+10,44,44)



# pour se deplacer
    def move(self):
     pressed_keys = pygame.key.get_pressed()
# Si l'ecran scroll, bouge pas
     if scroll == True:
        pass
     else:
        if pressed_keys[K_RIGHT] and self.x<=scr_width - 64:
# je definis des carres aux coins ou mon perso ne va pas
            if self.x >= scr_width -190 and self.y <= 180:

                    pass
            elif self.x >= scr_width -370 and self.y >= scr_height -170:
                pass
            else:
# mon perso regarde a droite
                self.direction = K_RIGHT
# retourne les 3 imgs successivement
                self.index_img = (self.index_img+1)%3
# deplacement horizontal vers droite
                self.x += persospeed
        if pressed_keys[K_LEFT] and self.x>=0:
            if self.x<= 205 and self.y <= 90:
                pass
            elif self.x <= 210 and self.y >= scr_height -260:
                pass
            else:
# mon perso regarde a gauche
                self.direction = K_LEFT
                self.index_img = (self.index_img+1)%3
# mon perso se deplace horizontalement vers la gauche
                self.x -= persospeed
        if pressed_keys[K_UP] and self.y>=0:
            if self.x <= 200 and self.y <= 90 :
                pass
            elif self.x >= scr_width -180 and self.y <= 180:
                pass
            else:
# mon perso regarde en haut
                self.direction = K_UP
                self.index_img = (self.index_img+1)%3
# deplacement vertical vers le haut
                self.y -= persospeed
        if pressed_keys[K_DOWN] and self.y<=scr_height - 64 :
            if self.x <= 210 and self.y >= scr_height - 260:
                pass
            elif self.x >= scr_width - 370 and self.y >= scr_height - 180 :
                pass
            else:
# perso regarde en bas
                self.direction = K_DOWN
                self.index_img = (self.index_img+1)%3
# deplacement vertical vers le bas
                self.y += persospeed

# si pas de touche pressee, alors on definit la direction avec le curseur de la souris
        else:


# retourne la position horizontale de la souris
            mousex = pygame.mouse.get_pos()[0]
# retourne la position verticale de la souris
            mousey = pygame.mouse.get_pos()[1]
            angle = math.degrees(math.atan2(mousey- self.y, mousex- self.x))
# calcule du vecteur entre mon perso et le curseur souris avec l'horizontale, puis le convertis en degres
# !!! retourne un angle entre -pi/2 et pi/2 !!!


# en fonction de la position de la souris, le perso regarde dans la direction assignee
            if -45>= angle >= -135:
# regarde en haut
                self.direction = K_UP

            if -180 < angle < -135 :
# regarde a gauche
                self.direction = K_LEFT

            if 180> angle >=    135:
# regarde aussi a gauche car math.hyp retourne entre -pi/2 et pi/2
                self.direction = K_LEFT

            if 135 > angle >= 45:
# regarde en bas
                self.direction = K_DOWN

            if 0 >= angle > -45 :
# regarde a droite
                self.direction = K_RIGHT
            if 45 > angle > 0:
# similaire a K_LEFT
                self.direction = K_RIGHT




#oblitere mon image sur l'ecran en fonction de sa direction et de son index
    def display(self):

        scr.blit(self.image[self.direction][self.index_img],(self.x,self.y))
# pour tirer
    def shoot(self):

# pour dire ou la balle va tirer
        if self.direction == K_UP:
            self.bulletx = float(self.x + CharacterHeight/2 -5)
            self.bullety = float(self.y)
        if self.direction == K_DOWN:
            self.bulletx = float(self.x + CharacterHeight -5)
            self.bullety =float( self.y + CharacterHeight)
        if self.direction == K_LEFT:
            self.bulletx = float(self.x)
            self.bullety = float(self.y + CharacterHeight/2 + 15)
        if self.direction == K_RIGHT:
            self.bulletx = float(self.x + CharacterHeight)
            self.bullety = float(self.y + CharacterHeight/2 + 15)
# la balle apparait au bon endroit
        now = pygame.time.get_ticks()
# check si le delai de tir est depasse; le cas echeant cree une balle  et l'ajoute e la liste des balles
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
#si j'ai le powerup pour tuer le boss, le 3e argument est sur true et la balle peut faire des dommages au boss
            if boss_hiteable == True:
                bullet = Bullet(self.bulletx, self.bullety, True)

            else:
                bullet = Bullet(self.bulletx ,  self.bullety, False)

            all_sprites.add(bullet)

            bullets.add(bullet)
# joue le son de tir
            shoot_sound.play()






# verfifie si il y a des collisions
    def checkcollision(self):

     if invincibility == False:
       for ennemy in ennemys:

#collision avec les ennemis en fonction du masque
            if pygame.sprite.collide_mask(self,ennemy):

                    pygame.sprite.Group.empty(ennemys)


# joue le son de mort et repositionne mon personnage au centre de l'ecran
                    explosionsound.play()
                    self.x = scr_width/2-32
                    self.y = scr_height/2 -32
# vide tous les groupes
                    ennemybullets.empty()
                    pygame.sprite.Group.empty(bullets)
                    pygame.sprite.Group.empty(all_sprites)
                    pygame.sprite.Group.empty(explosions)
                    powerups.empty()

# si je meurs, le compteur de vie bonus repart a 0
                    oneup = 0
# attends quelques secondes avant de reprendre
                    pygame.time.wait(500)
# je perds une vie
                    self.lives -= 1
# gere les collisions avec le boss, similaire aux ennemis
       for boss in boss_group:
            if pygame.sprite.collide_mask(self,boss):

                    boss_group.empty()

                     # je perds une vie
                    explosionsound.play()
                    self.lives -= 1
                    self.x = scr_width/2 -32
                    self.y = scr_height/2 -32
                    boss_group.empty()
                    if not self.lives == 0:
                        boss_spawn = True
                    ennemybullets.empty()
                    pygame.sprite.Group.empty(ennemys)
                    pygame.sprite.Group.empty(bullets)
                    pygame.sprite.Group.empty(all_sprites)
                    pygame.sprite.Group.empty(explosions)



                    powerups.empty()
                    boss_powerups.empty()
# si je meurs, le compteur de vie bonus repart a 0
                    oneup = 0



                    pygame.time.wait(500)
# collisions avec les balles tirees par les ennemis
       if pygame.sprite.spritecollideany(self, ennemybullets, pygame.sprite.collide_mask):
                 pygame.sprite.Group.empty(ennemys)

                 ennemybullets.empty()

                 self.lives -= 1
# joue le son de mort et repositionne mon personnage au centre de l'ecran
                 explosionsound.play()
                 self.x = scr_width/2-32
                 self.y = scr_height/2 -32
# vide tous les groupes

                 pygame.sprite.Group.empty(bullets)
                 pygame.sprite.Group.empty(ennemybullets)

                 pygame.sprite.Group.empty(all_sprites)
                 pygame.sprite.Group.empty(explosions)
                 powerups.empty()
# si je meurs, le compteur de vie bonus repart a 0
                 oneup = 0
# attends quelques secondes avant de reprendre
                 pygame.time.wait(500)
                 if minotaure_alive == True:
                    boss_group.empty()
                    boss = Boss()
                    boss_group.add(boss)
                    minotaure_spawn_sound.play()


# collisions si j'ai un bouclier
     elif invincibility == True:

# si les ennemis me touchent, ils meurent instantanement, mais pas les boss
            for ennemy in ennemys:
                if pygame.sprite.collide_mask(self,ennemy):
                    explosion = Explosion(ennemy.x, ennemy.y)
                    explosion.add(explosions)
                    ennemy_hit_sound.play()

                    ennemy.kill()
# le boss ne bouge plus
            for boss in boss_group:
                if pygame.sprite.collide_mask(self,boss):
                    boss.speedx = 0
                    boss.speedy = 0
            for ennemybullet in ennemybullets:
                if pygame.sprite.collide_mask(self, ennemybullet):
                    ennemybullet.kill()
# appelle mes methodes les unes apres les autres
# Nota bene: la fonction update peut etre appelee par un groupe et, des lors elle appelle la methode update de chaqu'un des sprites dans celle-ci
    def update(self):


        self.move()
        self.get_mask()
        self.display()








        self.checkcollision()


## CLASSE SIMILAIRE A BULLET
class Ennemybullet(pygame.sprite.Sprite):
# parametre position et gauche/droite en booleen
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = Tear

# rect pour les collisions
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = 15
        self.norme = math.sqrt(math.pow(perso.x - self.x,2) + math.pow(perso.y - self.y,2))
# defini sa vitesse pour se deplacer ainsi que sa direction
        self.speedx =(perso.x - self.x)/ self.norme*self.speed
        self.speedy = (perso.y - self.y)/self.norme*self.speed

        self.rect.topleft =self.x,self.y



 # obtiens un masque pour les collisions
        self.mask = pygame.mask.from_surface(self.image)




# met a jour sa position chaque balle individuellement
    def update(self):


        # elle se deplace en x et y en fonction de speedy et speedx
        self.y += self.speedy
        self.x += self.speedx


        scr.blit(self.image, (self.x, self.y))


# tue le sprite si il arrive dans les bordures de l'ecran
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.bottom > scr_height:
            self.kill()
        if self.rect.centerx <0:
            self.kill()
        if self.rect.centerx > scr_width:
            self.kill()
#chaque balle est tuee si collision avec un perso
        for perso in persos:

            if pygame.sprite.collide_mask(self, perso):
                self.kill()
        # si l'ecran scroll, ils ne disparaissent
        if scroll == True:

            self.kill()
# indispensable pour les collisions
        self.rect.topleft = self.x, self.y








# mes ennemis
class Ennemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
# vu que j'ai 4 zones, d'apparition, la je choisi si ils arrivent d'en haut et d'en bas ou de cote
# randint = random integer entre 0 et 1
        self.choice = randint(0,1)
        if self.choice == 0:
# choisi une position au hasard parmi numbersx
            self.x = random.choice(numbersx)
        elif self.choice == 1:
# choisi une position au hasard parmi numbersx2
            self.x = random.choice(numbersx2)
# son image de base
        self.image = tadmorv1
        self.image.set_colorkey(BLACK)
        self.index = 0
# son rectangle et son masque de base
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
# utile pour son animation
    #le timer commence a 0
        self.current_time = 0
    # le temps que chaque frame d'animation dure
        self.animation_time = 5
# ses vies sont en fonction du niveau
        if level == 1 or level == 2:
            self.lives = 1
        else: self.lives = level -1
# utile pour definir le decoupage de sa barre de vie
        self.max_life = self.lives
# choisi sa position en y en fonction de sa position en x choisie
        if self.x in numbersx1:
            self.y = randint(30,720)
        if self.x in numbersx2:
            self.y = random.choice(numbersy2)
        if self.x in numbersx3:
            self.y = randint(30, 720)
        self.ennemyspeed = 6 + level/2.5

# pour qu'il se deplacent
    def move(self):
# si l'ecran scroll, ils ne bougent pas
        if scroll == True:

            pass
        else:
# sinon, calcule la norme du vecteur entre le personnage et l'ennemi
            norme = math.sqrt(math.pow(perso.x - self.x,2) + math.pow(perso.y - self.y,2))
# defini sa vitesse pour se deplacer ainsi que sa direction
            self.speedx =(perso.x - self.x)/ norme*self.ennemyspeed
            self.speedy = (perso.y - self.y)/norme*self.ennemyspeed
# il se deplace
            self.x = self.x + self.speedx
            self.y = self.y + self.speedy
# methode pour l'afficher
    def display(self):
# choisi si il doit regarder a droite ou a gauche
      if self.speedx > 0:
# regarde a gauche
# ses images sont le dictionnaires tadmorv_img_left
         self.images = tadmorv_img_left
         self.image = tadmorv_img_left[self.index]
# timer incremente de 1
         self.current_time += 1
# determine si l'image d'animation change
         if self.current_time >= self.animation_time:
# reinitialise le timer
                self.current_time = 0
# effectue un modula afin de faire bouger les images qui composent l'animation en boucle (role de l'index)
                self.index = (self.index + 1) % len(self.images)

                self.image = self.images[self.index]

      if self.speedx <= 0:
# regarde a droite
            self.images = tadmorv_img_right
            self.image = tadmorv_img_right[self.index]

            self.current_time += 1
# determine si l'image d'animation change
            if self.current_time >= self.animation_time:
# reinitialise le timer
                self.current_time = 0
# effectue un modulo afin de faire bouger les images qui composent l'animation en boucle
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]
# finalement, oblitere l'image correspondante
      scr.blit(self.image,(self.x,self.y))


# affiche la barre de vie (seulement si le niveau est sup. a 1)
    def lifedisplay(self):
        if level > 2:
# si il a ses vies max, dessine un rectangle plein
            if self.lives == self.max_life:
                pygame.draw.rect(scr,(255,0,0), (self.x + 18 , self.y -15, 32,10),0)
            else:
# dessine un rectangle au de remplissage au prorata de ses vies actuelles et de ses vies max.
                pygame.draw.rect(scr,(255,0,0), (self.x + 18 , self.y -15, 31*self.lives/ self.max_life,10), 0)


# rectangle de contour
            pygame.draw.rect(scr,(0,0,0), (self.x + 16 , self.y -15, 32,10), 2)

# verifie si il meurt ou non
    def checklives(self):
        if self.lives <= 0:
# utile respectivement pour le compteur afin de scroller, le score et le compteur de vie bonus
            self.add(ennemys_killed)
            self.add(ennemys_killed_score)
            self.add(ennemys_killed_oneup)
# si il meurt, il explose
            explosion = Explosion(self.x, self.y)
            explosion.add(explosions)
#le retire de la liste des ennemis
            ennemys.remove(self)

#verifie les collisions
    def checkcollision(self):
        for bullet in bullets:
# collisions avec un masque, le cas echeant, la balle disparait
                    if pygame.sprite.collide_mask(self,bullet):
                        bullet.kill()
# il perd une vie
                        self.lives -= 1
# joue le son du degat
                        ennemy_hit_sound.play()

# masque pour les collisions
    def get_mask(self):

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.Rect(self.x+ 10,self.y+10,44,44)





# appelle chaque methode
    def update(self):
        self.move()

        self.display()

        self.get_mask()
        self.checkcollision()
        self.lifedisplay()
        self.checklives()

## Classe similaire a ennemys
class Pelpe(pygame.sprite.Sprite):
     def __init__(self):
        pygame.sprite.Sprite.__init__(self)
# idem a ennemys
        self.choice = randint(0,1)
        if self.choice == 0:
# choisi une position au hasard parmi numbersx
            self.x = random.choice(numbersx)
        elif self.choice == 1:
# choisi une position au hasard parmi numbersx2
            self.x = random.choice(numbersx2)
# son image de base
        self.image = Pelpe1_left_img
        self.image.set_colorkey(BLACK)
        self.index = 0
# son rectangle et son masque de base
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
# pour qu'il tire
        self.shoot_delay = 60
        self.shoot_time = 0
# utile pour son animation
    #le timer commence a 0
        self.current_time = 0
    # le temps que chaque frame d'animation dure
        self.animation_time = 5
# ses vies sont en fonction du niveau
        self.lives = 3
# utile pour definir le decoupage de sa barre de vie
        self.max_life = self.lives
# choisi sa position en y en fonction de sa position en x choisie
        if self.x in numbersx1:
            self.y = randint(30,720)
        if self.x in numbersx2:
            self.y = random.choice(numbersy2)
        if self.x in numbersx3:
            self.y = randint(30, 720)
        self.ennemyspeed = 3 + level/1.5
     def move(self):
# si l'ecran scroll, ils ne bougent pas
        if scroll == True:

            pass
        else:
# sinon, calcule la norme du vecteur entre le personnage et l'ennemi
            norme = math.sqrt(math.pow(perso.x - self.x,2) + math.pow(perso.y - self.y,2))
# defini sa vitesse pour se deplacer ainsi que sa direction
            self.speedx =(perso.x - self.x)/ norme*self.ennemyspeed
            self.speedy = (perso.y - self.y)/norme*self.ennemyspeed
# il se deplace
            self.x = self.x + self.speedx
            self.y = self.y + self.speedy

     def display(self):
# choisi si il doit regarder a droite ou a gauche
      if self.speedx < 0:
# regarde a gauche
# ses images sont le dictionnaires tadmorv_img_left
         self.images = Pelpe_imgs_left
         self.image = Pelpe_imgs_left[self.index]
# timer incremente de 1
         self.current_time += 1
# determine si l'image d'animation change
         if self.current_time >= self.animation_time:
# reinitialise le timer
                self.current_time = 0
# effectue un modula afin de faire bouger les images qui composent l'animation en boucle (role de l'index)
                self.index = (self.index + 1) % len(self.images)

                self.image = self.images[self.index]

      if self.speedx >= 0:
# regarde a droite
            self.images = Pelpe_imgs_right
            self.image = Pelpe_imgs_right[self.index]

            self.current_time += 1
# determine si l'image d'animation change
            if self.current_time >= self.animation_time:
# reinitialise le timer
                self.current_time = 0
# effectue un modulo afin de faire bouger les images qui composent l'animation en boucle
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]
# finalement, oblitere l'image correspondante
      scr.blit(self.image,(self.x,self.y))

     def lifedisplay(self):

# si il a ses vies max, dessine un rectangle plein
            if self.lives == self.max_life:
                pygame.draw.rect(scr,(255,0,0), (self.x + 8 , self.y -12, 47,10),0)
            else:
# dessine un rectangle au de remplissage au prorata de ses vies actuelles et de ses vies max.
                pygame.draw.rect(scr,(255,0,0), (self.x + 8 , self.y -12, 47*self.lives/ self.max_life,10), 0)


# rectangle de contour
            pygame.draw.rect(scr,(0,0,0), (self.x + 8 , self.y -12, 48,10), 2)

# verifie si il meurt ou non
     def checklives(self):
        if self.lives <= 0:
# utile respectivement pour le compteur afin de scroller, le score et le compteur de vie bonus
            self.add(ennemys_killed)
            self.add(ennemys_killed_score)
            self.add(ennemys_killed_oneup)
# si il meurt, il explose
            explosion = Explosion(self.x, self.y)
            explosion.add(explosions)
#le retire de la liste des ennemis
            ennemys.remove(self)

#verifie les collisions

     def checkcollision(self):
        for bullet in bullets:
# collisions avec un masque, le cas echeant, la balle disparait
                    if pygame.sprite.collide_mask(self,bullet):
                        bullet.kill()
# il perd une vie
                        self.lives -= 1
# joue le son du degat
                        ennemy_hit_sound.play()

# masque pour les collisions
     def get_mask(self):

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.Rect(self.x+ 10,self.y+10,44,44)

## Different de la classe Ennemy
     def shoot(self):
        if self.shoot_time > self.shoot_delay:
            self.shoot_time = 0

            ennemybullet = Ennemybullet(self.x + 20, self.y + 10)
            ennemybullet.add(ennemybullets)

        else: self.shoot_time += 1


# appelle chaque methode
     def update(self):
        self.move()

        self.display()

        self.get_mask()
        self.checkcollision()
        self.lifedisplay()
        self.checklives()
        self.shoot()

# ennemi special de type boss, la plupart des attributs sont les memes que pour les autres classes
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.index = 0
        self.image = minotaure_init_img
        self.rect = self.image.get_rect()
        self.current_time = 0
        self.index = 0
# delai entre chaque animation
        self.animation_time = 3
# positions de depart
        self.x = scr_width-150
        self.y = scr_height/2 -64
# variables pour le deplacement
        self.bossspeed =  29 + level
        self.chargedelay = 1800
        self.last_charge = 0
        self.charge_counter = 0
        self.moving = False
        self.prep = False
        self.preptime = 200
# vitesses de base
        self.speedx = 0
        self.speedy = 0
# si il est dans une bordure de l'ecran
        self.border = False




# ses vies de bases sont 10 * le niveau de difficulte actuel
        self.start_lives = 5  + 5* level
# defini ses vies de depart pour l'affichage de la barre de vie
        self.lives = self.start_lives
# masque pour les collisions
        self.mask = pygame.mask.from_surface(self.image)
# timer pour determiner le temps depuis quand il est apparu
        self.time_spawn = 0
# facteur qui multiplie les vecteurs de deplacement; dependent du niveau et utiles pour le faire bouger






    def get_direction(self):
# calcule la norme du vecteur entre lui et le personnage (analogue au mouvement des ennemis)
            norme = math.sqrt(math.pow(perso.x - self.x,2) + math.pow(perso.y - self.y,2))
            self.speedx =(perso.x - self.x)/ norme*self.bossspeed
            self.speedy = (perso.y - self.y)/norme*self.bossspeed
            self.last_charge = pygame.time.get_ticks()
# son deplacement
    def move(self):
# si il est apparu moins depuis - de 60 ticks, il ne bouge pas
        if self.time_spawn < 60:

                pass
# si il a fini son deplacement, il s'arrete
        if self.charge_counter == 30:
                self.moving = False
                self.animation_time = 3
# pour eviter qu'il sorte des bordures
        else:
                if  self.x < 0:
                    self.x =0
                    self.charge_counter += 5
                    self.border = True
                if self.x > scr_width-110:
                    self.border = True
                    self.x = scr_width-128
                    self.charge_counter += 5

                if self.y < 0:
                    self.y = 0
                    self.charge_counter += 5
                    self.border = True
                if self.y > scr_height - 140:
                    self.y = scr_height -141
                    self.charge_counter += 5
                    self.border = True

# l'animation ou il se prepare a charger
                else:
                    self.do_explosion = False
                    if self.charge_counter < 10:
                        self.border = False
                        self.animation_time = 6
                        self.x = self.x - self.speedx/ 30
                        self.y = self.y - self.speedy/30
                        self.charge_counter = self.charge_counter + 1
# la charge
                    elif self.charge_counter < 30:
                        self.border = False
                        self.animation_time = 3
                        self.x = self.x + self.speedx
                        self.y = self.y + self.speedy
                        self.charge_counter = self.charge_counter + 1

# son affichage
    def display(self):
# si il vient d'apparaitre, affiche son image d'apparition
      if self.time_spawn < 60:
          self.image = minotaure_init_img
          self.time_spawn += 1
# si il n'est pas en deplacement, regarde vers mon perso

      elif  self.moving == False or self.border == True:

        for perso in persos:
          if self.x - perso.x > 0:

            self.image = minotaure_init_img
          if self.x -perso.x < 0:
            self.image = minotaure_initright_img

      else:
# verifie si il doit regarder a gauche ou a droite
       if self.speedx < 0:
# regarde a gauche et gere son animation
         self.images = minotaure_left
         self.image = minotaure_left[self.index]

         self.current_time += 1
         if self.current_time >= self.animation_time:
                self.current_time = 0
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]
# regarde a droite et gere son animation
       if self.speedx >= 0:
            self.images = minotaure_right
            self.image = minotaure_right[self.index]

            self.current_time += 1
            if self.current_time >= self.animation_time:
                self.current_time = 0
                self.index = (self.index + 1) % len(self.images)
                self.image = self.images[self.index]






# oblitere sur l'ecran
      scr.blit(self.image,(self.x,self.y))

# masque pour les collisions
    def get_mask(self):
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.Rect( self.x + 10, self.y +10, 108,108)

# pour afficher sa barre de vie
    def lifedisplay(self):

# algorithme analogue a celui des ennemis; la barre de vie est juste plus longue
            if self.lives == self.start_lives:
                pygame.draw.rect(scr,(255,0,0), (self.x + 32 , self.y -15, 64,10),0)
            else:
                pygame.draw.rect(scr,(255,0,0), (self.x + 32 , self.y -15, 64*self.lives/ self.start_lives,10), 0)



            pygame.draw.rect(scr,(0,0,0), (self.x + 32 , self.y -15, 64,10), 2)

# verifie les collisions
    def checkcollision(self):
# si il vient d'apparaitre, ne fait rien
        if self.time_spawn < 65:
            self.time_spawn += 1
            pass
        else:
# si la balle qui le touche a sa valeur booleene sur True, alors il prend des degats
             for bullet in bullets:

                if bullet.bosskill == True:
                    if pygame.sprite.collide_mask(self,bullet):
# il perd une vie
                        self.lives -= 1
                        minotaure_hit_sound.play()

                else:

# sinon, il crie juste
                        if pygame.sprite.collide_mask(self,bullet):
                            minotaure_hit_sound.play()



# appelle les methodes une a une
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_charge > self.chargedelay:
            if self.time_spawn < 60:
                self.moving = False

                pass
            else:
                self.get_direction()
                self.charge_counter = 0
                self.moving = True





        self.move()

        self.display()
        self.lifedisplay()
        self.get_mask()
        self.checkcollision()




# classe pour le bouclier quand on attrape le powerup invincibility
class Shield(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = Shield_img
# defini sa position de depart en fonction de la position du perso
        self.x = perso.x -4
        self.y = perso.y -4
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
# rend son image legerement transparente
        self.image.set_alpha(30)


# methode pour actualiser son affichage
    def display(self):

# sa position est dependante de celle du personnage
        self.x = perso.x -4
        self.y = perso.y -4
# oblitere l'image au bon endroit
        scr.blit(self.image,(self.x,self.y))



    def update(self):
        self.display()




## Depend du personnage pour l'attribut bosskill
# classe pour les balles tirees par le personnage
class Bullet(pygame.sprite.Sprite):
# chaque balle prend 3 parametres a l'initialisation: position en x, en y et si elle inflige des degats au boss ou non (boolean)
    def __init__(self, x, y, bosskill):
        pygame.sprite.Sprite.__init__(self)
# je definis si elle doit infliger des degats au(x) boss ou non
        self.bosskill = bosskill
# definis son image speciale si le powerup bosspowerup est actif
        if self.bosskill == True :
            boss_bullet_img = pygame.image.load('images/boss_bullet.png').convert_alpha()
            boss_bullet_img = pygame.transform.scale(boss_bullet_img,(10,10))
            self.image = boss_bullet_img
# sinon image standart
        else:
            self.image = bullet_img
# colorkey rend les pixels de l'image en parametre transparents
            self.image.set_colorkey(WHITE)
# rect pour les collisions
        self.rect = self.image.get_rect()
# reprends les coordonnees et les stocke
        self.x = float(x)
        self.y = float(y)
# utile pour determiner le vecteur de base entre ma souris et l'endroit ou elle apparait; pour son deplacement
        self.start_posx = x
        self.start_posy = y



 # place la balle en fonction de la position du joueur
        self.rect.bottom = y
        self.rect.centerx = x
 # obtiens un masque pour les collisions
        self.mask = pygame.mask.from_surface(self.image)
 # obtiens les coordonnees du curseur
        mouse_x =pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]

# defini la vitesse en x et en y en fonction de la position du personnage et de la souris, essentiel pour deplacer chaque balle
        self.speedx = bulletspeed* (mouse_x -self.start_posx) /math.hypot(mouse_x - self.start_posx, mouse_y - self.start_posy)##float(bulletspeed* (mouse_x -self.x) / ((mouse_x-self.x)**2+(mouse_y-self.y)**2)**0.5)
        self.speedy = bulletspeed* (mouse_y -self.start_posy) /math.hypot(mouse_x - self.start_posx, mouse_y - self.start_posy) ##float(bulletspeed*(mouse_y-self.y)/  ((mouse_x-self.y)**2+(mouse_y-self.y)**2)**0.5)




# met a jour sa position chaque balle individuellement
    def update(self):


        # elle se deplace en x et y en fonction de speedy et speedx
        self.y += self.speedy
        self.x += self.speedx

        self.rect.bottom = self.y
        self.rect.centerx = self.x
# tue le sprite si il arrive dans les bordures de l'ecran
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.bottom > scr_height:
            self.kill()
        if self.rect.centerx <0:
            self.kill()
        if self.rect.centerx > scr_width:
            self.kill()









# initialise les acteurs de mon jeu et les ajoute a leur groupe correspondant
perso_menu = Perso_menu()
perso_menu.add(perso_menu_group)
boss = Boss()
powerup= PowerUp()
perso = Perso()
perso.add(persos)




pygame.display.flip()

# boucle principale
while 1:

    clock.tick(23)
    scr.blit(img_intro, (0,0))
# permet de quitter le jeu en cliquant sur la croix rouge
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pressed_keys = pygame.key.get_pressed()
# menu a la compilation
    if menu == "intro":
        skiptext = intropolice.render("Press escape to skip", 1, WHITE)
        if pygame.mixer.get_busy() == False:
            intro.play()
        now = pygame.time.get_ticks()
# l'image de fond scroll tous les intro_delay de 3 pixels
        if now - intro_last > intro_delay:
            intro_last = now
# decale l'image de fond de 5 verticalement
            img_intro.scroll(0, -3)

            intro_time += 1
        if intro_time > 718:

# quand c'est fini, commence mon jeu
# menu principal
            menu = "start"
# musique d'intro s'arrete
            intro.stop()
# si l'utilisateur appuie sur escape, passe l'intro
        if pressed_keys[K_ESCAPE]:
            menu = "start"
            intro.stop()

        scr.blit(skiptext, (scr_width- skiptext.get_size()[0], scr_height-skiptext.get_size()[1]))
    if menu == "Credits":

        skiptext = intropolice.render("Press escape to skip", 1, WHITE)
        if pygame.mixer.get_busy() == False:
            intro.play()
        now = pygame.time.get_ticks()
# l'image de fond scroll tous les intro_delay de 3 pixels
        if now - credits_last > intro_delay:
            credits_last = now
# decale l'image de fond de 5 verticalement
            credits_img.scroll(0, -4)


            credits_time += 1
        if credits_time > 500:

# quand c'est fini, commence mon jeu
# menu principal
            menu = "start"
            credits_time = 0
# musique d'intro s'arrete
            intro.stop()
            credits_img = pygame.image.load('Credits.png').convert()

            credits_img = pygame.transform.scale(credits_img, (scr_width, 2876))
        scr.blit(credits_img,(0,0))

# si l'utilisateur appuie sur escape, passe l'intro
        if pressed_keys[K_ESCAPE]:
            menu = "start"
            intro.stop()
            credits_time = 0
            credits_img = pygame.image.load('images/Credits.png').convert()

            credits_img = pygame.transform.scale(credits_img, (scr_width, 2876))

        scr.blit(skiptext, (scr_width- skiptext.get_size()[0], scr_height-skiptext.get_size()[1]))
    if menu == "start":

#joue la musique en boucle
             if pygame.mixer.get_busy() == False:
               music_menu.play()
#oblitere mon fond
             scr.blit(fond,(0,0))

# place les boutons interactifs sur l'ecran
             text=startfont.render("Start", 1, WHITE)
# position du texte
             textx = scr_width/2 - text.get_size()[0]/2
             texty = 60
# rectangle de collision en fonction de la taille du texte
             buttonrect=pygame.Rect((textx,texty), text.get_size())
# idem mais pour le bouton Rules
             rulestext = startfont.render("Rules",1,WHITE)
             rules_textx = 100
             rules_texty = 60
             rulesbuttonrect = pygame.Rect((rules_textx ,rules_texty), rulestext.get_size())
             creditstext = startfont.render("Credits",1, WHITE)
             credits_textx = scr_width*2/3 + 130
             credits_texty = 60
             creditsbuttonrect = pygame.Rect((credits_textx ,credits_texty), creditstext.get_size())
             pygame.draw.rect(scr,(0,50,200), rulesbuttonrect)
             pygame.draw.rect(scr, (0,50,200), buttonrect)
             pygame.draw.rect(scr, (0,50,200), creditsbuttonrect)
# oblitere les 2 boutons
             scr.blit(text, (textx,texty))
             scr.blit(rulestext,(rules_textx,rules_texty))
             scr.blit(creditstext,(credits_textx,credits_texty))
# si l'utilisateur clique sur les boutons, change de menu
             if pygame.mouse.get_pressed()[0] and \
                    buttonrect.collidepoint(pygame.mouse.get_pos()):
                 menu="game"
             elif pygame.mouse.get_pressed()[0] and \
                    rulesbuttonrect.collidepoint(pygame.mouse.get_pos()):
                 shoot_sound.stop()
                 menu="Rules"


             elif pygame.mouse.get_pressed()[0] and \
                    creditsbuttonrect.collidepoint(pygame.mouse.get_pos()):
                 scr.blit(credits_img, (0,0))
                 menu="Credits"
             elif pygame.mouse.get_pressed()[0]:
                for perso_menu in perso_menu_group:
                    perso_menu.shoot()
# anime mon perso sur l'ecran de menu
             perso_menu_group.update()
             bullets_menu.update()
# si mon menu est Rules
    if menu == "Rules":
            if pygame.mixer.get_busy() == False:
               music_menu.play()
# desactive le curseur de la souris
            pygame.mouse.set_visible(False)
# image de ce menu
            scr.blit(menu_rules_img,(0,0))
# si l'utilisateur appuie sur escape, retour au menu principal
            if pressed_keys[K_ESCAPE]:
                menu = "start"

                pygame.mouse.set_visible(True)

    if menu == "game" :
# joue la bonne musique en boucle
            music_menu.stop()
            if pygame.mixer.get_busy() == False:
                music_main.play()
# desactive le curseur
            pygame.mouse.set_visible(False)

# lecture du fichier highscore.txt et obtiens le highscore
            if gameover == 0:
                highscorefichier = open("highscore.txt", "r")
                highscore= highscorefichier.read()
                highscorefichier.close()
            now = pygame.time.get_ticks()
# minotaure en vie = seulement les powerups de boss qui spawnent
            if minotaure_alive == True:
# pseudo-aleatoire
                if now% 100 == 1:
# powerup qui apparait
                    bosspowerup = BossPowerup()
                    bosspowerup.add(boss_powerups)
# sinon autre powerup qui apparait
            elif now% 400 == 1 and powerup_spawn == True: #
                powerup = PowerUp()
                powerup.add(powerups)
# me rajoute une vie tous les 50 ennemis tues
            while oneup > 50:
                perso.lives = perso.lives + 1
                LifeUp_sound.play()
                oneup = 0




            now = pygame.time.get_ticks()
# ennemis spawnent plus si le minotaure a ete tue et si pas de scroll
            if minotaure_killed == True:
                ennemyspawn = False
            else:
                ennemyspawn = True
# idem si il est en vie
            if minotaure_alive == True:
                    ennemyspawn = False
            else:

                    ennemyspawn = True
# variable qui provient de la liste des ennemis tues
            scrollcount = len(ennemys_killed)

# liste similaire, incremente le score de un a chaque fois qu'elle n'est pas vide, puis la vide
            while len(ennemys_killed_score) > 0:
                ennemys_killed_score.empty()
                score += level

# idem a ennemys_killed_score mais pour les vies supplementaire
            while len(ennemys_killed_oneup) > 0:
                ennemys_killed_oneup.empty()
                oneup += 1
# les ennemis arretent de scroll si je viens juste de finir de scroller
            if afterscroll == True:
                ennemyspawn = False

                scrolltime += 1
#check quand est-ce que les ennemis reapparaissent apres le scroll
                if scrolltime >= afterscroll_delay:
                    scrolltime = 0
                    ennemyspawn = True
                    afterscroll = False

# tous les 30 ennemis tues, les ennemis et les powerups apparaissent plus
            if scrollcount >= 30:
                ennemyspawn = False
                powerup_spawn = False

            else:

                    ennemyspawn = True











# regarde si chaque powerup.buff est dans ma liste, si c'est le cas, ajoute concretement l'effet du powerup

            if 'SpeedUp' in activepowerups:
# sa vitesse est augmentee
                persospeed = 15
                now = pygame.time.get_ticks()
# verifie quand le powerup est echu
                if  now - last_SpeedUp > powerupduration:


                    activepowerups.remove('SpeedUp')
                    persospeed = 8

            if 'RoF' in activepowerups:
# chaque balle va plus vite
                bulletspeed = 30
# boucle semblable pour chaque type de powerup
                now = pygame.time.get_ticks()
                if  now - last_RoF > powerupduration:


                    activepowerups.remove('RoF')
# redefinit sa vitesse a sa vitesse de base
                    bulletspeed = 15

# verifie si le powerup de mon boss est echu
            if boss_hiteable == True:

                now = pygame.time.get_ticks()
                if now- last_bosspowerup > boss_powerupduration:

# il ne peut plus etre endommage et son image redevient celle de base
                    boss_hiteable = False
                    bulletspeed = 15
                    bullet_img = pygame.image.load('images/bullet.png').convert()
                    bullet_img = pygame.transform.scale(bullet_img,(7,7))

# grosses balles
            if 'BigBullet' in activepowerups:
# change l'image pour une grosse balle
                bullet_img = pygame.image.load('images/BigBullet_Active.png').convert_alpha()
                bullet_img = pygame.transform.scale(bullet_img,(16,16))
                now = pygame.time.get_ticks()
                if now- last_BigBullet > powerupduration:
                    activepowerups.remove('BigBullet')
                    bullet_img = pygame.image.load('images/bullet.png').convert()
                    bullet_img = pygame.transform.scale(bullet_img,(7,7))

# invincibilite
            if 'invincibility' in activepowerups:
# le perso est invincible
                invincibility = True
# instancie un bouclier
                shield = Shield()
                shield.add(Shield_group)
                now = pygame.time.get_ticks()
                if now - last_invincibility > powerupduration:
                    activepowerups.remove('invincibility')
                    invincibility = False
                    shield.remove(Shield_group)

# fait apparaitre mes ennemis en boucle
            if ennemyspawn == True:
# timer qui fait spawn tout les spawn_delay
                now = pygame.time.get_ticks()
                if not boss_group.has(boss):
                    if now% 300 == 30:
                        pelpe = Pelpe()
                        pelpe.add(ennemys)
                if now - last_spawn > spawn_delay:
# 3 ennemis apparaissent
                    ennemy = Ennemy()
                    ennemy1 = Ennemy()
                    ennemy2= Ennemy()
                    ennemy.add(ennemys)
                    ennemy1.add(ennemys)
                    ennemy2.add(ennemys)
                    last_spawn = now

# triple condition qui declenche le scrolling
            if (scrollcount >= 30 and perso.x >= scr_width - 64  and flechedisplay == True):
                    scroll = True

                    scroll_delay = 0.1
            else:


                    scr.blit(backgroundImage, (0,0))
# tous les 4 ecrans scrolles et l'ecran clear, un boss spawn
            if times_scrolled == 4 and scrollcount >= 30:
                if  boss_group.has(boss) == False and minotaure_killed == False:
                    boss_spawn = True

# fait apparaitre un boss
            if boss_spawn == True:
                boss = Boss()
                boss_group.add(boss)
                minotaure_spawn_sound.play()
                for boss in boss_group:
                    bigexplosion = BigExplosion(boss.x, boss.y)
                    bigexplosion.add(explosions)
                minotaure_alive = True
                boss_spawn = False

# si le minotaure est mort, affiche une fleche sur l'ecran
            if  minotaure_alive == False:
                 if scrollcount >= 30:
                    now = pygame.time.get_ticks()
                    flechedisplay = True

# si le boss a plus de vie, meurt et explose, plus de score
            for boss in boss_group:

             if boss.lives == 0:
                        minotaure_death_sound.play()
                        explosion = Explosion(boss.x, boss.y+100)
                        explosion.add(explosions)
                        explosion = Explosion(boss.x+ 40, boss.y+60)
                        explosion.add(explosions)
                        explosion = Explosion(boss.x, boss.y+90)
                        explosion.add(explosions)
                        explosion = Explosion(boss.x+ 40, boss.y+120)
                        explosion.add(explosions)
                        explosion = Explosion(boss.x+ 20, boss.y+50)
                        explosion.add(explosions)
                        explosion = Explosion(boss.x+ 40, boss.y+20)
                        explosion.add(explosions)
                        big_explosion = BigExplosion(boss.x, boss.y)
                        big_explosion.add(explosions)
                        boss.remove(boss_group)
                        minotaure_alive = False
                        score += 30
                        minotaure_killed = True
                        boss.rect = pygame.Rect(0,0,0,0)
# en cas de scroll
            if scroll == True:
# vide les groupes
                    all_sprites.empty()
                    bullets.empty()
                    powerups.empty()
                    boss_powerups.empty()
                    explosions.empty()
                    ennemybullets.empty
                    ennemys.empty()
                    boss_group.empty()
# desactive la fleche
                    flechedisplay = False

                    minotaure_alive = False

# scroll tous les scroll_delay ( soit 0,1 ticks)
                    now = pygame.time.get_ticks()
                    if now - last_scroll > scroll_delay:
                         last_scroll = now
# decale l'image de fond de 50
                         backgroundImage.scroll(-55)
# corrige la position de mon personnage
                         perso.x -= 54


                         scr.blit(backgroundImage,(0,0))
# pour arreter le scroll si mon perso est au bord de l'ecran
                         if perso.x <=  0:
                            ennemys_killed.empty()
                            scroll = False
                            minotaure_killed = False
                            now = pygame.time.get_ticks()
                            perso.x += 30

# reduit le delai d'apparition des ennemis
                            spawn_delay -= 10
                            afterscroll = True

# bouclier qui dure moins longtemps pour eviter de se faire tuer instantanement par un ennemi qui apparait sur la droite
                            activepowerups.append('invincibility')
                            last_invincibility = now - 10000
                            powerup_spawn = True

# incremente la variable pour qu'au 5e scroll, l'image originale soit obliteree
                            times_scrolled += 1
                            if times_scrolled == 5:

                                backgroundImage=pygame.image.load('images/fond_main_new.png').convert()
                                backgroundImage = pygame.transform.scale(backgroundImage,( scr_width*6, scr_height))
                                times_scrolled = 0
# augmente la difficulte d'un niveau
                                level += 1



# collisions des powerups avec le perso
            for powerup in powerups:
                if pygame.sprite.collide_circle(powerup, perso) == True:
                    powerupsound.play()
                    if powerup.buff == 'SpeedUp':
                        now = pygame.time.get_ticks()
                        last_SpeedUp = now
                    if powerup.buff == 'RoF':
                        now = pygame.time.get_ticks()
                        last_RoF = now
                    if powerup.buff == 'BigBullet':
                        last_BigBullet = now
                    if powerup.buff == 'invincibility':
                        last_invincibility = now
                    powerup.rect =(0,0,0,0)
                    powerup.remove(powerups)
# l'ajoute a la liste des powerups actifs
                    activepowerups.append(powerup.buff)
# idem pour celui du boss
            for bosspowerup in boss_powerups:
                if pygame.sprite.collide_circle(bosspowerup, perso) == True:
                    boss_powerup.play()
# augmente la vitesse des balles + fait des degats au boss
                    bulletspeed = 15
                    boss_hiteable = True

                    now = pygame.time.get_ticks()
                    last_bosspowerup = now
                    bosspowerup.rect =(0,0,0,0)
# le retire de la liste
                    bosspowerup.remove(boss_powerups)


# fait disparaitre la balle si elle touche un boss
            for bullet in bullets:
                bullet_hit_list = (pygame.sprite.spritecollide(boss,bullets, True, pygame.sprite.collide_mask))
                for bullet in bullet_hit_list:
                    bullets.remove(bullet)










# si mon perso n'a plus de vies, c'est gameover

            if perso.lives < 0:

                gameover = 1
                menu = "game over"
# joue la musique de mort
                death_music.play()





















# si l'utilisateur appuie sur click gauche, tire

            if pygame.mouse.get_pressed()[0]:


                    perso.shoot()



#affiche le score
            scoretext = police.render("Score {0}".format(int(score)), 1,
            BLACK)
            scr.blit(scoretext, ( scr_width/2 -scoretext.get_size()[0]/2, 30))
# affiche le highscore
            highscoretext = police.render("HighScore {0}".format(float(highscore)),1, (255,0,0))
            scr.blit(highscoretext, (scr_width/2 - highscoretext.get_size()[0]/2, 60))
# affiche les vies actuelles
            livestext= police.render("Lives : {0}".format(int(perso.lives)),1,BLACK)
            scr.blit(livestext, (scr_width/2 - livestext.get_size()[0]/2,  45))

# gere l'affichage de la fleche
            if flechedisplay == True:
                    fleche_img = fleche1_img
# timer pour l'animation
                    if now - last_fleche > fleche_delay:


                        fleche_img_displayed = fleche1_img
                    else: fleche_img_displayed = fleche2_img
                    if now- last_fleche > fleche_delay*2:
                        last_fleche = now
#oblitere la fleche si necessaire
            if flechedisplay == True:
                scr.blit(fleche_img_displayed,(scr_width - 140, scr_height /2-32))

# actualise tous mes groupes

            all_sprites.update()
            boss_group.update()
            boss_powerups.update()
            powerups.update()
            explosions.update()

            persos.update()

            Shield_group.update()
            ennemys.update()
            ennemybullets.update()
            all_sprites.draw(scr)
# affiche le curseur personnalise (viseur)
            scr.blit(curseur_img, (pygame.mouse.get_pos()[0] -8, pygame.mouse.get_pos()[1]-8))

# si perdu
    if menu=="game over":
        minotaure_spawn_sound.stop()
        music_main.stop()
# souris visible
        pygame.mouse.set_visible(True)


# affiche differentes images en fonction du score
        if score < 300:
            scr.blit(Gameover_Low_img,(0,0))
        if 300 < score < 500:
            scr.blit(Gameover_Medium_img,(0,0))
        if score > 500:
            scr.blit(Gameover_High_img,(0,0))


# bouton pour reessayer
        scr.blit(retrybutton, (scr_width / 2 -128, scr_height - 120))
        retryrect = pygame.Rect(scr_width/2- 128, scr_height - 120, 256,80)
# si il est presse, reinitialisele jeu et recommence
        if pygame.mouse.get_pressed()[0] and \
                    retryrect.collidepoint(pygame.mouse.get_pos()):
                 backgroundImage=pygame.image.load('images/fond_main_new.png').convert()
                 backgroundImage = pygame.transform.scale(backgroundImage,( scr_width*6, scr_height))
                 perso = Perso()
                 perso.add(persos)
                 score = 0.0
                 oneup = 0
                 ennemys_killed.empty()
                 times_scrolled = 0
                 ennemys.empty()
                 powerups.empty()
                 boss_group.empty()
                 bullets.empty()
                 pygame.sprite.Group.empty(all_sprites)
                 pygame.sprite.Group.empty(explosions)
                 death_music.stop()
                 music_main.play()
                 boss_hiteable = False
                 minotaure_alive = False
                 minotaure_killed = False
                 powerup_spawn = True
                 level = 1
                 bulletspeed = 15
                 persospeed = 10


                 menu="game"
# definis le score actuel comme highscore si il est effectivement un highscore
        if int(math.floor(score))>int(float(highscore)):

             newHighScore = highscorefont.render("New Record!"
                        .format(int(math.floor(score))), 1, (255,255,255))
# indique au joueur qu'il a fait un highscore
             scr.blit(newHighScore, (scr_width/ 2 -144, scr_height/2  + 140))
             highscorefichier = open("highscore.txt", "w")
             highscorefichier.write(str(math.floor(score)))

# affiche le score final
        scoretext = ScoreFont.render("{0}".format(int(math.floor(score))),1 , (255,255,255))
        scr.blit(scoretext ,(scr_width/2 + 133,scr_height/2  + 45))













    pygame.display.flip()


pygame.quit