import math

triangle = math.degrees(float(input("Angle: ")))

print(f"\033[38m•Cosine\033[34m...:{math.cos(triangle):.10f}")
print(f"\033[38m•Tangent\033[34m..:{math.tan(triangle):.10f}")
print(f"\033[38m•Sine\033[34m.....:{math.sin(triangle):.10f}")
