from pwnagotchi.ui.components import LabeledValue, Text
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.plugins as plugins
import pwnagotchi
import logging
import requests

class HaGet(plugins.Plugin):
    __author__ = 'https://github.com/mavotronik/pwnagotchi-plugins'
    __version__ = '1.0.0'
    __license__ = 'MIT'
    __description__ = 'A plugin that will get any data from your Home Assistant'

    def on_loaded(self):
        self.url = self.options.get("url", "http://homeassistant.local")
        self.token = self.options.get("token", "your_longlive_token")
        self.entities = self.options.get("entities", [])
        self.num_entities_to_show = int(self.options.get("num_entities_to_show", 1))
        self.pos_text_1 = self.options.get("pos_text_1", (70, 60))
        self.pos_data_1 = self.options.get("pos_data_1", (70, 65))
        self.pos_text_2 = self.options.get("pos_text_2", (70, 70))
        self.pos_data_2 = self.options.get("pos_data_2", (70, 75))
        self.pos_text_3 = self.options.get("pos_text_3", (70, 80))
        self.pos_data_3 = self.options.get("pos_data_3", (70, 85))

        global headers
        headers = {
            "Authorization": f"Bearer {self.token}",
            "content-type": "application/json",
        }

        if isinstance(self.entities, str):
            self.entities = [self.entities]

        logging.info(f"HAGet: plugin loaded with settings: URL={self.url}, ENTITIES={', '.join(self.entities)}")
        logging.info(f"HAGet: Elements to add: {self.num_entities_to_show}, {self.positions}")

    def on_ui_setup(self, ui):
        logging.info("HAGet: on_ui_setup called")
        if self.num_entities_to_show:
            ui.add_element(f"ha_text_1", Text(color=BLACK, value="", position=(self.pos_text_1[0], self.pos_text_1[1]), font=fonts.Medium))
            ui.add_element(f"ha_data_1", Text(color=BLACK, value="", position=(self.pos_data_1[0], self.pos_data_1[1]), font=fonts.Medium))
            if self.num_entities_to_show == 2:
                ui.add_element(f"ha_text_2", Text(color=BLACK, value="", position=(self.pos_text_2[0], self.pos_text_2[1]), font=fonts.Medium))
                ui.add_element(f"ha_data_2", Text(color=BLACK, value="", position=(self.pos_data_2[0], self.pos_data_2[1]), font=fonts.Medium))
            elif self.num_entities_to_show == 3:
                ui.add_element(f"ha_text_3", Text(color=BLACK, value="", position=(self.pos_text_3[0], self.pos_text_3[1]), font=fonts.Medium))
                ui.add_element(f"ha_data_3", Text(color=BLACK, value="", position=(self.pos_data_3[0], self.pos_data_3[1]), font=fonts.Medium))
        else: 
            logging.warning("HAGet: Nothing to show. Please set num_entities_to_show parameter above 0")

    def on_internet_available(self, agent):
        global headers
        
        for i in range(self.num_entities_to_show):
            entity = self.entities[i] if i < len(self.entities) else None
            if not entity:
                continue

            url = f"{self.url}/api/states/{entity}"
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                value = data.get("state", "N/A")
                logging.info(f"HAGet: entity: {entity}, Value: {value}")
            else:
                logging.warning(f"HAGet: Failed to fetch data for {entity}: {response.status_code}")

    def on_ui_update(self, ui):
        pass  

    def on_unload(self, ui):
        logging.info("HAGet: plugin unloaded")
        
        with ui._lock:
            if self.num_entities_to_show:
                ui.remove_element(f"ha_text_1")
                ui.remove_element(f"ha_data_1")
                if self.num_entities_to_show == 2:
                    ui.remove_element(f"ha_text_2")
                    ui.remove_element(f"ha_data_2")
                elif self.num_entities_to_show == 3:
                    ui.remove_element(f"ha_text_3")
                    ui.remove_element(f"ha_data_3")
            else:
                logging.warning("HAGet: Nothing to remove.")
            
            