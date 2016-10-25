#### Useful tools and code snippets for 3D fixes

##### inverseMatrix.asm
Shader assembly implementation of the Gauss-Jordan elimination algorithm to calculate the inverse matrix. It utilizes the vector capabilities of the GPU for improved efficiency.

##### shaderVM.py:
Python script which interprets a shader assembly file and allows to look into the register values during execution. For debugging it uses some special pseudo instructions inside comments.

Currently supported instructions are def, mov, mul, add, sub, rcp, if_eq, else, endif as well as the two special debug instructions // PRINT and // SETR.
