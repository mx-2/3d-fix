# ELEX 3D vision fix
========

This work in progress fix aims to make the game "ELEX" 3D vision ready.

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

#####What is not fixed yet:
- Everything not found

#####Known issues:
- Point lights are clipped at the left and right of the screen
- Ambient occlusion is a bit blurred when moving as this game used temporal blur.
  This can be disabled by pressing F3 in game.

#####Installation:
- Copy this folder structure into the directory which contains the ELEX.exe (should be ./system) so that "dxd3.ini" is in the same directory as the .exe.
- Download latest version of 3Dmigoto and copy d3d11.dll next to the ELEX.exe

#####Changelog:
- v1.1: Fixed HUD and some minor improvements
- v1.0: Initial Release

#####Credits:
- bo3b, DarkStarSword, Flugan and all others contributors for 3Dmigoto
- DarkStarSword for explanations on Frame Analysis, Tile Lighting and render target filtering

This fix is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Tested with ELEX v1.0 (GOG) on ultra setting and 1920x1080 resolution
on Windows 7 x64 with driver 358.87.

