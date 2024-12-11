import math
from auio_conv import audd

def right_hand_check(lm12,lm14,lm16):
     # Get 3D coordinates
                p12 = (lm12.x, lm12.y, lm12.z)
                p14 = (lm14.x, lm14.y, lm14.z)
                p16 = (lm16.x, lm16.y, lm16.z)

                # Create vectors
                vector1 = (p14[0] - p12[0], p14[1] - p12[1], p14[2] - p12[2])  # 12 → 14
                vector2 = (p16[0] - p14[0], p16[1] - p14[1], p16[2] - p14[2])  # 14 → 16

                # Calculate dot product and magnitudes
                dot_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))
                magnitude1 = math.sqrt(sum(v**2 for v in vector1))
                magnitude2 = math.sqrt(sum(v**2 for v in vector2))

                # Avoid division by zero
                if magnitude1 > 0 and magnitude2 > 0:
                    # Calculate angle in radians
                    angle_rad = math.acos(dot_product / (magnitude1 * magnitude2))
                    # Convert to degrees
                    angle_deg = math.degrees(angle_rad)
                    print("🟡🟡🟡🟡🟡🟡")
                    print(f"right hand Angle: {angle_deg:.2f} degrees")



                    if 9 <= angle_deg <= 14:
                        return 1
                    else:
                        print("🔴🔴🔴🔴🔴🔴")
                        instreuction = "bring hands to sholder level"
                        audd(instreuction)
                        print(instreuction)

def left_hand_check(lm11,lm13,lm15):
     # Get 3D coordinates
                p11 = (lm11.x, lm11.y, lm11.z)
                p13 = (lm13.x, lm13.y, lm13.z)
                p15 = (lm15.x, lm15.y, lm15.z)

                # Create vectors
                vector1 = (p13[0] - p11[0], p13[1] - p11[1], p13[2] - p11[2])  # 11 → 13
                vector2 = (p15[0] - p13[0], p15[1] - p13[1], p15[2] - p13[2])  # 13 → 15

                # Calculate dot product and magnitudes
                dot_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))
                magnitude1 = math.sqrt(sum(v**2 for v in vector1))
                magnitude2 = math.sqrt(sum(v**2 for v in vector2))

                # Avoid division by zero
                if magnitude1 > 0 and magnitude2 > 0:
                    # Calculate angle in radians
                    angle_rad = math.acos(dot_product / (magnitude1 * magnitude2))
                    # Convert to degrees
                    angle_deg = math.degrees(angle_rad)
                    print("🟡🟡🟡🟡🟡🟡")
                    print(f"left hand Angle: {angle_deg:.2f} degrees")

                    if 55 <= angle_deg <= 67:
                        return 1
                    else:
                        print("🔴🔴🔴🔴🔴🔴")
                        instreuction = "bring hands to your sholder level"
                        audd(instreuction)
                        print(instreuction)

def right_leg_check(lm24,lm26,lm28):
     # Get 3D coordinates
                p24 = (lm24.x, lm24.y, lm24.z)
                p26 = (lm26.x, lm26.y, lm26.z)
                p28 = (lm28.x, lm28.y, lm28.z)

                # Create vectors
                vector1 = (p26[0] - p24[0], p26[1] - p24[1], p26[2] - p24[2])  # 24 → 26
                vector2 = (p28[0] - p26[0], p28[1] - p26[1], p28[2] - p26[2])  # 26 → 28

                # Calculate dot product and magnitudes
                dot_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))
                magnitude1 = math.sqrt(sum(v**2 for v in vector1))
                magnitude2 = math.sqrt(sum(v**2 for v in vector2))

                # Avoid division by zero
                if magnitude1 > 0 and magnitude2 > 0:
                    # Calculate angle in radians
                    angle_rad = math.acos(dot_product / (magnitude1 * magnitude2))
                    # Convert to degrees
                    angle_deg = math.degrees(angle_rad)
                    print("🟡🟡🟡🟡🟡🟡")
                    print(f"right leg Angle: {angle_deg:.2f} degrees")

                    if 55 <= angle_deg <= 67:
                        return 1
                    else:
                        print("🔴🔴🔴🔴🔴🔴")
                        instreuction = "bend the right leg down"
                        audd(instreuction)
                        print(instreuction)

