

# python epdb1.py
# Execute the next statement with n (next)
# Printing the value of variables with p (print)
# Turning off the (Pdb) prompt with c (continue)
# Seeing where you are with l (list)


import pdb
a = "aaa"
pdb.set_trace()
b = "bbb"
c = "ccc"
final = a + b + c
print final