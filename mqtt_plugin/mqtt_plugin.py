import pwnagotchi.plugins as plugins
import pwnagotchi.ui as ui
import pwnagotchi
import os
import json
import logging
import paho.mqtt.client as mqtt

class MqttPlugin(plugins.Plugin):

    __author__ = 'https://github.com/mavotronik/pwnagotchi-plugins'
    __version__ = '1.0.1'
    __license__ = 'MIT'
    __description__ = 'A plugin that sends info about your pwnagotchi to MQTT'

    def __init__(self):
        host = self.options['host']
        topic = self.options['topic']

        super().__init__()
        self.client = mqtt.Client()
        self.client.connect(host, 1883, 60)

    def on_ui_update(self, ui):
        mem = f"{int(pwnagotchi.mem_usage() * 100)}"
        cpu_load = f"{int(pwnagotchi.cpu_load() * 100)}"
        temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1000
        points = len(os.listdir('/root/handshakes/'))
        

        self.client.publish(""topic"/mem", f"{mem}")
        self.client.publish(""topic"/cpu_load", f"{cpu_load}")
        self.client.publish(""topic"/temp", f"{temp}")
        self.client.publish(""topic"/points", f"{points}")


    def on_stats_update(self, stats):
        logging.info("MQTT Plugin: stats updated")

    def on_loaded(self):
        logging.info("MQTT Plugin: loaded")
        ui.set('face', '(✜‿‿✜)')
        ui.set('status', 'MQTT is ready!')

    def on_unloaded(self):
        logging.info("MQTT Plugin: unloaded")
        
