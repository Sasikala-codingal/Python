i=1
while i<=5:
    print("Outer Loop" )
    j=1
    while j<=10:
        print(j, end=" ")
        print("Inner loop")
        j=j+1
    i=i+1
    print("")
print("OUT OF THE LOOP NOW")