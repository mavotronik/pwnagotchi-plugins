from pwnagotchi.ui.components import LabeledValue, Text
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.plugins as plugins
import pwnagotchi
import logging
import requests

######  PROJECT IS UNDER CONSTRUCTOIN!!!!!!! ##########

class HaGet(plugins.Plugin):
    __author__ = 'https://github.com/mavotronik/pwnagotchi-plugins'
    __version__ = '1.0.0'
    __license__ = 'MIT'
    __description__ = 'A plugin that will get any data from your Home Assistant'

    def on_loaded(self):
        self.url = self.options.get('url', 'NOT SET')
        self.token = self.options.get('token', 'NOT SET')
        self.entities = self.options.get('entities', [])

        if isinstance(self.entities, str):
            self.entities = [self.entities]

        logging.info(f"HAGet: plugin loaded with settings: URL={self.url}, TOKEN={self.token}, ENTITIES={', '.join(self.entities)}")

    def on_unloaded(self):
        logging.info("HAGet: plugin unloaded.")

    def on_ui_update(self, ui):
        
        logging.info("HAGet: ui updated.")