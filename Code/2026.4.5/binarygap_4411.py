# This Python program implements the following use case:
# Write code to find BinaryGap of a given positive integer

def binary_gap(n):
    if not isinstance(n, int) or n <= 0:
        return 0
    binary = bin(n)[2:]
    max_gap = 0
    current_gap = 0
    found_one = False
    for bit in binary:
        if bit == '1':
            if found_one:
                max_gap = max(max_gap, current_gap)
            current_gap = 0
            found_one = True
        elif found_one:
            current_gap += 1
    return max_gap

print(binary_gap(9))
print(binary_gap(529))
print(binary_gap(20))
print(binary_gap(15))
print(binary_gap(1))