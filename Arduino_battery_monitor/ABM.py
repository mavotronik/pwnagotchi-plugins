from pwnagotchi.ui.components import LabeledValue, Text
from pwnagotchi.ui.view import BLACK
import pwnagotchi.ui.fonts as fonts
import pwnagotchi.plugins as plugins
import pwnagotchi
import logging
import serial


class ABM(plugins.Plugin):
    __author__ = 'https://github.com/mavotronik/pwnagotchi-plugins'
    __version__ = '1.0.0'
    __license__ = 'MIT'
    __description__ = 'Plugin that will get info about ur battery from arduino'

    def on_loaded(self):
        self.port = self.options.get("port", "/dev/ttyS0")
        self.baudrate = int(self.options.get("baudrate", "9600"))
        self.mode_to_show = self.options.get("mode_to_show", "voltage")
        self.pos_text = tuple(map(int, self.options.get("pos_text", "150,74").split(",")))
        self.pos_data = tuple(map(int, self.options.get("pos_data", "180,75").split(",")))

        logging.info(f"ABM: plugin loaded with settings: PORT={self.port}, SPEED={self.baudrate}, show: {self.mode_to_show}")
        logging.info(f"POSITIONS: pos_text: {self.pos_text}, pos_data: {self.pos_data}")

        self.serial = serial.Serial()
        self.serial.port = self.port
        self.serial.baudrate = self.baudrate

    def on_ui_setup(self, ui):
        logging.info("ABM: on_ui_setup called")
        ui.add_element(f"text", Text(color=BLACK, value="BATT:", position=(self.pos_text[0], self.pos_text[1]), font=fonts.Small))
        ui.add_element(f"data", Text(color=BLACK, value="-", position=(self.pos_data[0], self.pos_data[1]), font=fonts.Small))
    
    def on_ui_update(self, ui):
        # logging.info("ABM: on_ui_update called")
        
        raw_data = self.get_data()

        if not raw_data:
            logging.warning("ABM: No data received, skipping update")
            return
        
        voltage = raw_data[0]
        charge_status = raw_data[2]

        if self.mode_to_show == "voltage":
            data_to_display = f"{voltage}V | {'CH' if charge_status == '1' else 'DCH'}"
            
        elif self.mode_to_show == "percent":
            percents = self.batt_to_percent(float(voltage))
            data_to_display = f"{percents:.0f}% | {'CH' if charge_status == '1' else 'DCH'}"

        logging.info(f"ABM: data to show {data_to_display}")
        ui.set("data", data_to_display)

    def on_unload(self, ui):
        with ui._lock:
            try:
                ui.remove_element("text")
                ui.remove_element("data")
                logging.info("ABM: plugin unloaded succsesfully")
            except Exception as e:
                logging.info("ABM: plugin unloaded. Failed to remove UI elements")
        

            
    def get_data(self):
        try:
            self.serial.open()
            line = self.serial.readline().decode("utf-8").split(",")
            self.serial.close()
        
            data = [item.strip() for item in line]

            if len(data) != 5:
                logging.warning(f"ABM: Incomplete data received: {data}")
                return
        
            # logging.info(f"ABM: Raw data: {data}")
            return data

        except Exception as e: 
            logging.error(f"ABM: Err: {e}")

    def batt_to_percent(self, value, in_min=3.0, in_max=4.2, out_min=0, out_max=100):
        
        if value < in_min:
            value = in_min
        elif value > in_max:
            value = in_max
    
        scaled_value = ((value - in_min) / (in_max - in_min)) * (out_max - out_min) + out_min
        return scaled_value
