import numpy as np
import math

def read_input(fname):
    with open(fname, "r") as file:
        return [[x.strip()[0], x.strip()[1:]] for x in file.readlines()]
        
def convertLocationToCoords(location):
    location = location.split(", ")
    out = []
    x = location[0].split(" ")
    y = location[1].split(" ")
    if x[0] == "east":
        x = int(x[1])
    elif x[0] == "west":
        x = - int(x[1])
    if y[0] == "north":
        y = int(y[1])
    elif y[0] == "south":
        y = - int(y[1])
    return [x, y]
        
def followInstruction(instruction, location, direction):
    cardinal = instruction[0]
    units = int(instruction[1])
    lis = ["N", "E", "S", "W"]
    ind = lis.index(direction)
    
    if cardinal == "N":
        location[1] += units
    elif cardinal == "S":
        location[1] -= units
    elif cardinal == "E":
        location[0] += units
    elif cardinal == "W":
        location[0] -= units
    elif cardinal == "L":
        units = int(units / 90)
        direction = lis[(ind - units)%4]
    elif cardinal == "R":
        units = int(units / 90)
        direction = lis[(ind + units)%4]
    elif cardinal == "F":
        if direction == "N":
            location[1] += units
        elif direction == "S":
            location[1] -= units
        elif direction == "E":
            location[0] += units
        elif direction == "W":
            location[0] -= units
    return location, direction

def rotate(origin, point, angle):
    angle = math.radians(angle)
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return [round(qx), round(qy)]
    
def followInstructionPart2(instruction, location, waypoint):
    cardinal = instruction[0]
    units = int(instruction[1])
    
    if cardinal == "N":
        waypoint[1] += units
    elif cardinal == "S":
        waypoint[1] -= units
    elif cardinal == "E":
        waypoint[0] += units
    elif cardinal == "W":
        waypoint[0] -= units
    elif cardinal == "L":
        waypoint = rotate((0,0),waypoint, units)
    elif cardinal == "R":
        waypoint = rotate((0,0),waypoint, -units)
    elif cardinal == "F":
        location[1] += units * waypoint[1]
        location[0] += units * waypoint[0]
    return location, waypoint
    
def loopPart1(inputFile, location, direction):
    for ins in inputFile:
        location, direction = followInstruction(ins, location, direction)
        # print(ins, location, direction)
    return abs(location[0]) +  abs(location[1])
    
def loopPart2(inputFile, location, waypoint):
    for ins in inputFile:
        location, waypoint = followInstructionPart2(ins, location, waypoint)
        # print(ins, location, waypoint)
    return abs(location[0]) +  abs(location[1])
        
def main():
    inputFile = read_input("input.txt")
    location = convertLocationToCoords("east 0, north 0")
    direction = "E"
    print("The answer to part 1 is " + str(loopPart1(inputFile, location, direction)))
    
    location = convertLocationToCoords("east 0, north 0")
    waypoint = convertLocationToCoords("east 10, north 1")
    print("The answer to part 2 is " + str(loopPart2(inputFile, location, waypoint)))
   
    
if __name__ == "__main__":
    main()