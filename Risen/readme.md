# Risen 3D vision fix
========

This fix makes the game "Risen" 3D vision ready.

#####What is fixed:
- Halos in always everything
- Skybox and stars
- HUD moved to depth
- Shadows

#####Installation:
- Copy this folder structure into the directory which contains the Risen.exe (should be ./bin) so that "DX9Settings.ini" is in the same directory as the .exe. The screenshots directory is not needed.
- Get the HelixMod d3d9.dll from https://s3.amazonaws.com/-HeliX-/DLLS/DllsModPack1.zip (/DLLs/RELEASE/d3d9.dll) and put it in the same directory.

#####Configuration:
This fix has two presets for the HUD settings which can be selected with the numpad 9 and 3 keys. Preset 1 is the default after start. Preset 2 moves the HUD to higher depth and stretches it in X direction for better readability. The depths and amount of stretching can be configured with the Const1 and Const2 values in DX90Settings.ini.

#####Known issues:
- If convergence is increased far beyond 10, shadows move to wrong depth.
- Loading screens have red bars on the lief and right side.

#####Credits:
- bo3b for explaining the basics of shader fixing
  http://wiki.bo3b.net/index.php?title=Bo3b%27s_School_for_Shaderhackers
- HeliX for his dlls
