def diff(sour:int, bitter:int):
    return abs(sour - bitter)

def find(length, sour, bitter):
    global best
    if length == length_inp:
        if bitter > 0 and diff(sour, bitter) < best:
            best = diff(sour, bitter)
    else:
        find(length + 1, sour * sour_l[length], bitter + bitter_l[length])
        find(length + 1,sour, bitter)


inp = input("Enter Input : ").split(",")

length_inp= len(inp)

sour_l = []
bitter_l = []
best = 9999


for i in inp:
    i = i.split(" ")
    sour_l.append(int(i[0]))
    bitter_l.append(int(i[1]))

find(0, 1, 0)

print(best)