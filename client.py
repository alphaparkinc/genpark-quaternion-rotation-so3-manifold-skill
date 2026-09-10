import math

class QuaternionSO3:
    """
    Unit Quaternion 3D Spatial Rotation & SLERP (Spherical Linear Interpolation).
    q = (w, x, y, z) with ||q|| = 1.
    """
    def __init__(self, w, x, y, z):
        norm = math.sqrt(w*w + x*x + y*y + z*z) or 1.0
        self.w = w / norm
        self.x = x / norm
        self.y = y / norm
        self.z = z / norm

    def dot(self, other):
        return self.w * other.w + self.x * other.x + self.y * other.y + self.z * other.z

    def slerp(self, other, t):
        d = self.dot(other)
        if d < 0.0:
            other = QuaternionSO3(-other.w, -other.x, -other.y, -other.z)
            d = -d
        d = min(1.0, max(-1.0, d))
        theta = math.acos(d)
        if math.sin(theta) < 1e-6:
            return QuaternionSO3(self.w, self.x, self.y, self.z)

        sin_t = math.sin(theta)
        w1 = math.sin((1.0 - t) * theta) / sin_t
        w2 = math.sin(t * theta) / sin_t
        return QuaternionSO3(
            w1 * self.w + w2 * other.w,
            w1 * self.x + w2 * other.x,
            w1 * self.y + w2 * other.y,
            w1 * self.z + w2 * other.z
        )
