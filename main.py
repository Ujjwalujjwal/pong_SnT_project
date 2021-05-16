import sys, pygame
import paddle
import ball

pygame.init()

SCR_WTH = 800
SCR_HTH = 500

speed = [2, 2]
black = 0, 0, 0



screen = pygame.display.set_mode((SCR_WTH, SCR_HTH))

paddL = paddle.Paddle(15,SCR_HTH/2 - 55, 110,screen, SCR_HTH)
paddR = paddle.Paddle(SCR_WTH - 30 ,SCR_HTH/2 - 55, 110,screen, SCR_HTH)
ball = ball.Ball(10,SCR_WTH/2 , SCR_HTH/2,screen,SCR_HTH, SCR_WTH)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            paddL.checkInp(event.key, True)
            paddR.checkInp(event.key, True)

        elif event.type == pygame.KEYUP:
            paddL.checkInp(event.key, False)
            paddR.checkInp(event.key, False)

    ball.checkCollision(paddL.rect, paddR.rect)
    paddL.draw()
    paddR.draw()
    ball.draw()
    pygame.display.flip()
    screen.fill(black)
    