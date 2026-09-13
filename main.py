def power_set(items):
    n = len(items)
    subsets = []
    for mask in range(1<<n):
        subset = [items[i] for i in range(n) if (mask>>i) & 1]
        subsets.append(subset)
    return subsets

items = [0,1,2,3,4,5,6,7,8,9]
all_subsets = power_set(items)
print(f"items: {items}")
print(f"all subsets: ")
for s in all_subsets:
    print(s)