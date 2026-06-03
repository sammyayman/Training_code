# 7 Examples of if, elif, and else with break, pass, and continue
#%%
# Example 1: Using break in a loop with if/elif/else
print("Example 1: Using break with if/elif/else")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num < 5: print(f"{num} is less than 5")
    elif num == 5: print(f"{num} is exactly 5 - breaking loop"); break
    else: print(f"{num} is greater than 5")
print()

# Example 2: Using continue with if/elif/else
print("Example 2: Using continue with if/elif/else")
for i in range(1, 11):
    if i % 2 == 0: print(f"{i} is even - continuing"); continue
    elif i % 3 == 0: print(f"{i} is divisible by 3")
    else: print(f"{i} is odd and not divisible by 3")
print()

# Example 3: Using pass with if/elif/else (placeholder for future code)
print("Example 3: Using pass with if/elif/else")
score = 85
print("Grade: B") if 80 <= score < 90 else None  # TODO: Add grade A and C logic later
print()
#%%
# Example 4: Break when condition is met in elif
print("Example 4: Break in elif block")
count = 0
while count < 10:
    print(f"Count: {count} - Still counting") if count < 3 else print(f"Count: {count} - Reached 5, breaking!") if count == 5 else print(f"Count: {count} - Continuing...")
    if count == 5: break
    count += 1
print()
#%%
# Example 5: Continue skipping certain values with if/elif/else
print("Example 5: Continue skipping with if/elif/else")
for value in range(1, 15):
    if value % 2 == 0: continue  # Skip even numbers
    print(f"{value} is divisible by 5") if value % 5 == 0 else print(f"{value} is odd and not divisible by 5")
print()
#%%
# Example 6: Pass in all branches (skeleton structure)
print("Example 6: Pass in all branches")
temperature = 31
if temperature > 30: pass  # Hot weather logic to be implemented
elif temperature > 20: print("Pleasant weather")
else: pass  # Cold weather logic to be implemented
print()
#%%
# Example 7: Complex example with break, continue, and pass
print("Example 7: Complex example with all three keywords")
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for item in data:
    print(f"{item} is small") if item < 30 else print(f"{item} is in middle range") if item < 80 else print(f"{item} is very high")

# ============================================================================
# ELECTRICAL/ELECTRONIC ENGINEERING EXAMPLES
# ============================================================================
#%%
# Example 8: Ohm's Law - Voltage, Current, Resistance calculations with break
print("Example 8: Circuit Analysis - Checking component ratings with break")
voltages = [3.3, 5.0, 12.0, 24.0, 48.0,80]  # Volts
resistance = 100  # Ohms
max_current = 0.5 # Amperes (component rating)

for voltage in voltages:
    current = voltage / resistance  # I = V/R (Ohm's Law)
    power = voltage * current  # P = V*I (Power calculation)
    
    condition_1 = f"""WARNING: Voltage {voltage}V produces {current:.3f}A - EXCEEDS RATING!
        Breaking analysis - Component will fail!"""
    condition_2 = f"Voltage {voltage}V: Current = {current:.3f}A, Power = {power:.3f}W (Near limit)"
    condition_3 = f"Voltage {voltage}V: Current = {current:.3f}A, Power = {power:.3f}W (Safe)"
    
    print(condition_1)if current > max_current else print(condition_2) if current > 0.4 else print(condition_3)
    if current > max_current: break
print()
#%%
# Example 9: Power dissipation analysis with continue
print("Example 9: Power Dissipation Analysis - Skipping low power components")
components = [
    {"name": "Resistor R1", "voltage": 5.0, "current": 0.01},
    {"name": "LED D1", "voltage": 2.0, "current": 0.02},
    {"name": "Transistor Q1", "voltage": 12.0, "current": 0.5},
    {"name": "Resistor R2", "voltage": 3.3, "current": 0.005},
    {"name": "Motor M1", "voltage": 24.0, "current": 2.0},
]

min_power_threshold = 0.1  # Watts - skip components below this

for comp in components:
    power = float(comp["voltage"]) * float(comp["current"])
    cond_1 = f"{comp['name']}: Power = {power:.2f}W - HIGH POWER (needs heatsink)"
    cond_2 =f"{comp['name']}: Power = {power:.2f}W - Normal operation"
    
    if power < min_power_threshold: continue  # Skip low-power components
    print(cond_1) if power > 10 else print(cond_2)
print()

# Example 10: Frequency response analysis with pass
print("Example 10: Frequency Response Analysis - Filter design with pass")
frequencies = [10, 100, 1000, 10000, 100000]  # Hz
cutoff_frequency = 1000  # Hz (low-pass filter)

