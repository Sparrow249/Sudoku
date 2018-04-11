##-------TO DO-------##
# Create GUI
# Display amount of numbers according to difficulty
# Solve the sudoku (in steps with timer)

import random

numbers = [x for x in range(1, 10)]
solution = [[0 for j in range(9)] for i in range(9)]

def get_range(coord):
    #return block coordinates
    ranges = [[0,1,2],[3,4,5],[6,7,8]]
    for r in ranges:
        if coord in r:
            return r

def find_numbers(row, column):
    x_range = get_range(column)
    y_range = get_range(row)

    #check for available numbers within the block
    block_ok = numbers.copy()
    for y in y_range:
        for x in x_range:
            num = solution[y][x]
            if num in block_ok:
                block_ok.remove(num)

    #check for available numbers within the row
    row_ok = numbers.copy()
    for num in solution[row]:
        if num in row_ok:
            row_ok.remove(num)

    #check for available numbers within the column
    column_ok = numbers.copy()
    for row in range(9):
        num = solution[row][column]
        if num in column_ok:
            column_ok.remove(num)

    #return numbers that appear in all lists
    numbers_ok = list(set(block_ok) & set(row_ok) & set(column_ok))
    return numbers_ok


#--GENERATE SUDOKU--#
while True:
    restart = False
    
    for row in range(9):
        restart_count = 0
        
        while True:
            #check if stuck, if so restart generation from scratch
            if restart_count > 20:
                restart = True
                break

            #empty the row
            solution[row]= [0 for i in range(9)]

            #pick an available number for every slot
            for index in range(9):
                nums = find_numbers(row, index)
                
                if len(nums) > 0:
                    solution[row][index] = random.choice(nums)
                else:
                    restart_count += 1
                    break
                
            else:
                break
            
        if restart == True:
            break
        
    else:
        break
    
#--SHOW RESULT--#
for row in solution:
    print(row)




            


