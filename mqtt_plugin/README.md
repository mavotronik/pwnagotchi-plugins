# pwnagotchi-plugins

# Plugin Setup
If you have not set up a directory for custom plugins, create the directory and add its path to your config.toml.
`main.custom_plugins = "/usr/local/share/pwnagotchi/custom-plugins/"`
# MQTT plugin
 - Sends info about your Pwnagotchi to local MQTT broker. 
 - Tested on 1.5.5 official version.

```
sudo apt update && sudo apt install mosquitto mosquitto-clients && sudo pip3 install paho-mqtt==1.4.0
```
