import pwnagotchi.plugins as plugins
import pwnagotchi.ui as ui
import pwnagotchi
import os
import json
import logging
from gpiozero import Button

### USER SETTINGS ###
gpioPin = 21   # Button conected here
commands = 4   # Number of commands to execute (will be executed only up to this command)
hold_tme = 4.0 # time to hold button in seconds
### USER SETTINGS ###

held_for = 0.0
click = 0
hold = False

button = Button(gpioPin, hold_time=0.5, hold_repeat=False)

class multiclck(plugins.Plugin):

    __author__ = 'mavotronik'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'any disription'

                
    def on_loaded(self):
        logging.info("Multiclck: loaded")
        
    def on_ready(self, agent):
        global held_for
        global click
        
        click = 0
        held_for = 1
        
        logging.info("Multiclck: waiting for button")
    
    def onclick(self):
        global click
        global commands
        click = click + 1
        if (click > commands):
            click = 1
            
    def onheld(self):
        global held_for
        global hold_tme
        global hold
        held_for = max(held_for, button.held_time + button.hold_time + 1)
        if (held_for >= hold_tme):
            hold = True
            logging.info("Multiclck: button hold")
        else:
            hold = False
        

    def run_command(self):
        global hold
        global click
        if (hold == True):
           if (click == 1):
                logging.info("Multiclck: 1 mode")
           elif (click == 2):
                logging.info("Multiclck: 2 mode")
           elif (click == 3):
                logging.info("Multiclck: 3 mode")
           elif (click == 4):
                logging.info("Multiclck: 4 mode")
           elif (click == 5):
                logging.info("Multiclck: 5 mode")
           elif (click == 6):
                logging.info("Multiclck: 6 mode")
           else:
                logging.info("Multiclck: no mode")
                
          
    def on_ui_setup(self, ui):
        global hold
        global click
        ui.add_element('multiclckStatus',
                        LabeledValue(
                        color=BLACK,
                        label='MCS',
                        value='-',
                        position=(ui.width() - 42, ui.height() - 13),
                        label_font=fonts.Bold,
                        text_font=fonts.Medium
                        ))

    def on_ui_update(self, ui):
        global click
        ui.set('multiclckStatus', click)

        
    def on_unloaded(self):
        global button
        button.close()
        logging.info("Multiclck: unloaded")
        ui.remove_element('multiclckStatus')

    
#    button.is_pressed = onclick    
    button.when_pressed = onclick
    button.when_held = onheld
    button.when_released = run_command
