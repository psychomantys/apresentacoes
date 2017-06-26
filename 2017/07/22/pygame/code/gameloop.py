"""
Codigo demonstrativo para a apresentação. Algumas coisas podem
ser melhores, mas para a apresentação acho que vai ser mais didatico
assim

O codigo apenas abre uma tela e trata o evento de QUIT
"""

import pygame
import sys
import os


# Variaveis usadas ao longo do programa
done=False
clock=None
screen=None
fps=30
screen_mode=(800,600)

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


def game_init():
	pygame.init()
	pygame.display.set_caption("Python Day")
	pygame.display.set_mode(screen_mode)

	global clock
	clock=pygame.time.Clock()


def game_end():
	pygame.quit()


def render():
	pygame.display.flip()

	# Limita as iterações pelo numero de FPS
	clock.tick(fps)


def game_logic():
	pass


def step_physics():
	pass


if __name__ == "__main__":
	main(sys.argv)

