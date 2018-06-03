import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

display = pygame.display.set_mode((640, 480), 0)

cam = pygame.camera.Camera("/dev/video0", (640, 480))
cam.start()

while True:
    image = cam.get_image()
    display.blit(image, (0, 0))
    # pygame.display.flip() equals to pygame.display.update() when no arguments provided
    # pygame.display.update(rect_list) only update a rectangle area defined by rect list
    # rect_list refers to Rect(left, top, width, height)
    pygame.display.flip()
