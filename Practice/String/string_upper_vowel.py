
myString = "This is an another sentence"

# Initialize counters
a_counter = 0
e_counter = 0
i_counter = 0
o_counter = 0
u_counter = 0

# Iterate through each character in the string
for char in myString:
    if char.upper() == "A":
        a_counter += 1
    elif char.upper() == "E":
        e_counter += 1
    elif char.upper() == "I":
        i_counter += 1
    elif char.upper() == "O":
        o_counter += 1
    elif char.upper() == "U":
        u_counter += 1

print("Number of a is:", a_counter)
print("Number of e is:", e_counter)
print("Number of i is:", i_counter)
print("Number of o is:", o_counter)
print("Number of u is:", u_counter)