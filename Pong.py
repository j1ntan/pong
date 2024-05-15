import pygame, sys, random , time , pickle  

clock = pygame.time.Clock()

inp=int(input("0:See Highscore\n1:Play Game\n"))

x=None

if inp==0:
    x=False
    mode='r'
elif inp==1:
    x=True
    mode='r+'
else:
    print("invalid input.")


f = open('record.txt', mode)
a=eval(f.read())
p1_highscore=a[0]
p2_highscore=a[1]

from pygame.locals import *
pygame.init()
pygame.display.set_caption("Pong")

winsize = (1280, 720)
screen = pygame.display.set_mode(winsize, 0, 32)
p = pygame.image.load("player1.png")
b = pygame.image.load("ball.png")

spy = [-10,10,9,-9]

p1_up = False
p1_down = False
p1_pos = [10,290]

p2_up = False
p2_down = False
p2_pos = [1222,290]

ball_spx = random.choice(spy)
ball_spy = random.choice(spy)
ball_pos = [600,330]

score_right = 0
score_left = 0

ball_spx = random.choice(spy)
ball_spy = random.choice(spy)
ball_pos = [600,330]

score_right = 0
score_left = 0
player1 = pygame.Rect((p1_pos[0]+20, p1_pos[1]+10), (13, 106))
player2 = pygame.Rect((p2_pos[0]+20, p2_pos[1]+10), (13, 106))

font = pygame.font.SysFont("bahnschrift", 35)
white = (255, 255, 255)

#conditions
condition_right = ball_pos[0]>1180 and ball_pos[1]>310 and ball_pos[1]<410
condition_left = ball_pos[0]<30 and ball_pos[1]>310 and ball_pos[1]<410

while x:

    while True:

        ball = pygame.Rect((ball_pos[0]+20, ball_pos[1]+20), (40, 40))

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:

                if event.key == K_UP:
                    p2_up = True
                if event.key == K_DOWN:
                    p2_down = True
            if event.type == KEYUP:

                if event.key == K_UP:
                    p2_up = False
                if event.key == K_DOWN:
                    p2_down = False
            if event.type == KEYDOWN:

                if event.key == K_e:
                    p1_up = True
                if event.key == K_d:
                    p1_down = True
            if event.type == KEYUP:

                if event.key == K_e:
                    p1_up = False
                if event.key == K_d:
                    p1_down = False

        if ball_pos[1]>0 and ball_pos[1]<720:

            if ball_pos[0]>1200 or ball_pos[0]<5:

                if ball_pos[0]>1200:
                    score_right += 1
                    ball_pos = [600,325]
                    ball_spx=-10
                    ball_spy=random.choice(spy)
                    time.sleep(1)

                if ball_pos[0]<30:
                    score_left += 1
                    ball_pos = [600,325]
                    ball_spx=10
                    ball_spy=random.choice(spy)
                    time.sleep(1)

            else: 
                if ball_pos[0] <= -12 or ball_pos[0] >= 1215:
                    ball_spx *= -1

                if ball_pos[1] <= -12 or ball_pos[1] >= 655:
                    ball_spy *= -1

        else:

            if ball_pos[0] <= -12 or ball_pos[0] >= 1215:
                ball_spx *= -1

            if ball_pos[1] <= -12 or ball_pos[1] >= 655:
                ball_spy *= -1   

        if pygame.Rect.colliderect(ball,player1) or pygame.Rect.colliderect(ball,player2):
            ball_spx *= -1

        screen.fill((0,0,0))
        pygame.draw.line(screen,(255,255,255), [639,0], [639,720], width=1)
        pygame.draw.line(screen,(200,200,200), [0,5], [1280,5], width=3)
        pygame.draw.line(screen,(200,200,200), [0,715], [1280,715], width=3)
        screen.blit(p,p1_pos)
        screen.blit(p,p2_pos)
        screen.blit(b,ball_pos)

        ball_pos[0] += ball_spx
        ball_pos[1] += ball_spy

        ball.top = ball_pos[1]
        ball.left = ball_pos[0]

        if p1_up == True and p1_pos[1] > 0:
            p1_pos[1] -= 11
            player1.top -=11
        if p1_down == True and p1_pos[1] < 597:
            p1_pos[1] += 11
            player1.top +=11
        
        if p2_up == True and p2_pos[1] > 0:
            p2_pos[1] -= 11
            player2.top -=11
        if p2_down == True and p2_pos[1] < 597:
            p2_pos[1] += 11
            player2.top +=11

        #display
        value = font.render("P2 Score: " + str(score_left) , 2, True, white)
        screen.blit(value, [1050, 0])
        value_2 = font.render("P1 Score: " + str(score_right) , 2, True, white)
        screen.blit(value_2, [50, 0])

        #scoring
        if condition_right==True:
            score_right +=1
            ball_pos=[600,325]

        if condition_left==True:
            score_left +=1
            ball_pos=[600,325]

        if score_right>int(p1_highscore):
            p1_highscore=score_right
        if score_left>int(p2_highscore):
            p2_highscore=score_left

        pygame.display.update()
        clock.tick(130)
    
        f.seek(0)
        a=(p1_highscore,p2_highscore)
        f.write(str(a))

else:
    print("player 1 highscore -",a[0])
    print("player 2 highscore -",a[1])

f.close()