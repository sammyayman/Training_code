print("\033c")
# NumPy Array Creation Methods
import numpy as np

print("")


# 1. Creating arrays from Python lists
a1 = np.array([1, 2, 3, 4, 5])  # 1D array from list
a2 = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array from nested lists
print("1D array:", a1)
print("2D array:\n", a2)

# 2. Array with specific data type
a3 = np.array([1, 2, 3], dtype=np.float32)
print("\nArray with float32 type:", a3.dtype)

# 3. Common array creation functions
# Create array of zeros
zeros = np.zeros((2, 3))  # 2x3 array of zeros
print("\nZeros array:\n", zeros)

print("now")
# Create array of ones
ones = np.ones((3, 2))  # 3x2 array of ones
print("\nOnes array:\n", ones)

#Create array with range of values 
arr_range = np.array([range(10,50,5) , range(1,9)])
print("\nArray with range of values:\n", arr_range)

# Using arange to create arrays with different ranges
arr_range1 = np.arange(10, 50, 5)  # Start at 10, stop before 50, step by 5
arr_range2 = np.arange(1, 9)       # Start at 1, stop before 9, step 1 (default)

# To combine them into a 2D array
combined = np.array([arr_range1, arr_range2])
print("First range:", arr_range1)
print("Second range:", arr_range2)
print("Combined array:\n", combined)


# Create linearly spaced array
linspace = np.linspace(0, 10, 7)  # 7 numbers from 0 to 10 (inclusive)
print("\nLinspace array:", linspace)
print("\nLinspace array (formatted):", np.array2string(linspace, precision=2, separator=', '))

# Create identity matrix 



identity = np.eye(3)  # 3x3 identity matrix
print("\nIdentity matrix:\n", identity)



# 4. Random arrays
# 4.1 Random values between 0 and 1
random_vals = np.random.random((2, 2))
print("\nRandom values between 0 and 1 (2x2):\n", random_vals)

# 4.2 Random integers
random_ints = np.random.randint(1, 10, size=(2, 3))  # 2x3 array of ints from 1 to 9
print("\nRandom integers (1-9, 2x3):\n", random_ints)


# 4.3 Random numbers from normal (Gaussian) distribution
normal_dist = np.random.normal(loc=0, scale=1, size=(3,2))  # mean=0, std=1
print("\nNormal distribution (mean=0, std=1):", normal_dist)

normal_dist = np.random.rand(3,2) 
print("\n:", normal_dist)


# 4.4 Random choice from array
choices = ['red', 'blue', 'green', 'yellow']
random_choice = np.random.choice(choices, size=(2,2))  # Pick 3 colors with replacement
print("\nRandom choices from list:", random_choice)

# 4.5 Shuffling arrays
arr = np.arange(10)
np.random.shuffle(arr)  # Shuffles the array in-place
print("\nShuffled array:", arr)


# 4.6 Random permutation
permuted = np.random.permutation(8)  # Returns a permuted range of 0-4
print("Random permutation of 0-4:", permuted)

# For a 2x4 array of random permutations, you can use:
permuted_2d = np.random.permutation(8).reshape(2, 4)  # 2x4 array with numbers 0-7
print("2x4 permutation array:\n", permuted_2d)

# 4.7 Random seed for reproducibility
np.random.seed(42)  # Setting seed for reproducible results
random1 = np.random.randint(2,9 , size=(2,4))
random2 = np.random.random(size=(2,4))
print("\nRandom numbers with seed (should be same every run):", random1, random2)

# 4.8 Random sample from uniform distribution
uniform_sample = np.random.uniform(low=1, high=10, size=(2,2))  # Uniform distribution
print("\nUniform distribution (1-10):", uniform_sample)

# 4.9 Random binomial distribution (coin flips)
coin_flips = np.random.binomial(n=1, p=0.5, size=10)  # 1=Heads, 0=Tails
print("\nCoin flips (1=Heads, 0=Tails):", coin_flips)

# 5. Reshaping arrays
arr = np.arange(12)
reshaped = arr.reshape(3, 4)  # Reshape to 3x4 array
print("\nOriginal array:", arr)
print("Reshaped array (3x4):\n", reshaped)

# 6. Array attributes
print("\nArray attributes:")
print("Shape:", reshaped.shape)  # Dimensions
print("Number of dimensions:", reshaped.ndim)
print("Number of elements:", reshaped.size)
print("Data type:", reshaped.dtype)
print("Item size (bytes):", reshaped.itemsize)

# 7. Special arrays
# Full array with specific value
full_array = np.full((2, 2), 7)  # 2x2 array filled with 7
print("\nFull array (all 7s):\n", full_array)

# Diagonal array
diag = np.diag([1, 2, 3])  # Diagonal matrix with 1, 2, 3 on diagonal
print("\nDiagonal array:\n", diag)

# 8. Empty array (contains uninitialized data)
empty_array = np.empty((2, 3))
print("\nEmpty array (contains garbage values):\n", empty_array)






from scipy.stats import norm

# Parameters
mu, sigma = 70, 10

# 2D array of values
A = np.array([[60, 70],
              [80, 90]])

# Elementwise PDF
pdf_values = norm.pdf(A, loc=mu, scale=sigma)

# Elementwise CDF
cdf_values = norm.cdf(A, loc=mu, scale=sigma)

print("Array A:\n", A)
print("\nPDF values:\n", pdf_values)
print("\nCDF values:\n", cdf_values)


from scipy.stats import multivariate_normal

# Mean vector
mu = np.array([70, 70])

# Covariance matrix
sigma1, sigma2, rho = 10, 15, 0.5
Sigma = np.array([[sigma1**2, rho*sigma1*sigma2],
                  [rho*sigma1*sigma2, sigma2**2]])

# Point to evaluate
x = np.array([80, 90])

# PDF at point x
pdf_value = multivariate_normal.pdf(x, mean=mu, cov=Sigma)

print("Sigma covariance matrix:\n", Sigma)
print("\nPDF at (80,90):", pdf_value)
