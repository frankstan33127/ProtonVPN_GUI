#!/usr/bin/python3
#Makes the sudo prompt appear so that protonvpn works. Protonvpn doesn't work until it is run as root
import subprocess
subprocess.call('pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY /home/$USER/ProtonVPN_GUI/protonvpn_gui.py', shell=True)
