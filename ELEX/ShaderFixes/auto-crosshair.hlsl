// Auto crosshair code from https://github.com/bo3b/3Dmigoto/wiki/Auto-Crosshair
// ported to ELEX

float world_z_from_depth_buffer(float x, float y)
{
	uint width, height;
	float z;

	DepthBuffer.GetDimensions(width, height);

	x = min(max((x / 2 + 0.5) * width, 0), width - 1);
	y = min(max((-y / 2 + 0.5) * height, 0), height - 1);
	z = DepthBuffer.Load(int3(x, y, 0));
	if (z == 1)
		return 0;

	// Derive world Z from depth buffer. This is a kluge since I don't know
	// the correct scaling, and the Z buffer seems to be (1 - what I expected).
	// Might be able to determine the correct way to scale it from other shaders.
	return m_fFar*m_fNear/(((1-z)*m_fNear) + (m_fFar*z));
}

float adjust_from_depth_buffer(float x, float y)
{
	float4 stereo = StereoParams.Load(0);
	float separation = stereo.x; float convergence = stereo.y;
	float old_offset, offset, w, sampled_w, distance;
	uint i;

	// Stereo cursor: To improve the accuracy of the stereo cursor, we
	// sample a number of points on the depth buffer, starting at the near
	// clipping plane and working towards original x + separation.
	//
	// You can think of this as a line in three dimensional space that
	// starts at each eye and stretches out towards infinity. We sample 255
	// points along this line (evenly spaced in the X axis) and compare
	// with the depth buffer to find where the line is first intersected.
	//
	// Note: The reason for sampling 255 points came from a restriction in
	// DX9/SM3 where loops had to run a constant number of iterations and
	// there was no way to set that number from within the shader itself.
	// I'm not sure if the same restriction applies in DX11 with SM4/5 - if
	// it doesn't, we could change this to check each pixel instead for
	// better accuracy.
	//
	// Based on DarkStarSword's stereo crosshair code originally developed
	// for Miasmata, adapted to Unity, then translated to HLSL.

	// ELEX needs convergence scaled by m_fFar
	offset = (m_fNear - convergence/m_fFar) * separation;	// Z = X offset from center
	distance = separation - offset;			// Total distance to cover (separation - starting X offset)

	old_offset = offset;
	for (i = 0; i < 255; i++) {
		offset += distance / 255.0;

		// Calculate depth for this point on the line:
		w = (separation * convergence) / (separation - offset);

		sampled_w = world_z_from_depth_buffer(x + offset, y);
		// This does not for for ELEX.
		//if (sampled_w == 0)
		//	return 0;

		// If the sampled depth is closer than the calculated depth,
		// we have found something that intersects the line, so exit
		// the loop and return the last point that was not intersected:
		if (w > sampled_w)
			break;

		old_offset = offset;
	}

	return old_offset;
}
