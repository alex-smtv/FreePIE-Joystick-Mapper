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
	from helpers.freepie_helper  import reload_modules_from
	reload_modules_from(root_script_path)

	### ----------------------------------------------------------------------------------------------------
	###  Lab zone.
	### ----------------------------------------------------------------------------------------------------
	# Propagate important freepie vars to a centralized access that our modules will make use of.
	from helpers.freepie_vars    import FreePieVars
	from helpers.freepie_helper  import FreePieTypeCheck
	import utils.filters
	
	FreePieVars.feed_with(joystick, vJoy, keyboard, Key, diagnostics, speech)
	
	#for key in dir(utils.filters):
	#	diagnostics.debug(key)
	
	for key in dir(utils.filters):
		if callable(key):
			diagnostics.debug(key)
		#if key.endswith('Filter'):
		#	diagnostics.debug(key)
	
# Loop commands