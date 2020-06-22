# PROTONVPN_GUI
A simple and basic ProtonVPN GUI for linux. Made using python.

## Instructions 

1. git clone to your **home/user** directory. Or any directory you wish but you will then have to change the paths in the **.desktop** and python files.

2. Make the **ProtonVPN.desktop** executable by right-clicking and going to **Properties**, if it isn't executable already.

3. Make the **protonvpn_gui.py** and **run.py** executable in the same manner too.

4. Edit the **.desktop** files using a text editor and change the **'ICON'** path. More details are in the **.desktop** file. 
And you can place the .desktop file anywhere you wish.

5. Now before you start running, make sure you have the following :
 
  i. **protonvpn**, which can be installed with `sudo pip3 install protonvpn-cli` in your terminal.
  
  ii. **initiate protonvpn** with `sudo protonvpn init` and enter your **OpenVPN** in your terminal. 
  Further instructions can be found at [Proton VPN Official Page](https://protonvpn.com/support/linux-vpn-tool/)
 
  iii. Install the tkinter for your respective distro. It should be `sudo apt install python3-tk` for Debian/Ubuntu systems and 
  for Arch/Manjaro it should be `sudo pacman -S tk`.   You can google it for your respective distro.
 
  iv. Install subprocess library if it isn't already install. (Again just google it for your distro)
 
 **NOTE :** If the program isn't working, try running **protonvpn_gui.py** from terminal as `sudo python3 protonvpn_gui.py` and if you are getting 
 the error `_tkinter.TclError: unknown color name "BACKGROUND"` then try typing `xrdb -load /dev/null` and run it again. If it works now, then 
 you will have to add this line `subprocess.call('xrdb -load /dev/null',shell=True)` to run.py and see if you can run it without the terminal now.
 
 **NOTE :** For now it connects to the fastest server by default. I will be adding more connection features in the future and more options will be soon
 available as well. You are most welcome to add more features to this yourself and modify, recreate and/or reproduce this if you wish. 
 The icon was created by myself.
 
 
 
 
 
 
 
 
 
