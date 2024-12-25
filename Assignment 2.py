# Data structures in Python
# List
# Create a list of 5 random numbers and print the list.
L1=[2,45,23,34,78,90]
print(L1)
# Q2. Insert 3 new values to the list and print the updated list.
L1.insert(2,48)
print(L1)
L1.insert(6,67)
print(L1)
L1.insert(7,91)
print(L1)
L1.extend([48,67,91])
print(L1)
# Q3. Try to use a for loop to print each element in the list.
for i in L1:
    print(i)
# Dictionary
# Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.
D1={"Name":"John","Age":25,"Address":"New York"}
print(D1)
# Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'.
D1["Phone"]=1234567890
print(D1)
#  Set
# Q1.Create a set with values 1, 2, 3, 4, and 5.
S1={1,2,3,4,5}
print(S1)
# Q2.Add the value 6 to the set created in Q1.
S1.add(6)
print(S1)
# Q3.Remove the value 3 from the set created in Q1
S1.remove(3)
print(S1)
# # Tuple
# Create a tuple with values 1, 2, 3, and 4
T1=(1,2,3,4)
print(T1)
# Q2. Print the length of the tuple created in Q1.
print(len(T1))




























