# N Queen Problem
'''The N Queen is the problem of placing N Queens in a N*N chess board such that no two Queens attck each other'''
# Recursive solution
import tkinter as tk

numQueens = int(input("enter the number of queens\n"))
currentSolution = [0 for x in range(numQueens)]
solutions = []
solution1 = []


# Defining list of n rows
def list_(a):
    return [item for item in range(numQueens)]


row_list = list_(numQueens)
print("row_list", row_list)


# Defining a Safe function to check whether the Queen is safe or no
def Safe(testRow, testCol):
    if testRow == 0:
        return True
    # To check for column
    for row in range(0, testRow):
        if testCol == currentSolution[row]:
            return False
        # To check for diagonal attack
        elif abs(testRow - row) == abs(testCol - currentSolution[row]):
            return False
    return True
# Defining a function for placement of queen
def placeQueen(row):
    global currentSolution, solutions, numQueens, solution_1

    for col in range(numQueens):

        if not Safe(row, col):
            continue
        else:
            currentSolution[row] = col

            if row == (numQueens - 1):
                solutions.append(currentSolution.copy())

                if len(solutions) == 1:
                    solution_1 = list(zip(row_list, currentSolution))
                    print("Solution number ", len(solutions), (list(zip(row_list, currentSolution))))

                else:
                    print("Solution number ", len(solutions), (list(zip(row_list, currentSolution))))

            else:
                # recursive function
                placeQueen(row + 1)


print("Solving for " + str(numQueens) + " Queens")
placeQueen(0)

# Creating an interface such that the coordinates where the queen can be placed pops up
window = tk.Tk()
window.title("CHESS BOARD")
for i in range(numQueens):
    for j in range(numQueens):
        if (i, j) in solution_1:
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=5
            )
            frame.configure(bg="black")
            
        else:
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.configure(bg="red")

        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f" {i}, {j}")
        label.pack()

window.mainloop()