for freq in frequencies:
    F = 20 * (freq / cutoff_frequency)
    attenuation_db = F if freq > cutoff_frequency else 0  # Simplified calculation
    
    Below = f"Frequency {freq}Hz: Signal passes (below {cutoff_frequency}Hz cutoff)"
    Cutoff = f"Frequency {freq}Hz: At cutoff frequency (-3dB attenuation)"
    Attenuated = f"Frequency {freq}Hz: Attenuated by ~{attenuation_db:.1f}dB"
    
    print(Below) if freq < cutoff_frequency else print(Cutoff) if freq == cutoff_frequency else print(Attenuated)  # TODO: Calculate exact attenuation at -3dB point
print()

# Example 11: Impedance matching with break
print("Example 11: Impedance Matching - Finding optimal load with break")
Zc = 50  # Ohms (typical RF source) Source impedance 
Zl = [15, 42, 50, 75, 100, 150, 200]  # Ohms Load impedance
tolerance = 5 # Ohms

for load_z in Zl:
    mismatch = abs(load_z - Zc)
    
    vswr = (1 + (mismatch / Zc)) / (1 - (mismatch / Zc)) if mismatch < Zc else float('inf')
    
    perfect  = f" {mismatch} : Load {load_z}Ω: Perfect match! (VSWR ≈ 1.0) - Optimal found!"
    good= f" {mismatch} : Load {load_z}Ω: Good match (mismatch: {mismatch}Ω)"
    poor = f" {mismatch} : Load {load_z}Ω: Poor match (mismatch: {mismatch}Ω)"
    
    print(perfect) if mismatch <= tolerance else print(good) if mismatch <= 10 else print(poor)
    if mismatch <= tolerance : break
print()



# Example 12: Signal processing - ADC sampling with continue and pass
print("Example 12: ADC Signal Processing - Filtering noise with continue/pass")
adc_readings = [512, 1023, 0, 511, 1024, 1, 510, 1022, 2, 509]  # 10-bit ADC (0-1023)
valid_min = 10
valid_max = 1013
noise_threshold = 5

for reading in adc_readings:
    if reading < valid_min or reading > valid_max: continue  # Skip invalid readings
    voltage = (reading / 1023) * 5.0 if abs(reading - 512) >= noise_threshold else 0  # Convert to voltage (assuming 5V reference)
    noise_msg = f"Reading {reading}: Near zero (possible noise)"  # TODO: Implement noise filtering algorithm
    valid_msg = f"Reading {reading}: Valid signal = {voltage:.3f}V"
    print(noise_msg) if abs(reading - 512) < noise_threshold else print(valid_msg)
print("Signal processing complete!")

# %%
# ============================================================================
# SIMPLE ONE-LINER EXAMPLES
# ============================================================================

# Example 13: Simple one-liner with continue (simulated using filtering)
print("Example 13: Simple one-liner with continue")
[print(f"{i} is odd") for i in range(1, 11) if i % 2 != 0]
print()

# Example 14: Simple one-liner with pass (simulated using None)
print("Example 14: Simple one-liner with pass")
x = 5
print("x is positive") if x > 0 else None if x == 0 else print("x is negative")
print()

