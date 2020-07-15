'''
Input: an integer
Returns: an integer
'''

# Runtime 0(3^n) - small
def eating_cookies(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return (eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1))

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")


# Runtime 0(n) - large input
# def eating_cookies(n, cache):
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     # check the cache for the number
#     elif cache[n] > 0:
#         return cache[n]
#     # cache does not have the number
#     # use recursive and save answer in cache
#     else:
#         cache[n] = (eating_cookies(n-3, cache) + eating_cookies(n-2, cache) + eating_cookies(n-1, cache))
#     return cache[n]

# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_cookies = 100
#     cache = {i: 0 for i in range(num_cookies + 1)}

#     print(f"There are {eating_cookies(num_cookies, cache)} ways for Cookie Monster to each {num_cookies} cookies")