import sys, pygame
import paddle
import ball

pygame.init()

pygame.display.set_caption('Pong')

clock = pygame.time.Clock()

SCR_WTH = 800
SCR_HTH = 500

FontSize = 150

paddle_offset = 15
paddle_width = 20

screen = pygame.display.set_mode((SCR_WTH, SCR_HTH))

paddL = paddle.Paddle(paddle_offset,SCR_HTH/2 - 55, 110,paddle_width, (0, 154, 231, 1),screen, SCR_HTH,SCR_WTH, paddle_offset)
paddR = paddle.Paddle(SCR_WTH - paddle_offset - paddle_width,SCR_HTH/2 - 55, 110, paddle_width,(196, 11, 23, 1),screen, SCR_HTH, SCR_WTH,paddle_offset)
ball = ball.Ball(10,SCR_WTH/2 , SCR_HTH/2,screen,SCR_HTH, SCR_WTH)


while 1:
    deltatime = clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            #paddL.checkInp(event.key, True)
            paddR.checkInp(event.key, True)
            pass

        elif event.type == pygame.KEYUP:
            #paddL.checkInp(event.key, False)
            paddR.checkInp(event.key, False)
            pass


    pygame.draw.line(screen, (196, 196, 196, 0.12), (SCR_WTH/2,0),(SCR_WTH/2,SCR_HTH),paddle_offset)
    pygame.draw.rect(screen, (196, 196, 196, 0.12),pygame.Rect(0,0,SCR_WTH, SCR_HTH), paddle_offset)

    font = pygame.font.SysFont(None, FontSize)

    Lscore = font.render(str(paddL.score), True, (196, 196, 196, 0.12))
    screen.blit(Lscore, (SCR_WTH/4, SCR_HTH/2 - FontSize/2))

    Rscore = font.render(str(paddR.score), True, (196, 196, 196, 0.12))
    screen.blit(Rscore, (SCR_WTH * 3/4, SCR_HTH/2 - FontSize/2))

    paddL.activatebot(ball, True)
    #paddR.activatebot(ball, False)

    ball.checkCollision(paddL.rect, paddR.rect, paddle_offset)
    paddL.draw(deltatime)
    paddR.draw(deltatime)
    ball.draw(deltatime, paddle_offset, paddL, paddR)

    pygame.display.flip()

    screen.fill((0,0,0))

pygame.quit()
    