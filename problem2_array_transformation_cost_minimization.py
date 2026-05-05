"""
Problem 2: Array Transformation Cost Minimization
===================================================
Given array A of size N and a fixed integer K. We can add or subtract K
from any element any number of times.
Goal: make all elements equal with minimum total operations, or -1 if impossible.

Key Observations:
-----------------
1. A[i] can only reach values: A[i], A[i]+K, A[i]-K, A[i]+2K, ...
   i.e., any value of the form  A[i] + m*K  for integer m.

2. Two elements A[i] and A[j] can reach the same value only if:
   (A[i] - A[j]) is divisible by K  =>  A[i] % K == A[j] % K
   If any element has a different remainder, return -1.

3. If feasible, normalize: B[i] = (A[i] - r) // K
   Cost to bring B[i] to target t  =  |B[i] - t|  (each step covers K).
   Total cost = sum of |B[i] - t|, minimized when t = median(B).

Time Complexity:  O(N log N)  -- dominated by sorting for the median
Space Complexity: O(N)
"""

def min_operations(arr, k):
    mod = arr[0] % k

    for num in arr:
        if num % k != mod:
            return -1

    base = min(arr)
    steps = [(num - base) // k for num in arr]

    steps.sort()
    median = steps[len(steps)//2]

    total = sum(abs(x - median) for x in steps)
    return total

try:
    n = int(input("Enter n: "))
    arr = list(map(int, input("Enter array: ").split()))
    k = int(input("Enter k: "))

    if len(arr) != n:
        print("Array size mismatch")
    else:
        print(min_operations(arr, k))

except:
    print("Invalid input! Please enter numbers only.")
