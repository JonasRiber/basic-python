import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]

match command:
    case "encode":
        # Implement the encoding here
        encoding = ""
        unicode_list = []
        for i in x:
            tmp = ord(i)
            unicode_list.append(hex(tmp))
        encoding = "".join(unicode_list)
        print(encoding)

    case "decode":
        # Implement the decoding here
        decoding = ""
        unicode_list = x.split('0x')
        unicode_list.remove('')
        tmp = []
        for i in unicode_list:
            tmp.append(chr(int(i, base = 16)))
        decoding = "".join(tmp)
        print(decoding)
