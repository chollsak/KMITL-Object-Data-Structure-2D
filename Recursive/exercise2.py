def deleteIsland(Map,y,x):
    if y < 0 or x < 0 or y >= len(Map) or x >= len(Map[0]) or Map[y][x] == '.':
        return
    Map[y][x] = '.'
    deleteIsland(Map,y+1,x)
    deleteIsland(Map,y-1,x)
    deleteIsland(Map,y,x+1)
    deleteIsland(Map,y,x-1)
    
def countIsland(Map):
    M = Map[0]
    if '#' in M:
        deleteIsland(Map,Map.index(M),list(M).index('#'))
        return 1 + countIsland(Map)
    else:
        if len(Map) == 1:
            return 0
        return countIsland(Map[1:])
    
inp = input("Enter input: ").split()
Map = []
for i in range(int(inp[1])):
    a = list(input().split())
    Map.append(a)
    
print(f"{countIsland(Map)}")
    