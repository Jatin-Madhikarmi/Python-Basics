def get_matrix(name):
    print(f"\nEnter the elements for {name} (4 numbers per row, space-separated):")
    matrix = []
    for i in range(4):
        while True:
            try:
                line = input(f"Row {i+1}: ").split()
                # Convert all inputs in the row to floats
                row = [float(x) for x in line]
                
                if len(row) == 4:
                    matrix.append(row)
                    break
                else:
                    print("Error: Please enter exactly 4 numbers for this row.")
            except ValueError:
                print("Invalid input: Please enter numerical values only.")
    return matrix

def multiply_matrices(A, B):
    # Initialize a 4x4 matrix with zeros
    result = [[0.0 for _ in range(4)] for _ in range(4)]
    
    # Standard matrix multiplication algorithm
    for i in range(4):          # Row index of A
        for j in range(4):      # Column index of B
            for k in range(4):  # Index for summation
                result[i][j] += A[i][k] * B[k][j]
    return result

def display_matrix(matrix):
    for row in matrix:
        # Format to 2 decimal places for a cleaner look
        print("\t".join(f"{val:.4f}" for val in row))

# Main execution
print("--- 4x4 Float Matrix Multiplier ---")
matrix_a = get_matrix("Matrix A")
matrix_b = get_matrix("Matrix B")

result_matrix = multiply_matrices(matrix_a, matrix_b)

print("\nResulting Matrix (Formatted to 4 decimal places):")
display_matrix(result_matrix)