states_of_america1 = ['Delaware', 'Texas', 'California']
states_of_america1_orig = list(states_of_america1)
states_of_america2 = ['Minnesota', 'Washington']

states_of_america = states_of_america1 + states_of_america2

states_of_america1.append(states_of_america2)
states_of_america_append = list(states_of_america1)

states_of_america_sum = states_of_america1 + states_of_america2

states_of_america_extend = states_of_america1_orig
states_of_america_extend.extend(states_of_america2)

print("With append:")
print(states_of_america_append)
print("With addition:")
print(states_of_america_sum)
print("As you see, the append modifies the original data.")

print("")
print("With extend:")
print(states_of_america_extend)

orig_string: str = "Angela, Zoltan"
print(F"Split a string {orig_string.split(',')}:")
