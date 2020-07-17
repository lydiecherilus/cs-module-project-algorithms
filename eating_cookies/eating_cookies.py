'''
Input: an integer
Returns: an integer
'''

# Runtime 0(n)
def eating_cookies(n, cache={0: 1}):
    if n < 0:
        return 0
    if n not in cache:
        cache[n] = eating_cookies(
            n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 100
    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")