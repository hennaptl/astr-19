import numpy as np

def generate_sin_table(start, end, num_entries):
   
    x_values = np.linspace(start, end, num_entries)
    sin_x_values = np.sin(x_values)
    return x_values, sin_x_values

def print_table(x_values, sin_x_values):
    
    # Print the table header
    print(f"{'x':<15}{'sin(x)':<15}")
    print("-" * 30)

    # Iterate through the zipped values and print each row
    for x, sin_x in zip(x_values, sin_x_values):
        print(f"{x:<15.10f}{sin_x:<15.10f}")

def main():
    
    start_x = 0.0
    end_x = 2.0
    number_of_entries = 1000

    x, sin_x = generate_sin_table(start_x, end_x, number_of_entries)
    print_table(x, sin_x)

if __name__ == "__main__":
    main()
