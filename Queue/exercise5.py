class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    

    def __getitem__(self, i:int):
        return self.items[i]

inp = input("Enter width, height, and room: ").split()

max_x = int(inp[0])
max_y = int(inp[1])
map = inp[2].split(",")

def find_axis(map, point):
    axis = None
    for i in map:
        if point in i:
            axis = (int(i.index(point)),  int(map.index(i)))
            return axis
    if axis == None:
        print("Invalid map input.")
        quit()
    return axis
        

        


def error_check(map, max_x, max_y):
    x = False
    if len(map) != max_y:
        print("Invalid map input.")
        quit()
    for i in map:
        if len(i) != max_x:
            print("Invalid map input.")
            quit()


def find_path(map):
    error_check(map, max_x, max_y)
    direction = [(-1, 0), (0,1), (1,0), (0, -1)]
    start = find_axis(map, "F")
    ans = Queue()
    ans.enQueue(start)
    to_del = Queue()
    went = Queue()
    found = False

    while not found:
        if ans.isEmpty():
            print("Cannot reach the exit portal.")
            exit()
        else:
            print("Queue:",ans.items)
            axis = ans.deQueue()
            x1, y1 = axis[1], axis[0]
            for x2,y2 in direction:
                (new_x, new_y) = (x1 + x2, y1 + y2)
                if 0 <= new_x < max_y and 0 <= new_y < max_x:
                    if map[new_x][new_y] == "_"  and (new_y, new_x) not in went:
                        ans.enQueue((new_y,new_x))
                        went.enQueue((new_y, new_x))
                    elif map[new_x][new_y] == "O":
                        print("Found the exit portal.")
                        exit()
            
find_path(map)
