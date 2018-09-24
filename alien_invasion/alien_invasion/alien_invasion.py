import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

def run_game():
	# Initialize game and create a screen object
	pygame.init()
	ai_settings = Settings()
	
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# Create an instance to store game statistics and create a scorecard
	stats = GameStats(ai_settings)
	sb = ScoreBoard(ai_settings, screen, stats)
	
	# Make a ship, a group of bullets and a group of aliens
	ship = Ship(ai_settings, screen)
	
	bullets = Group()
	aliens = Group()
	# Create the fleet of aliens
	gf.create_fleet(ai_settings, screen, ship, aliens)
	play_button = Button(ai_settings, screen, "Play")
	
	
	# Start the main loop of the game
	while True:
		
		# Watch for keyboard and mouse events
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
		
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
		
run_game()
