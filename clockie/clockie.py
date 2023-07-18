#import pwnagotchi.ui.components
from pwnagotchi.ui.components import LabeledValue, Text
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.plugins as plugins
import pwnagotchi
import logging
import datetime
import paho.mqtt.client as mqtt


class clockie(plugins.Plugin):
    __author__ = 'https://github.com/mavotronik/pwnagotchi-plugins'
    __version__ = '0.0.4'
    __license__ = 'MIT'
    __description__ = 'A plugin displays a clock and other info'
    
    def on_loaded(self):
        logging.info("clockie: plugin loaded")
        
    def on_ready(self, agent):
        pass
        
        
    def on_ui_setup(self, ui):
        # ui.add_element('clockie_w', Text(color=BLACK, value='c',position=(ui.width() - 42, ui.height() - 13), font=fonts.Medium))
        ui.add_element('clock', Text(color=BLACK, value='',position=(150, 56), font=fonts.Medium))
        ui.add_element('clock_mqtt_1', Text(color=BLACK, value='',position=(145, 85), font=fonts.Medium))
        ui.add_element('clock_mqtt_2', Text(color=BLACK, value='',position=(175, 85), font=fonts.Medium))
                
    def on_ui_update(self, ui):
        dt_now = datetime.datetime.now()
        # time_rn = dt_now.strftime("%d/%m/%y" + "\n%H:%M:%S")  #with seconds
        time_rn = dt_now.strftime("%d/%m/%y" + "\n%H:%M")   #no seconds
        ui.set('clock', time_rn)
        ui.set('clock_mqtt_1', "#")
        ui.set('clock_mqtt_2', "#")
        # remove_all()
        with ui._lock:
            # ui.remove_element('bluetooth')
            ui.remove_element('memtemp')
            ui.remove_element('latitude')
            ui.remove_element('longitude')
            ui.remove_element('altitude')
            # ui.remove_element('aps')
            # ui.remove_element('channel')
            # ui.remove_element('uptime')
        
          
    def on_unload(self, ui):
        logging.info("clockie: plugin unloaded")
        with ui._lock:
            ui.remove_element('clock')
            ui.remove_element('clock_mqtt_1')
            ui.remove_element('clock_mqtt_2')
            # ui.remove_element('clockie_w')
            
    # def remove_all(ui):
        # logging.info("clockie: removing all")
        # with ui._lock:
            # # ui.remove_element('bluetooth')
            # ui.remove_element('memtemp')
            # ui.remove_element('latitude')
            # ui.remove_element('longitude')
            # ui.remove_element('altitude')
            # # ui.remove_element('aps')
            # # ui.remove_element('channel')
            # # ui.remove_element('uptime')
            
            