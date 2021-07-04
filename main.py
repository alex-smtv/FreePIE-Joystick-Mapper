#####################################################
## THIS FILE IS MEANT TO BE LOADED INSIDE FREEPIE! ##
#####################################################

try:
	if starting:
		# system.setThreadTiming(TimingTypes.HighresSystemTimer)
		# system.threadExecutionInterval = 1
		
		### ----------------------------------------------------------------------------------------------------
		###  Configuration zone.
		### ----------------------------------------------------------------------------------------------------
		
		# Specify here the full folder path where this script is stored.
		root_script_path = 'D:\\Dev\\Projects\\FreePIE\\FreePIE_Joystick_Mapper\\'
	
		# List here all profiles you want to keep track. IMPORTANT: due to a limitation, files' name should not contain any dash (-) separator.
		profiles = {
			# DCS AIRCRAFT
			100: 'DCS__FA_18C',
			101: 'DCS__Mirage_2000C',
			102: 'DCS__A10C_II',
			
			# DCS HELICOPTER
			200: 'DCS__Huey_UH_1H',
			201: 'DCS__Gazelle_SA342',
			202: 'DCS__KA_50',
			203: 'DCS__Mi8_MTV2',
			204: 'DCS__Mi24P_Hind',
			
			# Falcon BMS
			400: 'Falcon4_BMS',

			# IL2
			500: 'IL2',

			# Microsoft Flight Simulator 2020
			600: 'MSFS_Global',
			
			# Star Citizen
			700: 'Star Citizen',
			
			# Star Wars Squadrons
			800: 'Star_Wars_Squadrons',
			
			# X4 Foundations
			900: 'X4',
			
			# Generic
			1000: 'VJOY_1_to_1'
		}
		
		# Select here the profile you want to load.
		profile_selected = profiles[204]
	
		### ----------------------------------------------------------------------------------------------------
		###  Environment setups.    (Must be setup before making any use of our modules)
		### ----------------------------------------------------------------------------------------------------
		
		# Inject the root path of this script to allow importation of our custom modules.
		import sys
		sys.path.append(root_script_path)
	
		# DON'T TOUCH - THIS WAS USED BEFORE, BUT NOT USED ANYMORE (kept as a reference)
		# Reload our modules to acknolewdge modifications while FreePie is opened. Launch the script twice.
		#from helpers.freepie_helper  import reload_modules_from
		#reload_modules_from(root_script_path)
	
		# Propagate important freepie vars to a centralized access that our modules will make use of.
		from src.helpers.freepie_vars    import FreePieVars
		FreePieVars.feed_with(joystick, vJoy, keyboard, Key, diagnostics, speech)
	
		### ----------------------------------------------------------------------------------------------------
		###  Mappings setups.
		### ----------------------------------------------------------------------------------------------------
		from src.loader.profile_loader import ProfileLoader
	
		# Profile loading
		profile = ProfileLoader(profile_selected)
		
	profile.loop_apply_mappings()
	
except Exception as e:
	diagnostics.notify("Freepie script error, aborting...")
	raise e
