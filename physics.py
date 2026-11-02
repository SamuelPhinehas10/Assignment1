print("===== PHYSICS FORMULA CALCULATOR =====")

# 1. PRESSURE
print("\n1. PRESSURE")
force = float(input("Enter force in Newtons: "))
area = float(input("Enter area in square metres: "))
pressure = force / area
print("Pressure =", pressure, "Pa")

# 2. DENSITY
print("\n2. DENSITY")
mass = float(input("Enter mass in kg: "))
volume = float(input("Enter volume in cubic metres: "))
density = mass / volume
print("Density =", density, "kg/m3")

# 3. WORK DONE
print("\n3. WORK DONE")
force = float(input("Enter force in Newtons: "))
distance = float(input("Enter distance in metres: "))
work = force * distance
print("Work Done =", work, "J")

# 4. MOMENTUM
print("\n4. MOMENTUM")
mass = float(input("Enter mass in kg: "))
velocity = float(input("Enter velocity in m/s: "))
momentum = mass * velocity
print("Momentum =", momentum, "kg m/s")

# 5. POWER
print("\n5. POWER")
work = float(input("Enter work done in Joules: "))
time = float(input("Enter time in seconds: "))
power = work / time
print("Power =", power, "W")

print("\n===== CALCULATIONS COMPLETED =====")
