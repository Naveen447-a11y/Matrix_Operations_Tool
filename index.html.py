import numpy as np

# Function to input a matrix
def input_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []
    print("Enter matrix elements row-wise:")

    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    return np.array(matrix)


while True:
    print("\n===== MATRIX OPERATIONS TOOL =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        print("\nEnter Matrix A")
        A = input_matrix()

        print("\nEnter Matrix B")
        B = input_matrix()

        if A.shape == B.shape:
            result = A + B
            print("\nAddition Result:")
            print(result)
        else:
            print("Matrices must have the same dimensions!")

    elif choice == 2:
        print("\nEnter Matrix A")
        A = input_matrix()

        print("\nEnter Matrix B")
        B = input_matrix()

        if A.shape == B.shape:
            result = A - B
            print("\nSubtraction Result:")
            print(result)
        else:111e
            print("Matrices must have the same dimensions!")

    elif choice == 3:2
        print("\nEnter Matrix A")
        A = input_matrix()

        print("\nEnter Matrix B")
        B = input_matrix()

        if A.shape[1] == B.shape[0]:
            result = np.dot(A, B)
            print("\nMultiplication Result:")
            print(result)
        else:
            print("Matrix multiplication not possible!")

    elif choice == 4:
        print("\nEnter Matrix")
        A = input_matrix()

        result = A.T

        print("\nTranspose of Matrix:")
        print(result)

    elif choice == 5:
        print("\nEnter Matrix")
        A = input_matrix()

        if A.shape[0] == A.shape[1]:
            result = np.linalg.det(A)
            print("\nDeterminant of Matrix:")
            print(result)
        else:
            print("Determinant can only be calculated for square matrices!")

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")