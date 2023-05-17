#!/usr/bin/env bash
flock /tmp/pasystray.lock --command "pasystray" &
flock /tmp/nitrogen.lock --command "nitrogen --restore" &
flock /tmp/xscreensaver.lock --command "xscreensaver" &
# flock /tmp/xfce4-power-manager.lock --command "xfce4-power-manager" &
flock /tmp/dunst.lock --command "dunst" &
flock /tmp/picom.lock --command "picom" &
flock /tmp/rog.lock --command "rog-control-center" &
flock /tmp/shutter.lock --command "shutter --min_at_startup" &
flock /tmp/redshift.lock --command "redshift -t 5700:3600" &
