xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for i in xs:
    #a
    print(i)
    #b
    print(str(i)+', '+str(i**2))
    print()

print()
#c
print(sum(xs))

print()
#d
result = 1
for i in xs:
    result = result*i

print(result)
