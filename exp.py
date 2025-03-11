def speed_poly2():
    print("You selected Option 1")

def torque_linear():
    print("You selected Option 2")

#def case3():
    #print("You selected Option 3")

#def default_case():
    #print("Invalid option selected")

def switch_case(option):
    # Dictionary mapping options to functions
    switch_dict = {
        1: case1,
        2: case2,
        3: case3,
    }
    
    # Get the function from the dictionary, default to default_case if option is not found
    selected_case = switch_dict.get(option, default_case)
    
    # Execute the selected function
    selected_case()

# Main program
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 4:
                print("Exiting the program.")
                break
            switch_case(choice)
        except ValueError:
            print("Please enter a valid number.")
