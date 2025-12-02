#!/bin/python
with open('1_input', 'r') as input:
    instructions = [line.strip() for line in input.readlines()]  

value = 50
counter = 0
for inst in instructions:
    rot = inst[0]
    step = int(inst[1:])  

    print("#### new inst ####")
    if rot == "L":
        print("instruction: " + str(inst))
        print("L - " + str(value) + " - " + str(step))
        flipped = (100 - value) % 100
        passes = (flipped + step) // 100
        value = (value - step) % 100
        counter += passes
        print("add: " + str(passes))
        print("value: " + str(value))
    elif rot == "R":
        print("instruction: " + str(inst))
        print("R - " + str(value) + " + " + str(step))
        value = (value + step)
        if value > 99:
            add = value // 100
            counter += add
            print("add: " + str(add))
            value = value % 100
        else:
            add = 0
        print("value: " + str(value))

print("Value counter at the end: " + str(counter))
