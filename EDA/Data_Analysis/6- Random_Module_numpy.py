print("\033c")
import numpy as np

# 1. Setting the random seed for reproducibility
np.random.seed(42)  # Any number can be used as the seed

# 2. Basic random number generation
print("1. Basic Random Number Generation:")
print("Random float in [0.0, 1.0]:", np.random.random())
print("Random integer between 0 and 10:", np.random.randint(0, 10))
print("Random float from standard normal distribution:", np.random.randn())

# 3. Generating arrays of random numbers
print("\n2. Random Arrays:")
print("Array of 5 random floats in [0,1]):", np.random.rand(5))
print("2x3 array of random floats in [0,1]):\n", np.random.rand(2, 3))
print("Array of 3 random integers between 1 and 10:", np.random.randint(1, 11, 3))

# 4. Random sampling from arrays
print("\n3. Random Sampling:")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Original array:", arr)
print("Random choice from array:", np.random.choice(arr))
print("Random sample of 3 elements:", np.random.choice(arr, size=3, replace=False))
print("Shuffled array:", np.random.permutation(arr))

# 5. Probability distributions
print("\n4. Probability Distributions:")
print("Normal distribution (mean=0, std=1):", np.random.normal(0, 1, 5))
print("Uniform distribution [0,1):", np.random.uniform(0, 1, 5))
print("Binomial distribution (n=10, p=0.5):", np.random.binomial(10, 0.5, 5))
print("Poisson distribution (lambda=3):", np.random.poisson(3, 5))


# Example 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# 1. Normal distribution with array means and standard deviation
normal_result = np.random.normal(loc=arr, scale=1)  # Same shape as arr
print("Normal distribution with array means:\n", normal_result)

# 2. Uniform distribution with array bounds
uniform_result = np.random.uniform(low=arr, high=arr+1)  # Values between [arr, arr+1)
print("\nUniform distribution with array bounds:\n", uniform_result)

# 3. Binomial distribution with array probabilities
binomial_result = np.random.binomial(n=10, p=arr/10)  # n=10 trials, p from array
print("\nBinomial distribution with array probabilities:\n", binomial_result)

# 4. Poisson distribution with array lambdas
poisson_result = np.random.poisson(lam=arr)  # Lambda values from array
print("\nPoisson distribution with array lambdas:\n", poisson_result)

# 5. Using where parameter for conditional sampling
# Only sample where condition is True
condition = arr > 4
result = np.where(condition, 
                 np.random.normal(0, 1, size=arr.shape),  # if True
                 arr)                                     # if False
print("\nConditional sampling (normal where arr > 4, else original):\n", result)

# 6. Random sampling with probabilities
print("\n5. Weighted Random Sampling:")
probabilities = [0.1, 0.1, 0.1, 0.1, 0.6]  # Must sum to 1
print("Random choice with probabilities:", 
      np.random.choice(['A', 'B', 'C', 'D', 'E'], p=probabilities))

# 7. Random sampling without replacement
print("\n6. Sampling Without Replacement:")
print("Random sample without replacement:", 
      np.random.choice(10, 5, replace=False))  # No duplicates

# 8. Setting random state
print("\n7. Reproducibility with Random State:")
rng = np.random.RandomState(42)  # Create a random number generator
print("Reproducible random numbers:", rng.random(3))
print("Same numbers again:", rng.random(3))

# 9. Randomly shuffling arrays
print("\n8. Array Shuffling:")
arr_2d = np.arange(10).reshape(2, 5)
print("Original 2D array:\n", arr_2d)
np.random.shuffle(arr_2d)  # Shuffles along the first axis only
print("Shuffled array:\n", arr_2d)

# 10. Random permutations
print("\n9. Random Permutations:")
print("Permutation of range(10):", np.random.permutation(10))

# 11. Random selection with weights
print("\n10. Weighted Random Selection:")
weights = [0.1, 0.2, 0.7]  # Don't need to sum to 1
print("Weighted random choice:", np.random.choice(['A', 'B', 'C'], p=np.array(weights)/sum(weights)))

# 12. Random sampling from different distributions
print("\n11. Sampling from Various Distributions:")
print("Exponential distribution (scale=1.0):", np.random.exponential(1.0, 5))
print("Gamma distribution (shape=2.0, scale=1.0):", np.random.gamma(2.0, 1.0, 5))
print("Beta distribution (a=2.0, b=5.0):", np.random.beta(2.0, 5.0, 5))

# 13. Randomly selecting from a multinomial distribution
print("\n12. Multinomial Distribution:")
print("Multinomial sample (n=20, pvals=[0.1, 0.2, 0.7]):", 
      np.random.multinomial(20, [0.1, 0.2, 0.7]))

# 14. Randomly sampling from a multivariate normal distribution
print("\n13. Multivariate Normal Distribution:")
mean = [0, 0]
cov = [[1, 0], [0, 1]]  # diagonal covariance
print("Samples from multivariate normal:\n", 
      np.random.multivariate_normal(mean, cov, 3))
