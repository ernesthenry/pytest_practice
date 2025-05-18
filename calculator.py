def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b

def power(a,b):
    return a ** b


def square_root(a):
    if a< 0:
        raise ValueError("Cannot take square root of negative number")
    return a ** 0.5

def factorial(n):
    if n < 0:
        raise ValueError("Cannot take factorial of negative number")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    if n < 0:
        raise ValueError("Cannot take fibonacci of negative number")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors

def is_palindrome(s):
    return s == s[::-1]

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def count_consonants(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def remove_duplicates(lst):
    return list(set(lst))

def sort_list(lst):
    return sorted(lst)

def find_max(lst):
    if not lst:
        raise ValueError("List is empty")
    return max(lst)

def find_min(lst):
    if not lst:
        raise ValueError("List is empty")
    return min(lst)

def sum_list(lst):
    return sum(lst)

def average_list(lst):
    if not lst:
        raise ValueError("List is empty")
    return sum(lst) / len(lst)

def merge_lists(lst1, lst2):
    return lst1 + lst2

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def union(lst1, lst2):
    return list(set(lst1) | set(lst2))


def difference(lst1, lst2):
    return list(set(lst1) - set(lst2))

def is_subset(lst1, lst2):
    return set(lst1).issubset(set(lst2))

def is_superset(lst1, lst2):
    return set(lst1).issuperset(set(lst2))

def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

def transpose(matrix):
    if not matrix:
        return []
    return [list(row) for row in zip(*matrix)]

def matrix_multiply(matrix1, matrix2):
    if not matrix1 or not matrix2:
        raise ValueError("One or both matrices are empty")
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Matrices cannot be multiplied")
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def matrix_add(matrix1, matrix2):
    if not matrix1 or not matrix2:
        raise ValueError("One or both matrices are empty")
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices cannot be added")
    result = [[0] * len(matrix1[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result


def matrix_subtract(matrix1, matrix2):
    if not matrix1 or not matrix2:
        raise ValueError("One or both matrices are empty")
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices cannot be subtracted")
    result = [[0] * len(matrix1[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] - matrix2[i][j]
    return result

def matrix_transpose(matrix):
    if not matrix:
        raise ValueError("Matrix is empty")
    return [list(row) for row in zip(*matrix)]

def matrix_determinant(matrix):
    if not matrix:
        raise ValueError("Matrix is empty")
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square")
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for c in range(len(matrix)):
        det += ((-1) ** c) * matrix[0][c] * matrix_determinant([row[:c] + row[c + 1:] for row in matrix[1:]])
    return det


def matrix_inverse(matrix):
    if not matrix:
        raise ValueError("Matrix is empty")
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square")
    n = len(matrix)
    identity = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    augmented_matrix = [matrix[i] + identity[i] for i in range(n)]
    for i in range(n):
        if augmented_matrix[i][i] == 0:
            raise ValueError("Matrix is singular and cannot be inverted")
        for j in range(n):
            if i != j:
                ratio = augmented_matrix[j][i] / augmented_matrix[i][i]
                for k in range(2 * n):
                    augmented_matrix[j][k] -= ratio * augmented_matrix[i][k]
    inverse = [[augmented_matrix[i][j] / augmented_matrix[i][i] for j in range(n, 2 * n)] for i in range(n)]
    return inverse

def matrix_rank(matrix):
    if not matrix:
        raise ValueError("Matrix is empty")
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square")
    rank = 0
    for i in range(len(matrix)):
        if any(matrix[i]):
            rank += 1
    return rank

def matrix_eigenvalues(matrix):
    if not matrix:
        raise ValueError("Matrix is empty")
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square")
    n = len(matrix)
    eigenvalues = []
    for i in range(n):
        eigenvalues.append(matrix[i][i])
    return eigenvalues


