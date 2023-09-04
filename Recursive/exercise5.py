def staircase(height, current_row=0):
    if height == 0:
        return "Not Draw!\n"
    if height < 0:
        height = -height
        if  current_row < height:
            underline = "_" * current_row
            hashes = "#" * (height - current_row)
            total = underline + hashes + "\n"
            height = -height
            return total + str(staircase(height, current_row + 1))
        else:
            return ""
    elif height > 0:
        if current_row < height:
            underline = "_" * (height - (current_row + 1))
            hashed = "#" *  (height - len(underline))
            total = underline + hashed + "\n"
            return total + str(staircase(height, current_row + 1))
        else:
            return ""
    
print(staircase(int(input("Enter Input : "))))
