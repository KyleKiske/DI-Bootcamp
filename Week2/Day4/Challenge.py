matrix_string ="""7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""

true_message = ""
matrix_list = matrix_string.split("\n")
matrix_column_count = len(matrix_string.split("\n")[0])
last_is_alpha = True
for i in range(matrix_column_count):
    for x in matrix_list:
        if x[i].isalpha():
            if not last_is_alpha:
                true_message += " "
                last_is_alpha = True
            true_message += x[i]
        else:
            last_is_alpha = False
true_message = true_message.strip()
print(true_message)