#####################################################
## THIS FILE IS MEANT TO BE LOADED INSIDE FREEPIE! ##
#####################################################

try:
	if starting:
		# Specify here the full folder path where this script is stored.
		root_script_path = "D:\Dev\Projects\FreePIE\FreePIE_Joystick_Mapper"
		
		### ----------------------------------------------------------------------------------------------------
		###  Configuration zone.
		### ----------------------------------------------------------------------------------------------------
		
		# The following two system lines can be tweaked. These values fits me, but these lines can be removed
		# if the software is struggling (slow operations). Originaly these lines were not present.
		# More explanation here: https://www.mtbs3d.com/phpbb/viewtopic.php?t=18724
		system.setThreadTiming(TimingTypes.HighresSystemTimer)
		system.threadExecutionInterval = 13
		
		# Inject the root path of this script to allow importation of our custom modules.
		import sys
		sys.path.append(root_script_path)
	
		# Propagate important freepie vars to a centralized access that our modules will make use of.
		from src.helpers.freepie_vars    import FreePieVars
		FreePieVars.feed_with(root_script_path, joystick, vJoy, keyboard, Key, diagnostics, speech)
	
		### ----------------------------------------------------------------------------------------------------
		###  Mappings setups.
		### ----------------------------------------------------------------------------------------------------
		from src.loader.profile_loader import ProfileLoader
	
		# Handle for profiles loading
		profile = ProfileLoader()
		
	profile.loop_apply_mappings()
	
except Exception as e:
	message = "FreePIE script error, aborting..."
	diagnostics.notify(message)
	diagnostics.debug(message)
	raise e
