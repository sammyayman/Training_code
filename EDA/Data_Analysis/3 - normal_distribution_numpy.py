import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# 1. Generate random numbers from a normal distribution
# Parameters: loc (mean), scale (standard deviation), size
normal_data = np.random.normal(loc=0, scale=1, size=1000)

# 2. Basic statistics
mean = np.mean(normal_data)
std_dev = np.std(normal_data)
median = np.median(normal_data)

print(f"Mean: {mean:.4f}")
print(f"Standard Deviation: {std_dev:.4f}")
print(f"Median: {median:.4f}")

# 3. Probability Density Function (PDF)
def normal_pdf(x, mu=0, sigma=1):
    """Calculate the probability density function of a normal distribution."""
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# 4. Plotting the normal distribution
plt.figure(figsize=(10, 6))

# Histogram of the random data
sns.histplot(normal_data, kde=True, stat="density", label="Random Data")

# Theoretical normal curve
x = np.linspace(-4, 4, 1000)
pdf = normal_pdf(x, mean, std_dev)
plt.plot(x, pdf, 'r-', lw=2, label='Theoretical PDF')

plt.title('Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('normal_distribution.png')
plt.show()

# 5. Standard Normal Distribution (mean=0, std=1)
standard_normal = np.random.standard_normal(1000)

# 6. Calculate z-scores
def z_score(data):
    """Calculate z-scores for the data."""
    return (data - np.mean(data)) / np.std(data)

z_scores = z_score(normal_data)

# 7. Calculate percentiles
percentiles = np.percentile(normal_data, [25, 50, 75, 95, 99])
print("\nPercentiles (25th, 50th, 75th, 95th, 99th):")
print(np.round(percentiles, 4))

# 8. Check if data is normally distributed using Q-Q plot
plt.figure(figsize=(8, 6))
import scipy.stats as stats
stats.probplot(normal_data, dist="norm", plot=plt)
plt.title('Q-Q Plot for Normality Check')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('qq_plot.png')
plt.show()

# 9. Probability calculations
# Calculate probability of value being less than 1 standard deviation from mean
prob_less_than_1std = stats.norm.cdf(1) - stats.norm.cdf(-1)
print(f"\nProbability within 1 standard deviation: {prob_less_than_1std:.4f} (68.27% theoretical)")

# 10. Generate random numbers with different parameters
samples = np.random.normal(loc=5, scale=2, size=1000)
print(f"\nSamples with mean=5, std=2")
print(f"Sample mean: {np.mean(samples):.4f}, Sample std: {np.std(samples):.4f}")


import numpy as np
import math
from scipy.special import erf
# parameters
mu, sigma = 0, 1   # standard normal
x = np.linspace(-3, 3, 7)  # example values

pdf = (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-0.5*((x-mu)/sigma)**2)
# CDF using erf
# CDF using erf
cdf = 0.5 * (1 + np.vectorize(math.erf)((x - mu) / (sigma * np.sqrt(2))))
print("CDF:", cdf)
cdf = 0.5 * (1 + erf((x - mu) / (sigma * np.sqrt(2))))
print("CDF:", cdf)

print("x:", x)
print("PDF:", pdf)



import numpy as np
import math

arr = np.array([-1.0, 0.0, 1.0, 2.0])

# math.erf fails on arrays, but works on scalars
try:
    print(math.erf(arr))   # ❌ will raise an error
except Exception as e:
    print("Error:", e)

# vectorize math.erf
v_erf = np.vectorize(math.erf)

# now apply to the array
result = v_erf(arr)

print("Array:", arr)
print("erf applied:", result)

print("\033c")

import numpy as np
import math

# a 2D array
arr = np.array([[-1.0, 0.0, 1.0],
                [ 2.0, 0.5, -0.5]])

# math.erf alone will fail on array
# vectorize it
v_erf = np.vectorize(math.erf)
# compute CDF: Φ(x) = 0.5 * (1 + erf(x / sqrt(2)))
cdf = 0.5 * (1 + v_erf(arr / math.sqrt(2)))
# apply on 2D array
result = v_erf(arr)

print("Original array:\n", arr)
print("erf applied (2D):\n", result)
print("Original array:\n", arr)
print("Normal CDF applied (2D):\n", cdf)