# Example 15: Simple one-liner with break (simulated using any() and short-circuiting)
print("Example 15: Simple one-liner with break")
# any() stops iteration when it finds True (simulating break)
any((print(f"Found {num} - breaking!") or True) if num == 7 else (print(f"Number: {num}") and False) for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print()

# ============================================================================
# EXAMPLES WITH AND / OR LOGICAL OPERATORS
# ============================================================================

# Example 16: Range checking with 'and'
print("Example 16: Range checking with 'and'")
age = 25
print(f"Age {age} too young") if age >= 18 and age <= 65 else print(f"Age {age} is Adult")


 
# Example 17: Validating input with 'or'
print("Example 17: Validating input with 'or'")
user_role = "editor"

print(f"Access granted: User is an {user_role}")if user_role == "admin" or user_role == "editor" else print(f"Access denied: {user_role} ")



# Example 18: Complex condition mixing 'and' and 'or' (Loan eligibility)
print("Example 18: Loan eligibility (Income AND (Credit OR Co-signer))")
income , credit_score  , has_cosigner = 50000, 650, True
 
if income >= 40000 and (credit_score > 700 or has_cosigner):print("Loan Approved: Income sufficient AND (Good credit OR Has co-signer)")
else: print("Loan Denied")
print()

# Example 19: System Safety Check (Multiple 'and' conditions)
print("Example 19: System Safety Check")
T , P , coolant_level = 75  , 100 , "High"

print("System Status: NORMAL - All systems nominal") if T < 80 and P < 120 and coolant_level == "High" else print("System Status: WARNING - Check system parameters!")

 
# Example 20: Login Logic (Username match AND Password match)
print("Example 20: Simple Login Logic")
db_user = "admin"
db_pass = "secret123"
input_user = "admin"
input_pass = "secret123"

if input_user == db_user and input_pass == db_pass:
    print("Login Successful!")
elif input_user == db_user and input_pass != db_pass:
    print("Login Failed: Incorrect password")
else:
    print("Login Failed: User not found")
print()

# ============================================================================
# SOFTWARE ENGINEERING MATH EXAMPLES
# ============================================================================

# Example 21: Bitwise Power of 2 Check with Override (Memory Alignment)
print("Example 21: Power of 2 Check with 'or' Override")
buffer_size = 1024
force_alignment = False
# Check if size is power of 2 AND positive, OR if alignment is forced
if (buffer_size > 0 and (buffer_size & (buffer_size - 1)) == 0) or force_alignment:
    print(f"Allocation allowed: {buffer_size} (Valid power of 2 OR Forced)")
else:
    print(f"Allocation failed: {buffer_size} is invalid")
print()

# Example 22: Robust Float Comparison with Validity Checks
print("Example 22: Float Comparison with 'or' for Invalid States")
val1 = 0.1 + 0.1 + 0.1
val2 = 0.3
epsilon = 1e-9
is_nan = False  # Simulated NaN check

if is_nan or val1 == float('inf') or val2 == float('inf'):
    print("Comparison skipped: Values contain NaN or Infinity")
elif abs(val1 - val2) < epsilon:
    print(f"Match found: {val1:.17f} approx equals {val2}")
else:
    print("Values differ")
print()

# Example 23: Load Balancing with Health Checks
print("Example 23: Load Balancing with 'and' Health Checks")
request_id = 4532
server_count = 3
target = request_id % server_count
s1_healthy = True
s2_healthy = False # Server 2 is down
s3_healthy = True

if target == 0 and s1_healthy:
    print("Route to Server 1")
elif target == 1 and s2_healthy:
    print("Route to Server 2")
elif (target == 1 and not s2_healthy) or (target == 2 and s3_healthy):
    # Failover logic: If S2 is target but down, OR target is S3...
    print("Route to Server 3 (Failover or Primary)")
else:
    print("No healthy servers available")
print()

# Example 24: Algo Selection with Memory Constraints
print("Example 24: Sorting Algo with 'or' Memory Constraint")
size = 500000
low_memory_mode = True

# Use Merge Sort if size is large AND NOT in low memory mode
# Use Quick Sort (in-place) if size is large OR low memory mode is active
if size < 64:
    print("Insertion Sort")
elif size >= 64 and not low_memory_mode:
    print("Merge Sort (Stable but uses extra memory)")
elif size >= 64 or low_memory_mode:
    print("Quick Sort (In-place, preferred for low memory)")
print()

# Example 25: Collision Detection with Active Layers
print("Example 25: Collision Detection with 'and' Layer Check")
px, py = 15, 25
bx, by, bw, bh = 10, 10, 50, 50
layer_active = True
god_mode = False

# Collision if layer is active AND point is inside, unless god_mode is on
is_inside = (px >= bx and px <= bx + bw) and (py >= by and py <= by + bh)

if (is_inside and layer_active) and not god_mode:
    print("COLLISION DETECTED!")
elif is_inside and god_mode:
    print("Collision ignored (God Mode Active)")
else:
    print("No Collision")
print()

# ============================================================================
# PROBABILITY & STATISTICS EXAMPLES
# ============================================================================

# Example 26: Hypothesis Testing (P-value Significance)
print("Example 26: Hypothesis Testing with 'or' (Loose vs Strict)")
p_value = 0.035
alpha_strict = 0.01
alpha_loose = 0.05
exploratory_mode = True

# Reject Null Hypothesis if p < 0.01 OR (p < 0.05 AND we are in exploratory mode)
if p_value < alpha_strict or (p_value < alpha_loose and exploratory_mode):
    print(f"Result Significant: p={p_value} (Rejects H0)")
else:
    print(f"Result Not Significant: p={p_value} (Fail to reject H0)")
print()

# Example 27: Outlier Detection (Z-Score / Standard Deviation)
print("Example 27: Outlier Detection with 'or'")
mu = 50.0  # Mean
sigma = 5.0  # Std Dev
data_point = 66.0
z_score = (data_point - mu) / sigma

# Outlier if it is beyond 3 sigma (positive OR negative)
if z_score > 3 or z_score < -3:
    print(f"Extreme Outlier detected: Z={z_score:.2f}")
elif z_score > 2 or z_score < -2:
    print(f"Moderate Outlier detected: Z={z_score:.2f}")
else:
    print(f"Data point is within normal range: Z={z_score:.2f}")
print()

# Example 28: System Reliability (Series vs Parallel Probability)
print("Example 28: System Reliability (Redundancy Check)")
prob_comp_A = 0.95
prob_comp_B = 0.90
required_reliability = 0.99
is_critical_system = True

# Parallel reliability: 1 - (fail_A * fail_B)
prob_parallel = 1 - ((1 - prob_comp_A) * (1 - prob_comp_B))

if is_critical_system and prob_parallel >= required_reliability:
    print(f"System Safe: Combined Reliability {prob_parallel:.4f} meets target")
elif not is_critical_system and (prob_comp_A > 0.9 or prob_comp_B > 0.9):
    print("System Acceptable: Non-critical with at least one good component")
else:
    print(f"System Unsafe: {prob_parallel:.4f} below target {required_reliability}")
print()

# Example 29: Bayes Theorem Application (Spam Filter Logic)
print("Example 29: Spam Filter (Bayesian Logic with 'and')")
prob_spam = 0.2
word_in_spam = 0.8  # P(Word|Spam)
word_in_ham = 0.1   # P(Word|Ham)
has_suspicious_link = True

# Simplified Naive Bayes score proportional to P(Spam|Word)
spam_score = (word_in_spam * prob_spam) / ((word_in_spam * prob_spam) + (word_in_ham * (1 - prob_spam)))

if (spam_score > 0.9) or (spam_score > 0.5 and has_suspicious_link):
    print(f"Email marked as SPAM (Score: {spam_score:.2f})")
else:
    print(f"Email marked as HAM (Score: {spam_score:.2f})")
print()

# Example 30: Game Loot Drop (Weighted Probability)
print("Example 30: Loot Drop Rarity with 'and'")
roll = 0.96  # 0.0 to 1.0
player_luck_bonus = True
is_boss_chest = True

# Legendary: Top 5% (0.95+) AND Boss Chest, OR Top 1% (0.99+) anywhere
if (roll >= 0.99) or (roll >= 0.95 and is_boss_chest):
    print("DROP: **LEGENDARY ITEM**")
elif (roll >= 0.80 and player_luck_bonus) or roll >= 0.90:
    print("DROP: Epic Item")
else:
    print("DROP: Common Item")
print()

# %%
print("Example 31: At least one success")
p, n = 0.4, 5
p_any = 1 - (1 - p) ** n
if p_any >= 0.9 or (p_any >= 0.8 and n >= 5):
    print(f"High chance: {p_any:.3f}")
elif p_any >= 0.5:
    print(f"Moderate chance: {p_any:.3f}")
else:
    print(f"Low chance: {p_any:.3f}")
print()

print("Example 32: Poisson event probability")
import math
lambda_rate = 0.3
p_ge1 = 1 - math.exp(-lambda_rate)
threshold = 0.2
if p_ge1 > threshold and lambda_rate <= 1.0:
    print(f"Likely occurrence: {p_ge1:.3f}")
elif p_ge1 > threshold or lambda_rate > 2.0:
    print(f"Possible occurrence: {p_ge1:.3f}")
else:
    print(f"Unlikely occurrence: {p_ge1:.3f}")
print()

print("Example 33: Expected value decision")
p_success = 0.6
reward = 100
cost = 55
risk_aversion_low = True
expected_reward = p_success * reward
if expected_reward >= cost or (expected_reward >= 0.9 * cost and risk_aversion_low):
    print("Proceed")
else:
    print("Skip")
print()

print("Example 34: Binomial exact success probability")
n, k, p = 4, 2, 0.3
p_k = 6 * (p ** k) * ((1 - p) ** (n - k))
if p_k >= 0.4:
    print(f"High exact probability: {p_k:.3f}")
elif p_k >= 0.2 and p <= 0.5:
    print(f"Moderate exact probability: {p_k:.3f}")
else:
    print(f"Low exact probability: {p_k:.3f}")
print()

print("Example 35: Proportion confidence interval")
phat = 0.52
n = 500
z = 1.96
p0 = 0.5
m = z * ((phat * (1 - phat)) / n) ** 0.5
inside = (phat - m <= p0) and (p0 <= phat + m)
if inside:
    print("Hypothesis within interval")
else:
    print("Hypothesis outside interval")
print()
