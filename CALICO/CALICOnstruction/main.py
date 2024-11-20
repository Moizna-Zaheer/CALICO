def calico_blocks(input_path):
    # CALICO block mappings (with possible rotations)
    block_mappings = {
        'C': ['C'],
        'A': ['A'],
        'L': ['L'],
        'I': ['I', 'H'],
        'O': ['O', 'U'],
        'H': ['H', 'I'],
        'U': ['U', 'O'],
        'N': ['N'],
    }

    # Parse input from the file
    with open(input_path, 'r') as file:
        data = file.read().splitlines()
    T = int(data[0])  # Number of test cases
    test_cases = data[1:]

    results = []
    for S in test_cases:
        # Count the frequency of letters needed for the string
        freq = {}
        for char in S:
            found = False
            for key, mapped_chars in block_mappings.items():
                if char in mapped_chars:
                    freq[key] = freq.get(key, 0) + 1
                    found = True
                    break
            if not found:
                # If a character cannot be matched by any CALICO block
                results.append(-1)
                break
        else:
            # Calculate the maximum number of sets of CALICO blocks required
            max_sets = max((freq[block] for block in freq), default=0)
            results.append(max_sets)

    # Print results
    for result in results:
        print(result)

# Example file path for input
input_path = "input_path"
calico_blocks(input_path)
