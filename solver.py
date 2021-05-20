# solver.py
count=0 #this variable will count how many times we had to backtrack
bo = [
         [8, 1, 0, 0, 3, 0, 0, 2, 7],
         [0, 6, 2, 0, 5, 0, 0, 9, 0],
         [0, 7, 0, 0, 0, 0, 0, 0, 0],
         [0, 9, 0, 6, 0, 0, 1, 0, 0],
         [1, 0, 0, 0, 2, 0, 0, 0, 4],
         [0, 0, 8, 0, 0, 5, 0, 7, 0],
         [0, 0, 0, 0, 0, 0, 0, 8, 0],
         [0, 2, 0, 0, 1, 0, 7, 5, 0],
         [3, 8, 0, 0, 7, 0, 0, 4, 2]
    ]
def solve(bo):
    #base case for recursion.
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):   #As soon as we get a vlid value at a positiion then we solve for the next empty position
                return True # if we didn't find any empty position that means we have reached the end of our @D array.

            bo[row][col] = 0
            global count
            count = count + 1
    #solve(bo) would get replaced by false and the value at that position will be 0.
    #That means while recursion, we didn't get any valid value fot that position.
    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end=" ")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


print_board(bo)
solve(bo)
print("\n")
print_board(bo)
print(f'We had to backtrack {count} times')