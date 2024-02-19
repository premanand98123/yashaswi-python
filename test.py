def print_pattern(rows):
    for i in range(rows,0,-1):
        for j in range(i):
            print(j+1,end=" ")
        print()
    

print_pattern(5)

a