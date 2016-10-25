//
// inverseMatrix.asm
//
// Matrix inversion with Gauss-Jordan elimination
// algorithm on GPU.
//
// This algorithm uses 128 instructions, from which
// 83 (best case) to 110 (worst case) are executed.
//
// input matrix is in r0-r3
// output will be in r4-r7
// r8, r9 are used as temporary registers
// c200 = (1,0,0,0) is required
//
// r0.x r0.y r0.z r0.w | r4.x, r4.y, r4.z, r4.w
// r1.x r1.y r1.z r1.w | r5.x, r5.y, r5.z, r5.w
// r2.x r2.y r2.z r2.w | r6.x, r6.y, r6.z, r6.w
// r3.x r3.y r3.z r3.w | r7.x, r7.y, r7.z, r7.w
//
// Test:
// SETR r0, 0, 2, 3, 4
// SETR r1, 1, 0, 5, 4
// SETR r2,-1, 2, 3, 4
// SETR r3, 0, 2, 3, 5
//
// Should produce
// r4 =  1.0,  0.0, -1.0,  0.0
// r5 =  1.6, -0.3, -0.3, -0.8
// r6 =  0.6,  0.2,  0.2, -0.8
// r7 = -1.0,  0.0,  0.0,  1.0
//

// Init registers
def c200, 1, 0, 0, 0
mov r4, c200.xyzw
mov r5, c200.wxyz
mov r6, c200.zwxy
mov r7, c200.yzwx

// Pivot first column
mov r8, c200
if_eq r0.x, r8.y
  if_eq r1.x, r8.y
    if_eq r2.x, r8.y
      mov r9, r0
      mov r0, r3
      mov r3, r9
      mov r9, r4
      mov r4, r7
      mov r7, r9
    else
      mov r9, r0
      mov r0, r2
      mov r2, r9
      mov r9, r4
      mov r4, r6
      mov r6, r9
    endif
  else
    mov r9, r0
    mov r0, r1
    mov r1, r9
    mov r9, r4
    mov r4, r5
    mov r5, r9
  endif
endif

// First column
rcp r8.x, r0.x
mul r8.y, r8.x, r1.x
mul r9, r0, r8.y
add r1, r1, -r9
mul r9, r4, r8.y
add r5, r5, -r9

mul r8.y, r8.x, r2.x
mul r9, r0, r8.y
add r2, r2, -r9
mul r9, r4, r8.y
add r6, r6, -r9

mul r8.y, r8.x, r3.x
mul r9, r0, r8.y
add r3, r3, -r9
mul r9, r4, r8.y
add r7, r7, -r9

// Pivot second column
mov r8, c200
if_eq r1.y, r8.y
  if_eq r2.y, r8.y
    mov r9, r1
    mov r1, r3
    mov r3, r9
    mov r9, r5
    mov r5, r7
    mov r7, r9
  else
    mov r9, r1
    mov r1, r2
    mov r2, r9
    mov r9, r5
    mov r5, r6
    mov r6, r9
  endif
endif

// Second column
rcp r8.x, r1.y
mul r8.y, r8.x, r2.y
mul r9, r1, r8.y
add r2, r2, -r9
mul r9, r5, r8.y
add r6, r6, -r9

mul r8.y, r8.x, r3.y
mul r9, r1, r8.y
add r3, r3, -r9
mul r9, r5, r8.y
add r7, r7, -r9

// Pivot third column
mov r8, c200
if_eq r2.z, r8.y
  mov r9, r2
  mov r2, r3
  mov r3, r9
  mov r9, r6
  mov r6, r7
  mov r7, r9
endif

// Third column
rcp r8.x, r2.z
mul r8.y, r8.x, r3.z
mul r9, r2, r8.y
add r3, r3, -r9
mul r9, r6, r8.y
add r7, r7, -r9

// Normalize r3.w
rcp r8.x, r3.w
mul r3, r3, r8.x
mul r7, r7, r8.x

// Fourth column
mul r8, r3, r2.w
mul r9, r7, r2.w
add r2, r2, -r8
add r6, r6, -r9

mul r8, r3, r1.w
mul r9, r7, r1.w
add r1, r1, -r8
add r5, r5, -r9

mul r8, r3, r0.w
mul r9, r7, r0.w
add r0, r0, -r8
add r4, r4, -r9

// Normalize r2.z
rcp r8.x, r2.z
mul r2, r2, r8.x
mul r6, r6, r8.x

// Third column (upper part)
mul r8, r2, r1.z
mul r9, r6, r1.z
add r1, r1, -r8
add r5, r5, -r9

mul r8, r2, r0.z
mul r9, r6, r0.z
add r0, r0, -r8
add r4, r4, -r9

// Normalize r1.y
rcp r8.x, r1.y
mul r1, r1, r8.x
mul r5, r5, r8.x

// Second column (upper part)
mul r8, r1, r0.y
mul r9, r5, r0.y
add r0, r0, -r8
add r4, r4, -r9

// Normalize first column
rcp r8.x, r0.x
mul r0, r0, r8.x
mul r4, r4, r8.x

