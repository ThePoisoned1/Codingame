# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
extensions = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    extensions[ext.lower()]=mt
for i in range(q):
    line = input() # One file name per line.
    if "." not in line:
         print("UNKNOWN")
         continue
    fileExt = line.split(".")[-1].lower()  
    if fileExt in extensions:
        print(extensions[fileExt])
    else:
        print("UNKNOWN")

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
