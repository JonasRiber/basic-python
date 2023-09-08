import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.

if len(password) > 5 and 17 > len(password):
    one_int = False
    one_upper = False
    one_lower = False
    one_special = False
    for i in password:
        if i.isnumeric() == True:
            one_int = True
        if i.isupper() == True:
            one_upper = True
        if i.islower() == True:
            one_lower = True
        tmp = i in "$#@"
        if tmp == True:
            one_special = True

    if one_int == True and one_upper == True and one_lower == True and one_special == True:
        is_valid = True
    

print(is_valid)
