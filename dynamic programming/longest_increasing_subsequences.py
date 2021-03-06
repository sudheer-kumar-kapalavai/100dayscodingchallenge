# Program for computing longest increasing subsequences for a given array.
# we need to compute the length of longest possible subsequence which is increasing that is sorted in ascending order.
# --------------------------------------------------------------------------------------------------------
# We need to understand optimal substructure and overlapping subproblems.
# If we are finding the lis for let's index from 0....1, then next index ele has option to either take it or not take it.
# Thus, every element has option to either take it or not take it.
# Giving 2^n options which if we do it using naive method using recursion then exponential time is taken.
# We can find the optimal longest increasing subsequence if we are able to find the shorter ones and keep on increasing by either including
# or not including next elements.
# ---------------------------------------------------------------------------------------------------------
# L(i) = 1 + max( L(j) ) where 0 < j < i and arr[j] < arr[i]; or
# L(i) = 1, if no such j exists.
# (LIS(1)=1)
#
#       f(4)  {f(4) = 1 + max(f(1), f(2), f(3))}
#   /    |    \
# f(1)  f(2)  f(3) {f(3) = 1, f(2) and f(1) are > f(3)}
#        |      |  \
#       f(1)  f(2)  f(1) {f(2) = 1 + max(f(1)}
#               |
#             f(1) {f(1) = 1}
# Base case : when L(1) = 1, thus every single element is in itself longest increasing subsequence.
# -------------------------------------------------------------------------------------------------------------
# TIME : 0(N^2), SPACE : 0(N)
# -------------------------------------------------------------------------------------------------------------
# Can we do more better than this ?
# Let's without any dp or recursion.
# It's possible in TIME : 0(N * log(N)), SPACE : 0(N).
# We can use extra array to store the minimum possible value for the subsequence at index i, in the sequecne in the array M[i].
# Whenever new element comes, we check witht the last element stored in M, then move to previous element and this search can be done using binary search, as M stores 
# Indices whose elements are sorted.
# After searching, low will contain one length greater than length of longest prefix
# and then store the index i in M at new length found in low.
# Then, check if this is the max length found so far, thus update the max length.
# -------------------------------------------------------------------------------------------------------------

# DP based solution :

def compute_longest_incr_subs(arr):

    # base case
    lis = [1] * len(arr)

    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    return max(lis)

# NlogN solution : 
import math
def compute_longest_incr(X):
    n = len(X)
    M = [0 for _ in range(n + 1)]
    print(M)
    L = 0
    for i in range(0, n):
        print(M)
        low = 1
        high = L
        print(f"searching from {low} to {high}")
        while low <= high:
            mid = math.ceil(low + high) // 2
            print(f"mid found is  {mid}")
            if X[M[mid]] < X[i]:
                low = mid + 1
            else:
                high = mid - 1
        
        newL = low
        M[newL] = i
        
        if newL > L:
            L = newL
    
    return L


if __name__ == '__main__':
    arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]
    print(compute_longest_incr_subs(arr))
