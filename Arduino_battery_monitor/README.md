# Plugin Setup
1. If you have not set up a directory for custom plugins, create the directory and add its path to your config.toml.
`main.custom_plugins = "/usr/local/share/pwnagotchi/custom-plugins/"`
2. Install dependencies
3. Put plugin to your custom folder
4. Edit your config.toml
5. Restart pwnagotchi service

# ABM
- Displays data about charge from arduino
- Tested on 1.5.5

# Dependencies
```
sudo pip3 install pyserial==3.5
```

# Config.toml
```
main.plugins.ABM.enabled = true
main.plugins.ABM.port = "/dev/ttyS0"
main.plugins.ABM.baudrate = 9600
main.plugins.ABM.mode_to_show = "percent"
main.plugins.ABM.pos_text = "150, 74"
main.plugins.ABM.pos_data = "180, 75"
```
