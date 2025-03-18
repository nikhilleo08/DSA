# Print Name N Times using recursion
def print_name(cnt, n):
    if cnt > n:
        return
    print('Nikhil', ':', cnt)
    print_name(cnt+1, n)

print_name(0, 5)

# Print 1 => N using recursion
def print_1_to_n(i, n):
    if i > n:
        return
    print(i)
    print_1_to_n(i+1, n)

print()
print('Printing 1 => N')
print_1_to_n(1, 10)

# Print N => 1 using recursion
def print_n_to_1(i, n):
    if i < 1:
        return
    print(i)
    print_n_to_1(i-1, n)

print()
print('Printing N => 1')
print_n_to_1(100, 100)      # Prints 100 => 1
# print_n_to_1(10000000, 0) # 9999005 maximum recursion depth exceeded while calling a Python object

# Print from 1 => N, but cannot do print_1_to_n(i+1, n) (Cannot do the i+1 part)

# Print 1 => N using backtracking
def print_1_to_n_backtrack(i, n):
    if i < 1:
        return
    print_1_to_n_backtrack(i-1, n)
    print(i)

print()
print('Printing 1 => N Using - instead of + (Backtracking)')
print_1_to_n_backtrack(5, 5)      # Prints 1 => 5
# Print from 1 => N, but cannot do print_1_to_n_backtrack(i+1, n) (Cannot do the i+1 part)

# Print N => 1 using backtracking
def print_n_to_1_backtrack(i, n):
    if i > n:
        return
    print_n_to_1_backtrack(i+1, n)
    print(i)

print()
print('Printing N => 1 Using + instead of - (Backtracking)')
print_n_to_1_backtrack(1, 5)      # Prints 1 => 5
# Print from N => 1, but cannot do print_n_to_1_backtrack(i-1, n) (Cannot do the i-1 part)


# Lecture 3
# Print Summation of first N numbers parameterized way
print()
print('Parameterized Way')
def sum_1_to_n_parameterized(i, sum):
    if i < 1:
        print('Sum:', sum)
        return
    sum_1_to_n_parameterized(i-1, sum + i)

print('Sum of first 5 numbers:')
sum_1_to_n_parameterized(5, 0)

print('Sum of first 3 numbers:')
sum_1_to_n_parameterized(3, 0)

# # Print Summation of first N numbers with incremental fashion
# def sum_1_to_n(i, n, sum):
#     if i > n:
#         print(f'Sum of first {n} natural numbers is: ', sum)
#         return
#     sum_1_to_n(i+1, n, sum + i)

# print()
# sum_1_to_n(1, 5, 0)
# sum_1_to_n(1, 100, 0)

# Print Summation of first N numbers with functional way
def sum_1_to_n_functional(n):
    if n == 0:
        return 0
    return n + sum_1_to_n_functional(n - 1)

print()
print('Functional Way')
print('Sum of first 3 natural numbers is:', sum_1_to_n_functional(3))
print('Sum of first 5 natural numbers is:', sum_1_to_n_functional(5))
print('Sum of first 100 natural numbers is:', sum_1_to_n_functional(100))

# Factorial of a number (Parameterized)
def factorial_parameterized(n, ans):
    if n == 1:
        print("Factorial: ", ans)
        return
    factorial_parameterized(n - 1, ans * n)

print()
print('Factorial Parameterized Way')
print('Factorial of a 5 in Parameterized fashion')
factorial_parameterized(5, 1)
print('Factorial of a 10 in Parameterized fashion')
factorial_parameterized(10, 1)

# Factorial of a number (Functional)
def factorial_functional(n):
    if n == 1:
        return 1
    return n * factorial_functional(n-1)

print()
print('Factorial Functional Way')
print('Factorial of a 5 in Functional fashion', factorial_functional(5))
print('Factorial of a 10 in Functional fashion', factorial_functional(10))

print()
print('Print all subsequence of an array ☻')
def subsequence(idx, arr, nums):
    if idx >= len(nums):
        print(arr)
        return
    arr.append(nums[idx])
    subsequence(idx+1, arr, nums)
    arr.pop()
    subsequence(idx+1, arr, nums)

subsequence(0, [], [30,10,20])
print()
print('Print all subsequence of an array')
subsequence(0, [], [3,1,2])
# Time Complexity: O(2^N)
# Space Complexity: O(N)

print()
print('Print all subsequence of an array with sum k')
def subsequence(idx, arr, nums, k):
    if idx >= len(nums):
        if sum(arr) == k:
            print(arr)
        return
    subsequence(idx+1, arr, nums, k)
    arr.append(nums[idx])
    subsequence(idx+1, arr, nums, k)
    arr.pop()

print()
print('Sum = 30')
subsequence(0, [], [30,10,20], 30)
print('Sum = 2')
subsequence(0, [], [1,2,1], 2)
print('Sum = 3')
subsequence(0, [], [1,2,1], 3)
# Time Complexity: O(2^N)
# Space Complexity: O(N)


print()
print('Print 1 subsequence of an array with sum k')
def one_subsequence(idx, arr, nums, k):
    if idx >= len(nums):
        if sum(arr) == k:
            print(arr)
            return True
        return False
    arr.append(nums[idx])
    if one_subsequence(idx+1, arr, nums, k):
        return True
    arr.pop()
    if one_subsequence(idx+1, arr, nums, k):
        return True
    return False

print()
print('Print one subsequence of an array')
print('Sum = 30')
one_subsequence(0, [], [30,10,20], 30)
print('Sum = 2')
one_subsequence(0, [], [1,2,1], 2)
print('Sum = 3')
one_subsequence(0, [], [1,2,1], 3)
# Time Complexity: O(2^N)
# Space Complexity: O(N)

print()
print('Print count of number subsequence of an array with sum k')
def count_subsequence(idx, total, nums, k, cnt):
    if idx >= len(nums):
        if total == k:
            cnt += 1
        return cnt
    total += nums[idx]
    left = count_subsequence(idx+1, total, nums, k, cnt)
    total -= nums[idx]
    right = count_subsequence(idx+1, total, nums, k, cnt)
    return left + right
print()
print('Print count of subsequence of an array')
print('Sum = 10')
print(count_subsequence(0, 0, [30,10,20], 10, 0))
print('Sum = 2')
print(count_subsequence(0, 0, [1,2,1], 2, 0))
print('Sum = 3')
print(count_subsequence(0, 0, [1,2,1], 3, 0))
print('Sum = 300')
print(count_subsequence(0, 0, [1,2,1], 300, 0))
# Time Complexity: O(2^N)
# Space Complexity: O(N)