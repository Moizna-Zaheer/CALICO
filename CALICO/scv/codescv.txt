def is_triangle(grid, rows, cols):
    """Check if the grid represents a triangle."""
    vertices = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '#':
                vertices.append((i, j))

    if len(vertices) < 3:  # Not enough points for a triangle
        return False
    
    # Extract minimum and maximum coordinates for the vertices
    min_x = min(v[0] for v in vertices)
    max_x = max(v[0] for v in vertices)
    min_y = min(v[1] for v in vertices)
    max_y = max(v[1] for v in vertices)

    # Check if it forms a right isosceles triangle
    diagonal_length = abs(max_x - min_x)
    base_length = abs(max_y - min_y)
    return base_length == diagonal_length

def is_rectangle(grid, rows, cols):
    """Check if the grid represents a rectangle."""
    vertices = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '#':
                vertices.append((i, j))

    if len(vertices) < 4:  # Not enough points for a rectangle
        return False

    # Extract minimum and maximum coordinates for the vertices
    min_x = min(v[0] for v in vertices)
    max_x = max(v[0] for v in vertices)
    min_y = min(v[1] for v in vertices)
    max_y = max(v[1] for v in vertices)

    # Check if all cells within the bounding box are #
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            if grid[i][j] != '#':
                return False

    return True

def solve_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    t = int(lines[0])  # Number of test cases
    results = []
    idx = 1
    
    for _ in range(t):
        # Parse grid dimensions
        n, m = map(int, lines[idx].split())
        idx += 1
        
        # Parse grid rows
        grid = lines[idx:idx + n]
        grid = [line.strip()[:m] for line in grid]  # Ensure rows are exactly length `m`
        idx += n
        
        # Solve for current grid
        if is_rectangle(grid, n, m):  # Prioritize rectangle detection
            results.append("ferb")
        elif is_triangle(grid, n, m):
            results.append("phineas")
        else:
            results.append("unknown")
    
    # Print all results
    for result in results:
        print(result)

# Example usage
file_path = "C:/Users/hp/OneDrive/Desktop/CALICO/scv/scv.txt"  
solve_from_file(file_path)
