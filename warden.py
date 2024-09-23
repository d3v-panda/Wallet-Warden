from collections import Counter

addresses = [
    # Add your addresses here
    
]

# Count occurrences of each address
address_counts = Counter(addresses)

# Find duplicates
duplicates = [addr for addr, count in address_counts.items() if count > 1]

print("Duplicates found:", duplicates)