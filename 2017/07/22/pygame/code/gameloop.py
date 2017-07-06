"""
Codigo demonstrativo para a apresentação. Algumas coisas podem
ser melhores, mas para a apresentação acho que vai ser mais didatico
assim

"""

import pygame
import sys
import os


# Variaveis usadas ao longo do programa
done=False
clock=None
screen=None
layer_front=None

speed_x=5
speed_y=5
color_transparent=(44,3,195)
color_background=(0,0,0)
fps=30
screen_mode=(800,600)

class Ball(pygame.sprite.Sprite):
	image=None
	rect=None
	speed_x=None
	speed_y=None

	def __init__(self, image, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(image).convert()
		self.image.set_colorkey(color_transparent)
		self.rect=self.image.get_rect()

		self.rect.x=x
		self.rect.y=y

		self.speed_x=speed_x
		self.speed_y=speed_y

	def draw(self, screen):
		screen.blit(self.image, self.rect)

	def move(self, x, y):
		self.rect.move_ip(x,y)

	def turn(self):
		self.image=pygame.transform.flip(self.image, True, False)

	def update(self):
		if self.rect.left<0:
			self.speed_x=-self.speed_x
			self.turn()
		if self.rect.right>800:
			self.speed_x=-self.speed_x
			self.turn()
		if self.rect.top<0:
			self.speed_y=-self.speed_y
		if self.rect.bottom>600:
			self.speed_y=-self.speed_y


def main(argv):
	try:
		game_init()
		while not done:
			event_handler()
			game_logic()
			step_physics()
			render()
	finally:
		game_end()



def event_handler():
	global done

	for event in pygame.event.get():
		# Trata evento QUIT
		if event.type == pygame.QUIT:
			done=True
		elif event.type == pygame.KEYDOWN:
			print(pygame.key.name(event.key))
            


def game_init():
	global screen
	global clock
	global layer_front

	pygame.init()
	pygame.display.set_caption("Python Day")
	screen=pygame.display.set_mode(screen_mode)

	clock=pygame.time.Clock()
	screen.fill(color_background)

	layer_front=pygame.sprite.RenderUpdates()

	ball=Ball("figuras/ball.png", 100, 100)
	layer_front.add(ball)
	ball=Ball("figuras/ball.png", 200, 450)
	layer_front.add(ball)


def game_end():
	pygame.quit()

def render():
	screen.fill(color_background)
	#ball.draw(screen)
	layer_front.draw(screen)
	pygame.display.flip()

	# Limita as iterações pelo numero de FPS
	clock.tick(fps)


def game_logic():
	# ball.move(speed_x, speed_y)
	for item in layer_front:
		item.move(item.speed_x, item.speed_y)
	template="{} - FPS: {:.2f}"
	caption=template.format("Python Day", clock.get_fps())
	pygame.display.set_caption(caption)


def step_physics():
	# phys.step()
	layer_front.update()

if __name__ == "__main__":
	main(sys.argv)

