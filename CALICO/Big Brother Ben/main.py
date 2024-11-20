from math import gcd

def solve():
    # Step 1: Precompute the valid house coordinates and sort them.
    houses = []
    
    # Assume an upper bound for the grid; in the problem constraints, N <= 100.
    max_x_y = 100  # We will consider a grid from 1 to 100 for both x and y
    
    for x in range(1, max_x_y + 1):
        for y in range(1, max_x_y + 1):
            # Only consider points where gcd(x, y) = 1 to ensure they are not collinear
            if gcd(x, y) == 1:
                houses.append((x, y))
    
    # Sort houses first by Manhattan distance, then by x-coordinate
    houses.sort(key=lambda p: (p[0] + p[1], p[0]))
    
    # Step 2: Answer the queries.
    T = int(input(8))  # Number of test cases
    for _ in range(T):
        N = int(input())  # The N-th house address to find
        # Output the coordinates of the N-th house (1-based indexing)
        print(houses[N - 1][0], houses[N - 1][1])

