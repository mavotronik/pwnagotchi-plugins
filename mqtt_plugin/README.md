
# Plugin Setup
1. If you have not set up a directory for custom plugins, create the directory and add its path to your config.toml.
`main.custom_plugins = "/usr/local/share/pwnagotchi/custom-plugins/"`
2. Install dependencies
3. Put plugin to your custom folder
4. Restart pwnagotchi service
  
# MQTT Plugin
 - Sends info about your Pwnagotchi to local MQTT broker. 
 - Tested on 1.5.5 official version.

# Dependencies
```
sudo apt install mosquitto mosquitto-clients && sudo pip3 install paho-mqtt==1.4.0
```

# Defaults
- MQTT host: ``localhost``
- Topic: ``pwnagotchi``
