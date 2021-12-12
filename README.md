
# FreePIE Joystick Mapper
A bundle of scripts that operates together to offer mapping functionalities to your joystick with the help of [FreePIE](http://andersmalmgren.github.io/FreePIE/) and [vJoy](https://sourceforge.net/projects/vjoystick/).

![Intro](./_res/intro.png)

## IMPORTANT: State of the project
Before going further, it is important to understand the state of this project. The project is currently **unmaintained and will probably be kept as is** (unless I feel a personnal need to correct something). It is **NOT a finished product** as per my final vision, but still in a functionning state.

The fate of the project comes from frustrations to work with FreePIE's constraints when I was trying to implement complex ideas. Most notably the inability to efficiently track back execution errors as the FreePIE's debug window would always show me wrong line numbers.

As I need a sane development environment I decided to stop the production of this project as it already fits a lot of needs and redo it with my own tools from scratch (upcoming project). In the meantime I decided to release the project to the public so anyone can explore it if desired.

The project is very well usable (a lot of effort was spent to control errors despite constraints): I use it myself for my gaming needs as you'll be able to see in the profiles folder. However, it is not totally documented and organized as I envisioned it. It is foremost meant for people who knows how to handle python (probably devs) and can see where I was going on with the design (profile building at the minimum).

**In summary** **the project is mainly meant for exploration and not for daily usage unless you can understand how it works**. The project is **NOT user friendly if you don't know anything in programming**.

## Basic concept of how this works
The project use profiles defined by an user to determine which mappins to do. A profile is defined in a single file and is found in the `profiles` folder. FreePIE will load a selected profile and everything else is automated.

## How to use
1. `main.py` found at the root of the project is the starting point you'll have to load inside FreePIE.
2. In this file you'll have to modify these lines:
   - Line 15: the variable `root_script_path` should set the path where `main.py` resides. Be careful of the backslash character: you need to use the escape character `\` (meaning double backslash is needed).
   - Line 18: the variable `profiles` holds a dictionary of all registered profiles. Construct the dictionary that fits the profiles selection you want to keep easily accessible.
   - Right after `profiles` variable: the `profile_selected` set the profile we currently want to load.
3. Run the script from FreePIE top menu: `Script -> Run script`. The console at the bottom and a Windows notification will tell you if the profile is correctly loaded.

## Be mindful of these limitations
- FreePIE is unable to find by itself the project's root where `main.py` and all of its scripts reside. That's why we have to help him by setting a variable as explained in the previous section.
- A profile file' name should not contain any dash (-) separator.
- Be mindful when doing code changes that FreePie executes on Python 2.7.
- If you want your code changes to be applied it is advised you restart FreePie to avoid any side effects since Python is holding references in memory while FreePie is running. This does not apply if you make profile changes, you can make change and they will be applied within one FreePie session.
- Multiple concurrent devices mapping is not possible. It was meant to happen, but it is still not fully implemented (work on it had already started).

## Project folders structure
- profiles: all the profiles describing desired mappings
    - tables: hand-made reference tables to describe a joystick' properties
- src: the source code of the automated scripts that FreePIE will use when it starts.
- tools: some additional utilites
    - _geogebra: contains a file which holds the mathematical expressions to construct a custom curve. It is usefal as you get a direct visual feedback by changing parameters.
    - _labs: a place where some testing was made for different purpose. It is kept as a future reference, but should not be used. Some parts probably doesn't work anymore.

## Profile structure
Take a look at `_SYNTAX_REFERENCE.txt` in the profiles folder and also take a look at a created profile to get an idea of how to build a mapping. The main idea is you create a joystick instance with `joy(joy_name, joy_axis_max)` and specify mappings on it. Once finished, you return the joystick instance.

Also the name of the function that describes the mappings is not important, the only constraint is that it must end with `_mapping`. The profile loader (src/loader/profile_loader.py) will handle the rest.

### Note on vJoy version mismatch
If you are using the vJoy driver version 2.1.9 (219), don't worry about the message in the console saying it doesn't match the DLL version (218). They are basically the same. 219 is just meant for Windows 10 compatibilty with no deep change. 219 driver is totally compatible with 218 DLL (provided by FreePIE).

## License

You can do as you please with the code. The project is released under the [MIT](./LICENSE.md) license.
