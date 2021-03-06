# ELEX 3D vision fix
========

This fix aims to make the game "ELEX" 3D vision ready.

It is tested with ELEX v1.0.2946 (GOG) on ultra setting and 1920x1080 resolution
on Windows 7 x64 with driver 358.87.

** This fix may not work on Windows 10 or if the Evil Update (KB2670838) is installed! **

#####What is fixed:
- Shadows from sun 
- Point lights
- Sky and moon
- Decals
- Volumetric fog and light shafts
- Specular Highlights
- Smoke and water splash
- Rain
- HUD
- Auto crosshair

#####What is not fixed:
- Everything not found

#####Known issues:
- Point lights are clipped at the left and right of the screen
- Ambient occlusion is a bit blurred when moving as this game used temporal blur.
  This can be disabled by pressing F3 in game.
- Dialog boxes are clipped at the edges, especially on high HUD depths.

#####Installation:
- Copy this folder structure into the directory which contains the ELEX.exe (should be ./system) so that "dxd3.ini" is in the same directory as the .exe.
- Download latest version of 3Dmigoto and copy d3d11.dll next to the ELEX.exe

#####Hotkeys:
- F2 cycles between various HUD depths, however the HEX pattern is only correct at the standard depth
- F3 disables temporal part of ambient occlusion blur
- F4 cycles between two convergence presets, one for gameplay, one for MFD

#####Changelog:
- v1.5: Fixed some crash issues
- v1.4: Ported most fixes to ShaderRegex and updated the fix to patch 1.0.2946
- v1.3: Ported tile lighting fix to ShaderRegex to catch all missing shaders
        Decal fix now works at any resolution
        Menu HEX pattern fix now works on any resolution and HUD depth
- v1.2: Fixed rain, decals now work at any FoV, added auto-crosshair and added hotkeys
- v1.1: Fixed HUD and some minor improvements
- v1.0: Initial Release

#####Credits:
- bo3b, DarkStarSword, Flugan and all others contributors for 3Dmigoto
- DarkStarSword for explanations on Frame Analysis, Tile Lighting and render target filtering
- skr68 and DHR for tracking down the crash issues

This fix is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
