def print_oreo_cookie():
    cream_size = int(input("Enter cream size (1-10): "))

    # Print top biscuit
    print("##########")
    print("#       #")

    # Print cream filling
    for _ in range(cream_size):
        print("#       #")

    # Print bottom biscuit
    print("#       #")
    print("##########")

print_oreo_cookie()