# Risen 2 3D vision fix
========

This fix makes the game "Risen 2" 3D vision ready.

#####What is fixed:
- Stars
- Water reflections
- Crosshair moved to depth
- HUD moved to depth
- Shadows
- Point lights without shadows
- Point lights with shadows (by DarkStarSword)
- Specular highlights

#####Installation:
- Copy this folder structure into the directory which contains the Risen.exe (should be ./system) so that "DX9Settings.ini" is in the same directory as the .exe. The screenshots directory is not needed.
- Get the HelixMod d3d9.dll from https://s3.amazonaws.com/-HeliX-/DLLS/DllsModPack1.zip (/DLLs/RELEASE/d3d9.dll) and put it in the same directory.

Alternatively download Risen2-3d-fix.7z in the downloads directory. It contains all necessary files.
However, the zip file does not always contain the lastest version of the fix.

#####Known issues:
- When starting the game, there are flickering edges in the main menu.

#####Changelog:
- v1.0: Initial release

#####Credits:
- bo3b for explaining the basics of shader fixing
  http://wiki.bo3b.net/index.php?title=Bo3b%27s_School_for_Shaderhackers
- DarkStarSword for his help with light and shadow fixes
- HeliX for his dlls
