if starting:
	### Initial loading setups
	import sys
	
	# The script is launched through FreePie and Python is not aware of our custom script's folder. We add the script's folder path so we can load submodules later.
	script_path = 'D:\\Dev\\Projects\\FreePIE\\FreePIE_Joystick_Mapper\\'
	sys.path.append(script_path)
	
	# Reload our modules in order to acknowledge any modifications. Launch freepe script twice.
	from helpers.freepie_helper import reload_modules_from
	#import helpers.freepie_helper.reload_modules_from
	reload_modules_from(script_path)
	
	### Profile selection
	profiles = {
		1: 'DCS__FA_18',
		2: 'DCS__M2000C',
		3: 'Falcon4_BMS',
		4: 'IL2'
	}
	
	profile_selected = profiles[3]	# TO-DO: check profile exists
	
	from helpers.freepie_helper import KeyExtended
	
	for member in vars(KeyExtended):
		diagnostics.debug(member)
	
	diagnostics.debug(KeyExtended.B)
	diagnostics.debug("---------")
	#diagnostics.debug(FreePieTypeCheck.str_type_of(keyboard, joystick[0], vJoy[0]))

	K = KeyExtended.key_combination_constructor()
	diagnostics.debug(K( 'Right Alt + ;' ))
	diagnostics.debug(K( 'Left Shift + 1' ))
	diagnostics.debug(K( 'Left Control + Num 8' ))
	diagnostics.debug(K( 'Left control + Num 8' ))
	diagnostics.debug(K( 'Left control + Num *' ))
