import pwnagotchi.plugins as plugins
#import pwnagotchi.ui as ui
import pwnagotchi
import os
import logging
import subprocess

class Hcxpcapngtool(plugins.Plugin):

    __author__ = 'https://github.com/mavotronik/pwnagotchi-plugins'
    __version__ = '1.0.0'
    __license__ = 'MIT'
    __description__ = 'A plugin that converts .pcap files to .hc22000 files'

    def __init__(self):
        self.text_to_set = ""
    
    def on_loaded(self):
        logging.info("Hcxpcapngtool Plugin: loaded")
        if os.path.exists(self.options['hc_folder']):
            print("Hcxpcapngtool Plugin: hc directory is ok")
        else:
            print("Hcxpcapngtool Plugin: Creating hc dierectory . . .")
            subprocess.run(('sudo mkdir ' + self.options['hc_folder']), shell=True, stdout=subprocess.PIPE)

    def on_unloaded(self):
        logging.info("Hcxpcapngtool Plugin: unloaded")

    def on_handshake(self, agent, filename, access_point, client_station):
        logging.info("Hcxpcapngtool Plugin: New handshake " + filename + " captured!")
        
