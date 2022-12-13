
counter = 0
x = 1
checkValues = [20, 60, 100, 140, 180, 220]
currIndex = 0
values = []

with open("in.txt") as f:
    for row in f:
        row = row.strip().split(' ')
        if row[0] == "noop":
            counter += 1
            if currIndex < len(checkValues) and counter >= checkValues[currIndex]:
                values.append(x * checkValues[currIndex])
                currIndex += 1
                

        elif row[0] == "addx":
            addV = int(row[1])
            # if after the first cycle it crosses the threshold, 
            # we need to add the old value, otherwise, add the new value
            if currIndex < len(checkValues) and counter + 2 >= checkValues[currIndex]:
                values.append(x * checkValues[currIndex])
                currIndex += 1                
                counter += 2
                x += addV
                # print(counter, x, addV, "1st")

            elif currIndex < len(checkValues) and counter + 3 == checkValues[currIndex]:
                x += addV
                # print(counter, x, addV, "2nd")
                values.append(x * checkValues[currIndex])
                currIndex += 1                
                counter += 2
            
            else:
                x += addV
                counter += 2
    
    print(values, sum(values))


        

        

