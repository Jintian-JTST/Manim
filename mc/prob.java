private static float getHeightValue(SimplexNoise noise, int x, int z) {
    int chX = x / 2;
    int chZ = z / 2;
    int secX = x % 2;
    int secZ = z % 2;

    // Problematic part - integer overflow when x/z are too large
    float errorWithNaN = 100 - Mth.sqrt(x * x + z * z) * 8;
    errorWithNaN = Mth.clamp(errorWithNaN, -100, 80);

    /* Outer islands generation code */
    for (int iX = -12; iX <= 12; iX++) {
        for (int iZ = -12; iZ <= 12; iZ++) {
            long nX = (chX + iX);
            long nZ = (chZ + iZ);

            if (nX * nX + nZ * nZ > 4096 && noise.getValue(nX, nZ) < -0.9F) {
                float rnd = (Mth.abs(nX) * 3439 + Mth.abs(nZ) * 147) % 13 + 9;
                float gx = (secX - iX * 2);
                float gy = (secZ - iZ * 2);
                float islandDensity = 100 - Mth.sqrt(gx * gx + gy * gy) * rnd;
                islandDensity = Mth.clamp(islandDensity, -100, 80);
                errorWithNaN = Math.max(errorWithNaN, islandDensity);
            }
        }
    }
    return errorWithNaN;
}