def left_leg_check(lm23,lm25,lm27):
     # Get 3D coordinates
                p23 = (lm23.x, lm23.y, lm23.z)
                p25 = (lm25.x, lm25.y, lm25.z)
                p27 = (lm27.x, lm27.y, lm27.z)

                # Create vectors
                vector1 = (p25[0] - p23[0], p25[1] - p23[1], p25[2] - p23[2])  # 23 → 25
                vector2 = (p27[0] - p25[0], p27[1] - p25[1], p27[2] - p25[2])  # 25 → 27

                # Calculate dot product and magnitudes
                dot_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))
                magnitude1 = math.sqrt(sum(v**2 for v in vector1))
                magnitude2 = math.sqrt(sum(v**2 for v in vector2))

                # Avoid division by zero
                if magnitude1 > 0 and magnitude2 > 0:
                    # Calculate angle in radians
                    angle_rad = math.acos(dot_product / (magnitude1 * magnitude2))
                    # Convert to degrees
                    angle_deg = math.degrees(angle_rad)
                    print("🟡🟡🟡🟡🟡🟡")
                    print(f"left leg Angle: {angle_deg:.2f} degrees")

                    if 111 <= angle_deg <= 120:
                        return 1
                    else:
                        print("🔴🔴🔴🔴🔴🔴")
                        instreuction = "strighten your left leg"
                        audd(instreuction)
                        print(instreuction)

def right_hip_check(lm12,lm24,lm26):
     # Get 3D coordinates
                p12 = (lm12.x, lm12.y, lm12.z)
                p24 = (lm24.x, lm24.y, lm24.z)
                p26 = (lm26.x, lm26.y, lm26.z)

                # Create vectors
                vector1 = (p24[0] - p12[0], p24[1] - p12[1], p24[2] - p12[2])  # 12 → 24
                vector2 = (p26[0] - p24[0], p26[1] - p24[1], p26[2] - p24[2])  # 24 → 26

                # Calculate dot product and magnitudes
                dot_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))
                magnitude1 = math.sqrt(sum(v**2 for v in vector1))
                magnitude2 = math.sqrt(sum(v**2 for v in vector2))

                # Avoid division by zero
                if magnitude1 > 0 and magnitude2 > 0:
                    # Calculate angle in radians
                    angle_rad = math.acos(dot_product / (magnitude1 * magnitude2))
                    # Convert to degrees
                    angle_deg = math.degrees(angle_rad)
                    print("🟡🟡🟡🟡🟡🟡")
                    print(f"right hip Angle: {angle_deg:.2f} degrees")

                    if 5 <= angle_deg <= 15:
                        return 1
                    else:
                        print("🔴🔴🔴🔴🔴🔴")
                        instreuction = "bend a bit more"
                        audd(instreuction)
                        print(instreuction)

def left_hip_check(lm11,lm23,lm25):
     # Get 3D coordinates
                p11 = (lm11.x, lm11.y, lm11.z)
                p23 = (lm23.x, lm23.y, lm23.z)
                p25 = (lm25.x, lm25.y, lm25.z)

                # Create vectors
                vector1 = (p23[0] - p11[0], p23[1] - p11[1], p23[2] - p11[2])  # 11 → 23
                vector2 = (p25[0] - p23[0], p25[1] - p23[1], p25[2] - p23[2])  # 23 → 25

                # Calculate dot product and magnitudes
                dot_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))
                magnitude1 = math.sqrt(sum(v**2 for v in vector1))
                magnitude2 = math.sqrt(sum(v**2 for v in vector2))

                # Avoid division by zero
                if magnitude1 > 0 and magnitude2 > 0:
                    # Calculate angle in radians
                    angle_rad = math.acos(dot_product / (magnitude1 * magnitude2))
                    # Convert to degrees
                    angle_deg = math.degrees(angle_rad)
                    print("🟡🟡🟡🟡🟡🟡")
                    print(f"left hip Angle: {angle_deg:.2f} degrees")

                    if 5 <= angle_deg <= 15:
                        return 1
                    else:
                        print("🔴🔴🔴🔴🔴🔴")
                        instreuction = "bend a bit more"
                        audd(instreuction)
                        print(instreuction)