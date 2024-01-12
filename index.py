import math
file_path = 'c1.txt'

length_count = {}
try:
    with open(file_path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            parts = line.strip().split(': ')
            length = float(parts[0].split()[-1])
            count = int(parts[1])

            length_count[length] = count
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Display lengths and counts
for length, count in length_count.items():
    print(f"Messages with length {length}: {count}")

# Calculate cumulative sum
cumulative_sum = {}
current_sum = 0
for length in sorted(length_count.keys()):
    current_sum += length_count[length]
    cumulative_sum[length] = current_sum

# Display cumulative sum
print("\nCumulative sum:")
for length, cum_sum in cumulative_sum.items():
    print(f"Messages with length {length}: {cum_sum}")

# Calculate log scale
log_scale = {}
for length, count in length_count.items():
    log_scale[length] = math.log10(count)

# Display log scale
print("\nLog scale:")
for length, log_value in log_scale.items():
    print(f"Messages with length {length}: {log_value}")
