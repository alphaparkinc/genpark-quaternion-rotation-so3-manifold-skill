from client import QuaternionSO3

def main():
    print("=== Testing Quaternion SO(3) Manifold & SLERP ===")
    q_start = QuaternionSO3(1, 0, 0, 0) # identity
    q_end = QuaternionSO3(0, 1, 0, 0)   # 180 deg around x

    q_half = q_start.slerp(q_end, 0.5)
    print(f"SLERP at t=0.5: ({round(q_half.w, 4)}, {round(q_half.x, 4)}, {round(q_half.y, 4)}, {round(q_half.z, 4)})")

    assert abs(q_half.w - q_half.x) < 1e-4
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
