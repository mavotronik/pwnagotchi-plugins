# Plugin Setup
1. If you have not set up a directory for custom plugins, create the directory and add its path to your config.toml.
`main.custom_plugins = "/usr/local/share/pwnagotchi/custom-plugins/"`
2. Install dependencies
3. Put plugin to your custom folder
4. Edit your config.toml
5. Restart pwnagotchi service

# Memtemp_adv Plugin
 - Displays CPU, RAM, disk usage, CPU temperature. Support waveshare v3  
 - Tested on 1.5.5 official version and 1.5.5FIX.

# Dependencies

```
sudo pip3 install psutil==5.4.7
```

# Config.toml
```
main.plugins.memtemp_adv.enabled = true
main.plugins.memtemp_adv.scale = "celsius"
main.plugins.memtemp_adv.orientation = "horizontal"
```
