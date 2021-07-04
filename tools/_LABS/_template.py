if starting:
	### ----------------------------------------------------------------------------------------------------
	###  Configuration zone.
	### ----------------------------------------------------------------------------------------------------
	
	# Specify here the full folder path where this script is stored.
	root_script_path = 'D:\\Dev\\Projects\\FreePIE\\FreePIE_Joystick_Mapper\\'

	### ----------------------------------------------------------------------------------------------------
	###  Environment setups.    (Must be setup before making any use of our modules)
	### ----------------------------------------------------------------------------------------------------
	
	# Inject the root path of this script to allow importation of our custom modules.
	import sys
	sys.path.append(root_script_path)

	# Reload our modules to acknolewdge modifications while FreePie is opened. Launch the script twice.
	from src.helpers.freepie_helper  import reload_modules_from
	reload_modules_from(root_script_path)

	### ----------------------------------------------------------------------------------------------------
	###  Lab zone.
	### ----------------------------------------------------------------------------------------------------
	from src.helpers.freepie_vars    import FreePieVars
	FreePieVars.feed_with(joystick, vJoy, keyboard, Key, diagnostics, speech)
	
	joy_name     = "X52 Professional H.O.T.A.S."
	joy_axis_max = 1000
	joy = joystick[joy_name]
	

# Loop commands