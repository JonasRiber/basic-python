
# Print the pattern
x = ""
for i in range(1,11):
    
    if i < 6:
        x = x + " *"
    else:
        x = x[:-2]
    print(x)