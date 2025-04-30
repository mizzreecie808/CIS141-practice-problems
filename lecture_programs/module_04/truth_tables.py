# Truth Tables
# https://www.youtube.com/watch?v=cXsnxFkw3ZQ
# Problem of the day: (A OR B) AND NOT(A AND B)
# 1. List variables:
# A, B

# 2. Determine the Number of Rows
# 2 Possiblities for A
# 2 Possiblities for B
# 2 x 2 combinations of A&B

# 3. Create Table Columns
# A B  (A OR B)  (A AND B)  NOT(A AND B)  (A OR B) AND NOT(A AND B)

# 4. Enumerate All Possible (A, B) Combinations
# A B  (A OR B)  (A AND B)  NOT(A AND B)  (A OR B) AND NOT(A AND B)
# T T
# T F
# F T
# F F

# 5. Fill Each Row with Sub-Expression Results
# A B  (A OR B)  (A AND B)  NOT(A AND B)  (A OR B) AND NOT(A AND B)
# T T   True      True          False      False
# T F   True      False         True       True
# F T   True      False         True       True
# F F   False     False         True       False
