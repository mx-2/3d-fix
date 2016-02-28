# Risen 3 3D vision fix
========

This work in progress fix aims to make the game "Risen 3" 3D vision ready.
It is only tested with the 64bit version of the game.
Profile, based on Prototype, fixes a lot of halo issues.

#####What is fixed:
- HUD moved to depth
- Halos
- Shadows
- Point lights
- Sun, clouds
- Fog (approximate fix)

#####What is not fixed:
- Specular highlights
- Reflections in puddles and on crystals

#####Disabled effects:
- Sunrays

#####How to install the profile:

1. Download and run the GeForce 3D Profile Manager from here:
http://nvidia.custhelp.com/app/answers/detail/a_id/2625/kw/Profile

2. Delete the file nvdrssel.bin in the hidden directory C:/ProgramData/NVIDIA Corporation/Drs (it will be automatically created again after profile import)

3. Export your profiles the the profile manager.

4. Open the exported file in notepad and replace the existing Risen3 profile with that from the file risen3_profile.txt. If there is no existing profile just add it.

5. If nvdrssel.bin got created, delete it again!

6. Import the modified profile file.

