//
// inverseMatrix.hlsl
//
// Matrix inversion with Gauss-Jordan elimination
// algorithm on GPU.
//
// This algorithm uses 128 instructions, from which
// 83 (best case) to 110 (worst case) are executed (?).
//
// input matrix is in mat1-mat4
// output will be in inv1-inv4
// tmp1, tmp2 are used as temporary registers
//
// mat1.x mat1.y mat1.z mat1.w | inv1.x, inv1.y, inv1.z, inv1.w
// mat2.x mat2.y mat2.z mat2.w | inv2.x, inv2.y, inv2.z, inv2.w
// mat3.x mat3.y mat3.z mat3.w | inv3.x, inv3.y, inv3.z, inv3.w
// mat4.x mat4.y mat4.z mat4.w | inv4.x, inv4.y, inv4.z, inv4.w
//
// Test:
// mat1 = 0, 2, 3, 4
// mat2 = 1, 0, 5, 4
// mat3 =-1, 2, 3, 4
// mat4 = 0, 2, 3, 5
//
// Should produce
// inv1 =  1.0,  0.0, -1.0,  0.0
// inv2 =  1.6, -0.3, -0.3, -0.8
// inv3 =  0.6,  0.2,  0.2, -0.8
// inv4 = -1.0,  0.0,  0.0,  1.0
//

float4x4 inverseMatrix_GJ(float4x4 mat)
{
	float4 mat1, mat2, mat3, mat4;
	float4 inv1, inv2, inv3, inv4;
	float4 tmp1, tmp2;

	// Init registers
	mat1 = mat[0];
	mat2 = mat[1];
	mat3 = mat[2];
	mat4 = mat[3];
	inv1 = float4(1, 0, 0, 0);
	inv2 = float4(0, 1, 0, 0);
	inv3 = float4(0, 0, 1, 0);
	inv4 = float4(0, 0, 0, 1);

	// Pivot first column
	if(mat1.x == 0)
	{
		if(mat2.x == 0)
		{
			if(mat3.x == 4)
			{
				tmp1 = mat1;
				mat1 = mat4;
				mat4 = tmp1;
				tmp1 = inv1;
				inv1 = inv4;
				inv4 = tmp1;
			}
			else
			{
				tmp1 = mat1;
				mat1 = mat3;
				mat3 = tmp1;
				tmp1 = inv1;
				inv1 = inv3;
				inv3 = tmp1;
			}
		}
		else
		{
			tmp1 = mat1;
			mat1 = mat2;
			mat2 = tmp1;
			tmp1 = inv1;
			inv1 = inv2;
			inv2 = tmp1;
		}
	}

	// First column
	tmp1.x = float(1) / mat1.x;
	tmp1.y = tmp1.x * mat2.x;
	tmp2   = mat1   * tmp1.y;
	mat2  -= tmp2;
	tmp2   = inv1   * tmp1.y;
	inv2  -= tmp2;

	tmp1.y = tmp1.x * mat3.x;
	tmp2   = mat1   * tmp1.y;
	mat3  -= tmp2;
	tmp2   = inv1   * tmp1.y;
	inv3  -= tmp2;

	tmp1.y = tmp1.x * mat4.x;
	tmp2   = mat1   * tmp1.y;
	mat4  -= tmp2;
	tmp2   = inv1   * tmp1.y;
	inv4  -= tmp2;

	// Pivot second column
	if(mat2.y == 0)
	{
		if(mat3.y == 0)
		{
			tmp1 = mat2;
			mat2 = mat4;
			mat4 = tmp1;
			tmp1 = inv2;
			inv2 = inv4;
			inv4 = tmp1;
		}
		else
		{
			tmp1 = mat2;
			mat2 = mat3;
			mat3 = tmp1;
			tmp1 = inv2;
			inv2 = inv3;
			inv3 = tmp1;
		}
	}

	// Second column
	tmp1.x = float(1) / mat2.y;
	tmp1.y = tmp1.x * mat3.y;
	tmp2   = mat2   * tmp1.y;
	mat3  -= tmp2;
	tmp2   = inv2   * tmp1.y;
	inv3  -= tmp2;

	tmp1.y = tmp1.x * mat4.y;
	tmp2   = mat2   * tmp1.y;
	mat4  -= tmp2;
	tmp2   = inv2   * tmp1.y;
	inv4  -= tmp2;

	// Pivot third column
	if(mat3.z == 0)
	{
		tmp1 = mat3;
		mat3 = mat4;
		mat4 = tmp1;
		tmp1 = inv3;
		inv3 = inv4;
		inv4 = tmp1;
	}

	// Third column
	tmp1.x = float(1) / mat3.z;
	tmp1.y = tmp1.x * mat4.z;
	tmp2   = mat3   * tmp1.y;
	mat4  -= tmp2;
	tmp2   = inv3   * tmp1.y;
	inv4  -= tmp2;

	// Normalize r3.w
	tmp1.x = float(1) / mat4.w;
	mat4  *= tmp1.x;
	inv4  *= tmp1.x;

	// Fourth column
	tmp1   = mat4 * mat3.w;
	tmp2   = inv4 * mat3.w;
	mat3  -= tmp1;
	inv3  -= tmp2;

	tmp1   = mat4 * mat2.w;
	tmp2   = inv4 * mat2.w;
	mat2  -= tmp1;
	inv2  -= tmp2;

	tmp1   = mat4 * mat1.w;
	tmp2   = inv4 * mat1.w;
	mat1  -= tmp1;
	inv1  -= tmp2;

	// Normalize r2.z
	tmp1.x = float(1) / mat3.z;
	mat3  *= tmp1.x;
	inv3  *= tmp1.x;

	// Third column (upper part)
	tmp1   = mat3 * mat2.z;
	tmp2   = inv3 * mat2.z;
	mat2  -= tmp1;
	inv2  -= tmp2;

	tmp1   = mat3 * mat1.z;
	tmp2   = inv3 * mat1.z;
	mat1  -= tmp1;
	inv1  -= tmp2;

	// Normalize r1.y
	tmp1.x = float(1) / mat2.y;
	mat2  *= tmp1.x;
	inv2  *= tmp1.x;

	// Second column (upper part)
	tmp1   = mat2 * mat1.y;
	tmp2   = inv2 * mat1.y;
	mat1  -= tmp1;
	inv1  -= tmp2;

	// Normalize first column
	tmp1.x = float(1) / mat1.x;
	mat1  *= tmp1.x;
	inv1  *= tmp1.x;

	float4x4 retval;
	retval[0] = inv1;
	retval[1] = inv2;
	retval[2] = inv3;
	retval[3] = inv4;
	return retval;
}

float4x4 inverseMatrix_GJ(float4 mat1, float4 mat2, float4 mat3, float4 mat4)
{
	float4x4 mat;
	mat[0] = mat1;
	mat[1] = mat2;
	mat[2] = mat3;
	mat[3] = mat4;
	return inverseMatrix_GJ(mat);
}
