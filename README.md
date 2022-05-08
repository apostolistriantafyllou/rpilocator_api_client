# rpilocator api client
a stockcheck client for my modified version of the raspberry pi locator api that checks every 60 minutes and sends you a notification if any are found. DESIGNED FOR WINDOWS

# Installation instructions
1. set up [rpilocator_api](https://github.com/apostolistriantafyllou/rpilocator_api/)
2. run `pip install win10toast_click ast requests time webbrowser`
3. download main.py and put your rpilocator api address in the apiurl variable
4. create a shortcut in shell:startup(put that in explorer path bar) pointing to pythonw.exe(pythonw is python but background(without cmd)), then a space and then main.py's path
5. either reboot your computer or double click the shortcut
