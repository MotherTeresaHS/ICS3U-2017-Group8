# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
from help_scene import *
from game_scene import *
from credit_scene import *

import ui


class MainMenuScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # set background image
        self.background = SpriteNode('./assets/sprites/bg.PNG',
        	                           position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)
                                     
        self.start_button = SpriteNode('./assets/sprites/Play_Button.PNG',
                                       parent = self,
                                       position = self.size/2,
                                       scale = 0.5)
                                       
                                        
        shop_button_position = self.size/2
        shop_button_position.y = shop_button_position.y - 170
        self.shop_button = SpriteNode('./assets/sprites/Shop_Button.PNG',
                                       parent = self,
                                       position = shop_button_position,
                                       scale = 0.5)
                                        
        credit_button_position = self.size/2
        credit_button_position.y = credit_button_position.y + 110
        self.credit_button = SpriteNode('./assets/sprites/Credits_Button.PNG',
                                        parent = self,
                                        position = credit_button_position,
                                        scale = 0.5)
         
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
         # if start button is pressed, goto game scene
       # if self.start_button.frame.contains_point(touch.location):
         #   self.present_modal_scene(GameScene())
            
        # if start button is pressed, goto game scene
        if self.shop_button.frame.contains_point(touch.location):
            self.present_modal_scene(HelpScene())
        
        if self.credit_button.frame.contains_point(touch.location):
            self.present_modal_scene(CreditScene())
        
        if self.start_button.frame.contains_point(touch.location):
            self.present_modal_scene(())
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
