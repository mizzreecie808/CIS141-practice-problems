'''
Problem #1
Construct a truth table for the expression:
(A AND B) OR (NOT B) where A and B each can be True or False.
Your truth table should be commented out (as it's not valid Python code!)
'''
# 1) List the variables
# A, B

# 2) Determine the number of rows
# 2 X 2 = 4 rows

# 3) Create table columns
# A   B    (A AND B)   (NOT B)  (A AND B) OR (NOT B)

# 4) Enumerate all possible (A, B) combinations
# A   B    (A AND B)   (NOT B)  (A AND B) OR (NOT B)
# T   T
# T   F
# F   T
# F   F

# 5) Fill each row with sub-expression results
# A   B    (A AND B)   (NOT B)  (A AND B) OR (NOT B)
# T   T     T           F        T
# T   F     F           T        T
# F   T     F           F        F
# F   F     F           T        T
