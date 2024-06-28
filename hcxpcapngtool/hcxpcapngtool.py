import pwnagotchi.plugins as plugins
#import pwnagotchi.ui as ui
import pwnagotchi
import os
import json
import logging

class Hcxpcapngtool(plugins.Plugin):

    __author__ = 'https://github.com/mavotronik/pwnagotchi-plugins'
    __version__ = '1.0.0'
    __license__ = 'MIT'
    __description__ = 'A plugin that converts .pcap files to .hc22000 files'

    def on_loaded(self):
        logging.info("Hcxpcapngtool Plugin: loaded")

    def on_unloaded(self):
        logging.info("Hcxpcapngtool Plugin: unloaded")

    def on_handshake(self, agent, filename, access_point, client_station):
        logging.info("Hcxpcapngtool Plugin: New handshake" + filename + "captured!")
