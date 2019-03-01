import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# If we sort both lists, we can make use of Pythons comparison operators for
# strings, that is < and >. We can iterate up one list comparing each name to
# the next value in the other list. Whenever the other list has a high value,
# we switch lists and continue. In this way, we only need to make one sweep
# over the combined list, and our runtime complexity is a function of the
# total number of names. That is, linear or O(n).

# Sort both lists
names_1.sort()
names_2.sort()

# Setup duplicates, lists, and indices
duplicates = []
list_current = names_1
list_cross_compare = names_2
index_max_names = max(len(names_1), len(names_2))
index_current = 0
index_cross_compare = 0

# Advance through the lists, finding duplicates
while max(index_cross_compare, index_current) < index_max_names:
    # Get current and comparison values for this iteration
    value_current = list_current[index_current]
    value_cross_compare = list_cross_compare[index_cross_compare]
    # Advance if cross value is still less than current value
    if value_cross_compare < value_current:
        index_cross_compare += 1
        continue
    # Switch if cross value is greater than current value
    if value_cross_compare > value_current:
        list_current, list_cross_compare = list_cross_compare, list_current
        index_current, index_cross_compare = index_cross_compare, index_current
        index_cross_compare += 1
        continue
    # Add a duplicate and advance each
    duplicates.append(value_current)
    index_cross_compare += 1
    index_current += 1

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
