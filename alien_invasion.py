import sys
import os
import pygame

from settings import Settings
from ship import Ship

def run_game():
	# Инициализирует игру и создает объект экрана.
	somevariable = True
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion ")	
	ship = Ship(screen)

	# Запуск основного цикла игры.
	while somevariable == True:
		# Отслеживание событий клавиатуры и мыши.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				somevariable = False

			screen.fill(ai_settings.bg_color)
			ship.blitme()

		# Отображение последнего прорисованного экрана.
		pygame.display.flip()

	pygame.quit()
	os._exit(1)

run_game()

