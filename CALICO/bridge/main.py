def solve():
    T = int(input())  # Number of test cases
    for _ in range(T):
        B, N = map(int, input().split())  # Max cost and number of buildings
        heights = list(map(int, input().split()))  # Building heights
        
        min_danger = float('inf')  # Initialize with a large value for danger
        best_height = -1  # Variable to store the optimal height
        best_cost = float('inf')  # Variable to store the cost for the best height
        
        # Try all possible heights for the bridge from 0 to 100
        for h in range(101):
            danger = 0
            cost = 0
            for si in heights:
                if h > si:  # Bridge is above the building
                    danger += h - si
                else:  # Bridge is below or at the level of the building
                    cost += si - h
            
            # Debug: print the current height, danger, and cost
            print(f"Trying height {h}: Danger = {danger}, Cost = {cost}")
            
            # If the cost is within the allowed budget
            if cost <= B:
                # We want to minimize danger first, then cost
                if danger < min_danger or (danger == min_danger and cost < best_cost):
                    min_danger = danger
                    best_height = h
                    best_cost = cost
        
        # Output the best height for this test case
        print(f"Best height: {best_height}")

