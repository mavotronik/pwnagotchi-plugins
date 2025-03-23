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
        self.url = self.options.get("url", "homeassistant.local")
        self.token = self.options.get("token", "your_longlive_token")
        self.entities = self.options.get("entities", [])
        self.num_entities_to_show = self.options.get("num_entities_to_show", 1)
        self.pos_x = self.options.get("pos_x")
        self.pos_y = self.options.get("pos_y")

        global headers
        headers = {
            "Authorization": f"Bearer {self.token}",
            "content-type": "application/json",}


        if isinstance(self.entities, str):
            self.entities = [self.entities]

        logging.info(f"HAGet: plugin loaded with settings: URL={self.url}, TOKEN={self.token}, ENTITIES={', '.join(self.entities)}  ")


    def on_internet_available(self, agent):
        global headers
        
        for i in range(self.num_entities_to_show):
            entity = (self.entities[i])
            #logging.info(f"HAGet: ")

            url = f"{self.url}/api/states/{entity}"
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                value = data['state']
                logging.info(f"HAGet: entity: {entity}, state value: {value}, url: {url}")
            else:
                logging.warning(f"Failed to fetch data: {response.status_code}")



    def on_ui_update(self, ui):
        pass
        #logging.info("HAGet: ui updated.")    
        
    def on_unloaded(self):
        logging.info("HAGet: plugin unloaded.")