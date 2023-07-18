
# Plugin Setup
1. If you have not set up a directory for custom plugins, create the directory and add its path to your config.toml.
`main.custom_plugins = "/usr/local/share/pwnagotchi/custom-plugins/"`
2. Install dependencies
3. Put plugin to your custom folder
4. Restart pwnagotchi service
  
# Clockie
 - Displays time, date and info from mqtt topics . 
 - Testing on 1.5.5 official version.

# Dependencies
```
sudo apt install mosquitto mosquitto-clients && sudo pip3 install paho-mqtt==1.4.0
```

# Config.toml
```
no config yet
```
