import pwnagotchi.plugins as plugins
#import pwnagotchi.ui as ui
import pwnagotchi
import os
import logging
import subprocess
import time

class Hcxpcapngtool(plugins.Plugin):

    __author__ = 'https://github.com/mavotronik/pwnagotchi-plugins'
    __version__ = '1.0.0'
    __license__ = 'MIT'
    __description__ = 'A plugin that converts .pcap files to .hc22000 files'

    def __init__(self):
        self.text_to_set = ""
    
    def on_loaded(self):
        logging.info("Hcxpcapngtool Plugin: loaded")
        if os.path.exists("/root/hc"):
            logging.info("Hcxpcapngtool Plugin: [/root/hc] directory is ok")
        else:
            logging.info("Hcxpcapngtool Plugin: Creating [/root/hc] dierectory . . .")
            subprocess.run(('sudo mkdir /root/hc'), shell=True, stdout=subprocess.PIPE)
        time.sleep(10)
        logging.info("Hcxpcapngtool Plugin: Trying to convert .pcap-s")
        subprocess.run(('cd /root/handshakes && for f in *.pcap; do hcxpcapngtool "$f" -o "/root/hc/${f%.pcap}.hc22000"; done'), shell=True, stdout=subprocess.PIPE)

    
    def on_unloaded(self):
        logging.info("Hcxpcapngtool Plugin: unloaded")

    def on_handshake(self, agent, filename, access_point, client_station):
        logging.info("Hcxpcapngtool Plugin: New handshake " + filename + " captured! Converting . . .")
        #subprocess.run((f'hcxpcapngtool {filename} -o "/root/hc/${f%.pcap}.hc22000"'))
        
