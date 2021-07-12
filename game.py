import pygame
pygame.init()


size = [600, 400]

display = pygame.display.set_mode(size)

clock = pygame.time.Clock()
FPS = 30

white = (255, 255, 255)
red = (255, 0, 0)
yellow = (240, 230, 170)

car_surf = pygame.image.load('images/car.bmp').convert()
car_surf = pygame.transform.scale(car_surf,
                                  (car_surf.get_width() // 3,
                                   car_surf.get_height() // 3))
finish_surf = pygame.image.load('images/finish.png')
finish_rect = finish_surf.get_rect(center=(0, 0))
background = pygame.image.load('images/sand.jpg').convert()

icon = pygame.image.load('images/icon_car.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Car")

car_surf.set_colorkey(white)
car_rect = car_surf.get_rect(center=(size[0] - 35, size[1] - 50))

background = pygame.transform.scale(background,
                                    (background.get_width() // 3,
                                     background.get_height() // 3))

cactus = pygame.image.load('images/cactus.png')
cactus = pygame.transform.scale(cactus, (cactus.get_width() // 15, cactus.get_height() // 15))
cactus_rect = cactus.get_rect(center=(200, 290))

cactus2 = pygame.image.load('images/cactus.png')
cactus2 = pygame.transform.scale(cactus2, (cactus2.get_width() // 15, cactus2.get_height() // 15))
cactus2_rect = cactus2.get_rect(center=(400, 100))

boom = pygame.image.load('images/boom.png')
boom.set_colorkey(white)
boom = pygame.transform.scale(boom, (boom.get_width() // 6, boom.get_height() // 6))
boom_rect = boom.get_rect(center=(0, 0))

def cactusBOOM():
    if car_rect.colliderect(cactus_rect) or car_rect.colliderect(cactus2_rect):
        return False
    return True

def win():
    if car_rect.colliderect(finish_rect):
        draw_win()
        pygame.time.wait(3000)
        return False
    return True


f = pygame.font.Font('fonts/fontMY.otf', 100)
sc_text = f.render('YOU LOSE!', 1, red)
sc_text2 = f.render('YOU WIN!', 1, white)
pos = sc_text.get_rect(center=(size[0] // 2, size[1] // 2))


def draw_text():
    display.blit(sc_text, pos)
    pygame.display.update()

def draw_win():
    display.blit(sc_text2, pos)
    pygame.display.update()








car_up = car_surf
car_down = pygame.transform.flip(car_surf, False, True)
car_left = pygame.transform.rotate(car_surf, 90)
car_right = pygame.transform.flip(car_left, True, False)
car_rightup = pygame.transform.rotate(car_surf, -45)
car_rightdown = pygame.transform.rotate(car_surf, -135)
car_leftup = pygame.transform.rotate(car_surf, 45)
car_leftdown = pygame.transform.rotate(car_surf, 135)
car = car_up
left = right = down = False
up = True
speed = 5

game = True
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    key = pygame.key.get_pressed()




    if key[pygame.K_a]:
        left = True
        car = car_left
        car_rect.x -= speed
        if car_rect.x < 0:
            car_rect.x = 0
    else:
        left = False

    if key[pygame.K_d]:
        right = True
        car = car_right
        car_rect.x += speed
        if car_rect.right > size[0]:
            car_rect.right = size[0]
    else:
        right = False

    if key[pygame.K_w]:
        up = True
        car = car_up
        car_rect.y -= speed
        if car_rect.y < 0:
            car_rect.y = 0
    else:
        up = False

    if key[pygame.K_s]:
        down = True
        car = car_down
        car_rect.y += speed
        if car_rect.bottom > size[1]:
            car_rect.bottom = size[1]
    else:
        down = False

    if up and right:
        car = car_rightup
    if up and left:
        car = car_leftup
    if down and right:
        car = car_rightdown
    if down and left:
        car = car_leftdown

    car_rect = car.get_rect(center=(car_rect.center))




    display.blit(background, (0, 0))
    display.blit(cactus, cactus_rect)
    display.blit(cactus2, cactus2_rect)
    display.blit(finish_surf, (0, 0))
    display.blit(car, car_rect)

    game = win()
    game = cactusBOOM()
    if game == False:
        if car_rect.colliderect(cactus_rect):
            display.blit(boom, (100, 210))
            draw_text()
            pygame.display.update()
        if car_rect.colliderect(cactus2_rect):
            display.blit(boom, (300, 20))
            draw_text()
            pygame.display.update()

        pygame.time.wait(3000)

    pygame.display.update()

