# Sidenote for X52 Pro users

The throttle wheel up/down/click and mouse click won't be recognized for custom mapping with FreePie while the Logitech or default Saitek driver for the device is installed and active. Uninstalling the corresponding driver is a necessary step if you want to apply custom mapping to these entities. Another better solution is to use [HidHide](https://github.com/ViGEm/HidHide).

## Using HidHide
Globally hide your X52 device except for:

- Program Files (x86)\FreePIE\FreePIE.exe : allow FreePIE to see your device
- Program Files\Logitech\X52 Professional\ST.exe : Logitech driver & software
- Program Files\Logitech\X52 Professional\X52Pro_Profiler.exe : Logitech driver & software
- Windows\System32\rundll32.exe : allow your device to appear to the game controllers window (Win + R and type joy.cpl)