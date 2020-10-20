'''
#
# Obligatorisk karaktersatt oppgave #1
#
# Legg spesielt merke til at det er kun koden i klassen Kalman som kan endres. Det er koden som skal leveres inn
# Det er derfor viktig at INGEN ANNEN KODE ENDRES !!! 
#
'''
import pygame as pg
from random import random, randint
import numpy as np
from numpy.linalg import norm

fps = 0.0

class Projectile():

    def __init__(self, kalman=None):
        self.background = background
        self.rect = pg.Rect((800, 700), (16, 16))
        self.px = self.rect.x
        self.py = self.rect.y
        self.dx = 0.0
        self.kalm = kalman

    def move(self, goal):

        #  if self.kalm:
        #      goal = self.kalm.calc_next(goal)

        deltax = np.array(float(goal) - self.px)
        # print(delta2)
        mag_delta = norm(deltax)  # * 500.0
        np.divide(deltax, mag_delta, deltax)

        self.dx += deltax
        #  if self.dx:
        #     self.dx /= norm(self.dx) * 50

        self.px += self.dx / 50.0
        self.py += -0.5
        try:
            self.rect.x = int(self.px)
        except:
            pass
        try:
            self.rect.y = int(self.py)
        except:
            pass


class Target():

    def __init__(self, background, width):
        self.background = background
        self.rect = pg.Rect(self.background.get_width() // 2 - width // 2,
                            50, width, 32)
        self.dx = 1 if random() > 0.5 else -1

    def move(self):
        self.rect.x += self.dx

        if self.rect.x < 300 or self.rect.x > self.background.get_width() - 300:
            self.dx *= -1

    def noisy_x_pos(self):
        pos = self.rect.x
        center = self.rect.width // 2
        noise = np.random.normal(0, 1, 1)[0]
        return pos + center + noise * 300.0

#
# Her er Kalmanfilteret du skal utvikle
#
class Kalman():
    '''
    # https://www.kalmanfilter.net/alphabeta.html
    # https://arxiv.org/pdf/1204.0375.pdf
    # Algoritmen er iterativ. Hvert trinn inkluderer to faser: prediksjon og måleoppdatering.
    # Init: System state initial guess
    # 1: Input: Målt verdi
    # 2: Kalkuler Kalman gain (A). Estimer current state med state update equation. Output: System State Estimate ^Xn,n
    # 3: Kalkuler forventet state for neste iterasjon. Unit delay (n -> n+1). ^Xn,n-1
    # Gjenta 2 og 3
    '''

    # Enkelte verdier er basert på gjetting, prøving og feiling
    def __init__(self):
        self.alpha = 2 / 3
        self.beta = 0.1
        self.n = iters  # antall iterasjoner
        self.dt = fps   # dt antall målinger i sekundet gitt i fps
        self.current_iteration = 9   # xn_n
        self.prediction = 0    # Xn,n + 1
        self.previous_iteration = 0   # Xn,n - 1
        self.xdhn_n = 1
        self.xdhn_n_plus_1 = 0
        self.xdhn_n_minus_1 = 0
        self.z_n = 0.0

    def state_extrapolation_equation(self):
        self.prediction = self.current_iteration + (self.dt * self.xdhn_n)
        self.xdhn_n_plus_1 = self.xdhn_n

    def state_update_equation(self):
        self.current_iteration = self.previous_iteration + self.alpha * (self.z_n - self.previous_iteration)

        ''' Hver for seg gir de to neste regnestykkene stigende eller synkende kalmanscore.
            Ved å bruke begge to får jeg mer konsistent resultat / kalmanscore.'''
        self.xdhn_n = self.xdhn_n_minus_1 + self.beta * (
                (self.z_n - self.previous_iteration) // self.dt)  # gir økende kalmanscore 0.0 -> 0.8
        self.xdhn_n = self.xdhn_n_minus_1 + self.beta * (
                (self.z_n - self.previous_iteration) / self.dt)  # gir minkende kalmanscore 0.4 -> 0.9

    def measurement(self, value):
        self.z_n = value

    def iterate(self):
        self.n += iters  # iterasjoner
        # predikeringen fra forrige iterasjon settes til det forrige estimatet til nåværende iterasjon
        self.previous_iteration = self.current_iteration
        self.xdhn_n_minus_1 = self.xdhn_n
        self.dt = fps

    def calc_next(self, zi):
        # ved første iterering initialiserer man verdiene med kvalifisert gjetning
        if self.n == 0:
            self.state_extrapolation_equation()
            self.previous_iteration = self.prediction
            self.xdhn_n_minus_1 = self.xdhn_n_plus_1

        self.measurement(zi)
        self.state_update_equation()
        self.state_extrapolation_equation()
        self.iterate()
        return self.current_iteration    # returnerer predikert posisjon til k_miss


pg.init()

w, h = 1600, 800

background = pg.display.set_mode((w, h))
surf = pg.surfarray.pixels3d(background)
running = True
clock = pg.time.Clock()

kalman_score = 0
reg_score = 0
iters = 0

while running:
    target = Target(background, 32)
    missile = Projectile(background)
    kalman = Kalman()
    k_miss = Projectile(background)  # kommenter inn denne linjen naar Kalman er implementert
    noisy_draw = np.zeros((w, 20))

    trial = True
    iters += 1

    while trial:
        # Setter en maksimal framerate på 300. Hvis dere vil øke denne er dette en mulig endring
        clock.tick(300)
        fps = clock.get_fps()

        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False

        background.fill(0x448844)
        surf[:, 0:20, 0] = noisy_draw

        last_x_pos = target.noisy_x_pos()  # dette er støyen vi skal filtrere

        target.move()
        missile.move(last_x_pos)
        k_miss.move(kalman.calc_next(last_x_pos))  # kommenter inn denne linjen naar Kalman er implementert

        pg.draw.rect(background, (255, 200, 0), missile.rect)
        pg.draw.rect(background, (0, 200, 255), k_miss.rect)  # kommenter inn denne linjen naar Kalman er implementert
        pg.draw.rect(background, (255, 200, 255), target.rect)

        noisy_draw[int(last_x_pos):int(last_x_pos) + 20, :] = 255
        noisy_draw -= 1
        np.clip(noisy_draw, 0, 255, noisy_draw)

        coll = missile.rect.colliderect(target.rect)
        k_coll = k_miss.rect.colliderect(target.rect)  # kommenter inn denne linjen naar Kalman er implementert#

        if coll:
            reg_score += 1

        if k_coll:  # kommenter inn denne linjen naar Kalman er implementert
            kalman_score += 1

        oob = missile.rect.y < 20

        # runden er over
        if oob or coll or k_coll:  # or k_coll #endre denne sjekken slik at k_coll ogsaa er med naar kalman er implementert
            trial = False

        pg.display.flip()

    print('kalman score: ', round(kalman_score / iters, 2))  # kommenter inn denne linjen naar Kalman er implementert
    print('regular score: ', round(reg_score / iters, 2))

pg.quit()
