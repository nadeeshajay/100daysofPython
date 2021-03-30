row1 = ["X", "X", "X"]
row2 = ["X", "X", "X"]
row3 = ["X", "X", "X"]
row4 = ["X", "X", "X"]
map = [row1, row2, row3, row4]
print(f"{row1}\n{row2}\n{row3}")
x = int(input("Type the row number(x) : "))
y = int(input("Type the coloumn number(y) : "))
map[x-1][y-1] = "O" 
print(f"{row1}\n{row2}\n{row3}\n{row4}")