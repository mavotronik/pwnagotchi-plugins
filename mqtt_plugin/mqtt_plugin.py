import pwnagotchi.plugins as plugins
import pwnagotchi.ui as ui
import pwnagotchi
import os
import json
import logging
import paho.mqtt.client as mqtt

class MqttPlugin(plugins.Plugin):

    __author__ = 'mavotronik'
    __version__ = '1.0.0'
    __license__ = 'GPL3'
    __description__ = 'A plugin that sends info about your pwnagotchi to mqtt'

    def __init__(self):
        self.options = {
        'host': 'localhost',
        'topic': 'pwnagotchi'
        }
        
        super().__init__()
        self.client = mqtt.Client()
        self.client.connect("localhost", 1883, 60)

    def on_ui_update(self, ui):
        mem = f"{int(pwnagotchi.mem_usage() * 100)}"
        cpu_load = f"{int(pwnagotchi.cpu_load() * 100)}"
        temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1000
        points = len(os.listdir('/root/handshakes/'))
        
#        self.mqtt_publish()
        self.client.publish("pwnagotchi/mem", f"{mem}")
        self.client.publish("pwnagotchi/cpu_load", f"{cpu_load}")
        self.client.publish("pwnagotchi/temp", f"{temp}")
        self.client.publish("pwnagotchi/points", f"{points}")


    def on_stats_update(self, stats):
        logging.info("MqttPlugin: stats updated")

    def on_loaded(self):
        logging.info("MqttPlugin: loaded")
        ui.set('face', '(✜‿‿✜)')
        ui.set('status', 'MQTT is ready!')

    def on_unloaded(self):
        logging.info("MqttPlugin: unloaded")
        
#    def mqtt_publish(self):
#        self.client.publish("pwnagotchi/mem", f"{mem}")
#        self.client.publish("pwnagotchi/cpu_load", f"{cpu_load}")
#        self.client.publish("pwnagotchi/temp", f"{temp}")
#        self.client.publish("pwnagotchi/points", f"{points}")
