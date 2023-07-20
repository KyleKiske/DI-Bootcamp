playerX = "Player X"
playerO = "Player O"
list_of_inputs = []

def display_board(inputs):
    field_line_list = ["*     |   |     *", "*     |   |     *", "*     |   |     *"]
    the_board = []
    if inputs != None:
        for x in inputs:
            player = x[0]
            row = x[1]
            column = x[2]
            field_line_list[row-1] = field_line_list[row-1][:column*4] + player + field_line_list[row-1][column*4+1:]            

    title = "TIC TAC TOE"
    horizontal_edge = "*"*17
    separator_line = "*  ___|___|___  *"
    the_board.append(title)
    the_board.append(horizontal_edge)
    the_board.append(field_line_list[0])
    the_board.append(separator_line)
    the_board.append(field_line_list[1])
    the_board.append(separator_line)
    the_board.append(field_line_list[2])
    the_board.append(horizontal_edge)
    for x in the_board:
        print (x)
    return the_board

def player_input(player):
    print (f"{player}\'s turn...\n")
    while True:
        row = int(input("Enter desired row: "))
        column = int(input("Enter desired column: "))
        if (row > 3 or column > 3 or row < 1 or column < 1):
            print("This field is not there, try to write in proper field.")
        elif ((("X", row, column) in list_of_inputs) or (("O", row, column) in list_of_inputs)):
            print("This field is occupied, try to write in another field.")
        else:
            list_of_inputs.append((player[-1], row, column))
            break

    return (player, row, column)

def check_win(inputs):
    matrix = [0,0,0,0,0,0,0,0]
    for j in inputs:
        for i in range(3):
            if (j[0] == "X" and j[1] == i+1):
                matrix[i] += 1
            elif (j[0] == "O" and j[1] == i+1):
                matrix[i] -= 1
            if (j[0] == "X" and j[2] == i+1):
                matrix[i+3] += 1
            elif (j[0] == "O" and j[2] == i+1):
                matrix[i+3] -= 1
        if (j[1] == j[2] and j[0] == "X"):
            matrix[6] += 1
        elif (j[1] == j[2] and j[0] == "O"):
            matrix[6] -= 1
        if ((j[1] == 1 and j[2] == 3 and j[0] == "X") or (j[1] == 2 and j[2] == 2 and j[0] == "X") or (j[1] == 3 and j[2] == 1 and j[0] == "X")):
            matrix[7] += 1
        elif ((j[1] == 1 and j[2] == 3 and j[0] == "O") or (j[1] == 2 and j[2] == 2 and j[0] == "O") or (j[1] == 3 and j[2] == 1 and j[0] == "O")):
            matrix[7] -= 1
    return matrix

def main():
    print("Welcome to TIC TAC TOE!\n")
    while (len(list_of_inputs) < 9) :

        display_board(list_of_inputs)
        if len(list_of_inputs) % 2 == 0:
            player_input(playerX)
        else:
            player_input(playerO)
        if (3 in check_win(list_of_inputs)) or (-3 in check_win(list_of_inputs)):
            display_board(list_of_inputs)
            print (check_win(list_of_inputs))
            if (3 in check_win(list_of_inputs)):
                return print("Player X won")
            else:
                return print("Player O won")
    else:
        return ("fields are exhausted")

main()