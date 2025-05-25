setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx.intersection(sety)
print(setz)

setz = setx.union(sety)
print(setz)

setz = setx.difference(sety)
print(setz)


setz = setx.symmetric_difference(sety)
print(setz)
