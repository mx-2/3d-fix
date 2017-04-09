# Risen 3 3D vision fix
========

This fix aims to make the game "Risen 3" 3D vision ready.
It is only tested with the 64bit version of the game.
Profile, based on Prototype, fixes a lot of halo issues.

#####What is fixed:
- HUD and crosshair moved to depth
- Halos
- Shadows
- Point lights
- Sun, clouds
- Fog and Sunrays
- Specular highlights

#####What is not fixed:
- Ambient Occlusion (SSAO, seems to be unfixable)
  minor issue, can be disabled ingame with F4

#####Installation:
- Copy this folder structure into the directory which contains the Risen3.exe (should be ./system) so that "DX9Settings.ini" is in the same directory as the .exe. The screenshots directory is not needed.
- Get the HelixMod d3d9.dll from https://s3.amazonaws.com/-HeliX-/DLLS/DllsModPack1.zip (/DLLs/RELEASE/x64/d3d9.dll) and put it in the same directory.
- Install the Risen 3 profile (see below)

Alternatively download Risen3-3d-fix.7z in the downloads directory. It contains all necessary files.
However, the zip file does not always contain the lastest version of the fix.
Regardless of the used installation method the profile has to be installed manually.

#####Configuration:
HUD and crosshair depth can be configured with constants in DX9Settings.ini.
In the default configuration, the key 'R' cycles between three crosshair depths and
F4 can be used to disable SSAO which seems to be impossible from ingame options.

######How to install the profile:

1. Download and run the GeForce 3D Profile Manager from here:
http://nvidia.custhelp.com/app/answers/detail/a_id/2625/kw/Profile

2. Delete the file nvdrssel.bin in the hidden directory C:/ProgramData/NVIDIA Corporation/Drs (it will be automatically created again after profile import)

3. Export your profiles the the profile manager.

4. Open the exported file in notepad and replace the existing Risen3 profile with that from the file risen3_profile.txt. If there is no existing profile just add it.

5. If nvdrssel.bin got created, delete it again!

6. Import the modified profile file.

#####Changelog:
- v1.3: Added spell crosshair correction and changed default crosshair depth key to 'R'
- v1.2: Added missing crosshair correction
- v1.1: Added some missing shaders and added configuration
- v1.0: Initial release

#####Credits:
- bo3b for explaining the basics of shader fixing
  http://wiki.bo3b.net/index.php?title=Bo3b%27s_School_for_Shaderhackers
- DarkStarSword for his help with light and shadow fixes
- HeliX for his dlls

