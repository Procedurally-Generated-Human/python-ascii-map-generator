import random
import numpy as np


def create_world(height,width,percent):    
    numbers = np.random.uniform(0,1,h*w)
    for index,value in enumerate(numbers):
        if value >= (100-percent)/100:
            numbers[index] = 1
        else:
            numbers[index] = 0
    return [round(x) for x in numbers]

def draw_world(list2d):
    print("Generation:",gen_number)
    print("")
    list2d = [[p if p !=0 else '.' for p in s] for s in list2d]
    list2d = [[p if p !=1 else '#' for p in s] for s in list2d]
    for row in list2d:
        for col in row:
            print(col, end = "")
        print()
    print("")
    print("")

def nest_list(list1,rows, columns):    
        result=[]               
        start = 0
        end = columns
        for i in range(rows): 
            result.append(list1[start:end])
            start +=columns
            end += columns
        return result

def cellular_automata():
    for row in range(h):
        for col in range(w):
            if 5 <= info[row][col]['ones_around'] >= 7  :
                info[row][col]['change'] = 1

def apply_changes():
    for row in range(h):
        for col in range(w):
            world[row][col] = info[row][col]['change']

def world_info(arr):
    world_info = []

    for i in range(len(arr)):
        for j, value in enumerate(arr[i]):
            if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
                # corners
                new_neighbors = []
                if i != 0 and j != 0:
                    new_neighbors.append(arr[i - 1][j - 1]) 
                if i != 0:
                    new_neighbors.append(arr[i - 1][j])
                if i != 0 and j != len(arr[i]) - 1:
                    new_neighbors.append(arr[i - 1][j + 1])
                if j != len(arr[i]) - 1:
                    new_neighbors.append(arr[i][j + 1]) 
                if i != len(arr) - 1 and j != len(arr[i]) - 1:
                    new_neighbors.append(arr[i + 1][j + 1]) 
                if i != len(arr) - 1:
                    new_neighbors.append(arr[i + 1][j]) 
                if i != len(arr) - 1 and j != 0:
                    new_neighbors.append(arr[i + 1][j - 1])
                if j != 0:
                    new_neighbors.append(arr[i][j - 1])

            else:
                new_neighbors = [
                    arr[i - 1][j - 1],  
                    arr[i - 1][j],  
                    arr[i - 1][j + 1],  
                    arr[i][j + 1],  
                    arr[i + 1][j + 1],  
                    arr[i + 1][j],  
                    arr[i + 1][j - 1],
                    arr[i][j - 1] 
                ]
            non = 0
            for e in new_neighbors:
                if e == 1:
                    non = non + 1
                    
            change = arr[i][j]
            if arr[i][j] == 1:
                if non <= 2:
                   change = 0
                elif non >= 3:
                    pass
            elif arr[i][j] == 0:
                if non > 5:
                    change = 1
                elif non <= 5:
                    pass
            world_info.append({
                "index": (i,j),
                "value": value,
                "neighbors": new_neighbors,
                "ones_around": non,
                "change": change
                })
    return world_info


h = int(input("Map height: "))
w = int(input("Map width: "))
generations = int(input("How many generations: "))
land_percent = int(input("Percent of land (0-100 / recommended 40-60): "))
world = nest_list(create_world(h,w,land_percent),h,w)
gen_number = 0
print("")

for a in range(generations+1):
    draw_world(world)
    info = nest_list(world_info(world),h,w)        
    cellular_automata()
    apply_changes()
    gen_number += 1
