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
	# Propagate important freepie vars to a centralized access that our modules will make use of.
	from src.helpers.freepie_vars    import FreePieVars
	from src.helpers.freepie_helper  import FreePieTypeCheck
	
	import atexit
	
	def exit_handler():
		diagnostics.notify('My application is ending!')
	
	#atexit.register(exit_handler)
	
	import signal

	def handle_exit():
		diagnostics.notify('My application is ending!')
	
	atexit.register(handle_exit)
	signal.signal(signal.SIGABRT, handle_exit)
	signal.signal(signal.SIGFPE, handle_exit)
	signal.signal(signal.SIGILL, handle_exit)
	signal.signal(signal.SIGINT, handle_exit)
	signal.signal(signal.SIGSEGV, handle_exit)
	signal.signal(signal.SIGINT, handle_exit)
	signal.signal(signal.SIGBREAK, handle_exit)
	
	FreePieVars.feed_with(joystick, vJoy, keyboard, Key, diagnostics, speech)
	
	diagnostics.debug(FreePieTypeCheck.py_str_type_of(joystick))
	diagnostics.debug(FreePieTypeCheck.py_str_type_of(vJoy))
	diagnostics.debug(FreePieTypeCheck.py_str_type_of(keyboard))
	diagnostics.debug(FreePieTypeCheck.py_str_type_of(Key))
	diagnostics.debug(FreePieTypeCheck.py_str_type_of(diagnostics))
	diagnostics.debug(FreePieTypeCheck.py_str_type_of(speech))
	FreePieTypeCheck.check_joystick(joystick)
	
# Loop commands