class Settings():
    
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
    	self.ship_speed_factor = 2.5
    	self.ship_limit = 3
    	self.screen_width = 1200
    	self.screen_height = 600
    	self.bg_color = (51, 51, 255)
    	self.bullet_speed_factor = 6
    	self.bullet_width = 3
    	self.bullet_height = 15
    	self.bullet_color = 60, 60, 60
    	self.bullets_allowed = 10
    	
    	# Alien settings
    	self.alien_speed_factor = 2
    	self.fleet_drop_speed = 10
    	# fleet_direction of 1 represents right; -1 represents left.
    	self.fleet_direction = 1