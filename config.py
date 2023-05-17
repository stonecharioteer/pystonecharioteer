import subprocess
import json
import os
from stonecharioteer.qtile import config
from libqtile import hook
from libqtile.log_utils import logger

config_file = os.path.expanduser("~/.config/qtile/stonecharioteer.json")

with open(config_file) as f:
    cfg = json.load(f)

c = config(cfg)

mod = c["mod"]
groups = c["groups"]
terminal = c["terminal"]
layouts = c["layouts"]
screens = c["screens"]
keys = c["keys"]
dgroups_key_binder = c["dgroups_key_binder"]
dgroups_app_rules = c["dgroups_app_rules"]
follow_mouse_focus = c["follow_mouse_focus"]
bring_front_click = c["bring_front_click"]
cursor_warp = c["cursor_warp"]
auto_minimize = c["auto_minimize"]

@hook.subscribe.startup
def dbus_register():
   logger.info("Attempting to run startup script.")
   desktop_autostart_id = os.environ.get('DESKTOP_AUTOSTART_ID')
   autostart_script = os.path.expanduser("~/.config/qtile/autostart.sh")
   subprocess.Popen([autostart_script])
   logger.info("Successfully executed startup script.")

   logger.info("Attempting to start gnome session manager")
   # if not desktop_autostart_id:
   #    logger.warning("`DESKTOP_AUTOSTART_ID` not set. Not running startup script.")
   #    return
   desktop_autostart_id = desktop_autostart_id or 1

   subprocess.Popen(['dbus-send',
                     '--session',
                     '--print-reply',
                     '--dest=org.gnome.SessionManager',
                     '/org/gnome/SessionManager',
                     'org.gnome.SessionManager.RegisterClient',
                     'string:qtile',
                     'string:' + str(desktop_autostart_id)])
   logger.info("Started gnome session manager")
