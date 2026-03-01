
st = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))


sq = [i**2 for i in range(st, end + 1)]


evensq = [sq for sq in sq if sq % 2 == 0]
oddsq = [sq for sq in sq if sq % 2 != 0]

# Display results
print("All square values:", sq)
print("Even square values:", evensq)
print("Odd square values:", oddsq)2