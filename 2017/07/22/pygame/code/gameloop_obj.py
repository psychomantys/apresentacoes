
import pygame

class Ball(pygame.sprite.Sprite):
	image=None
	rect=None
	speed_x=None
	speed_y=None

	color_transparent=None

	def __init__(self, image, x, y, transparency):
		pygame.sprite.Sprite.__init__(self)

		self.color_transparent=transparency

		self.image=pygame.image.load(image).convert()
		self.image.set_colorkey(self.color_transparent)
		self.rect=self.image.get_rect()

		self.rect.x=x
		self.rect.y=y

		self.speed_x=5
		self.speed_y=5

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


class App(object):
	# Variaveis usadas ao longo do programa
	done=False
	clock=None
	screen=None
	layer_front=None

	color_transparent=(44,3,195)
	color_background=(0,0,0)
	fps=30
	screen_mode=(800,600)

	
	def main_loop(self):
		while not self.done:
			self.event_handler()
			self.game_logic()
			self.step_physics()
			self.render()

	def __del__(self):
		pygame.quit()

	def __init__(self):

		pygame.init()
		self.screen=pygame.display.set_mode(self.screen_mode)

		self.clock=pygame.time.Clock()
		self.screen.fill(self.color_background)

		self.layer_front=pygame.sprite.RenderUpdates()

		ball=Ball("figuras/ball.png", 100, 100, self.color_transparent)
		self.layer_front.add(ball)
		ball=Ball("figuras/ball.png", 200, 450, self.color_transparent)
		self.layer_front.add(ball)

	def event_handler(self):
		for event in pygame.event.get():
			# Trata evento QUIT
			if event.type == pygame.QUIT:
				self.done=True
			elif event.type == pygame.KEYDOWN:
				print(pygame.key.name(event.key))
            
	def render(self):
		self.screen.fill(self.color_background)
		self.layer_front.draw(self.screen)
		pygame.display.flip()

		# Limita as iterações pelo numero de FPS
		self.clock.tick(self.fps)


	def game_logic(self):
		
		for item in self.layer_front:
			item.move(item.speed_x, item.speed_y)
		template="{} - FPS: {:.2f}"
		caption=template.format("Python Day", self.clock.get_fps())
		pygame.display.set_caption(caption)


	def step_physics(self):
		# phys.step()
		self.layer_front.update()

if __name__ == "__main__":
	App().main_loop()

