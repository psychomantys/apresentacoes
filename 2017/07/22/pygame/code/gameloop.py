"""
Codigo demonstrativo para a apresentação. Algumas coisas podem
ser melhores, mas para a apresentação acho que vai ser mais didatico
assim

O codigo apenas abre uma tela e trata o evento de QUIT
"""

import pygame
import os 


# Variaveis usadas ao longo do programa
done=False
clock=pygame.time.Clock()
screen=None
fps=30
screen_mode=(800,600)


def event_handler():
	global done
	for event in pygame.event.get():
		# Trata evento QUIT
		if event.type == pygame.QUIT:
			done=True


def game_init():
	pygame.init()
	screen=pygame.display.set_mode(screen_mode)
	done=True


def game_end():
	pygame.quit()


def render():
	# Limita as iterações pelo numero de FPS
	clock.tick(fps)
	pygame.display.flip()


def game_logic():
	done


def step_physics():
	done


try:
	game_init()
	while not done:
		event_handler()
		game_logic()
		step_physics()
		render()
finally:
	game_end()

