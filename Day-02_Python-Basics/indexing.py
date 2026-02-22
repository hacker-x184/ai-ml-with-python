name = "Anonymous"
# Accessing characters using index
print(name[0])   # First character
print(name[1])   # Second character
print(name[-1])  # Last character
print(name[-2])  # Second last character
# now We are using the slincing concenpt
text = "PythonLearning"
print(text[0:6])   # Python
print(text[6:14])  # Learning
print(text[:6])    # Python
print(text[6:])    # Learning
print(text[:])     # Full string
print("\n--- Slicing ---")
sample = "CyberSecurity"
print("First 5 letters:", sample[:5])
print("Last 8 letters:", sample[-8:])
print("Reverse:", sample[::-1])
print("Every 2nd char:", sample[::2])