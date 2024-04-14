# There are three methods to ensure that no whitespaces extra
# exists at the right, left sides of a string:
# rstrip() and lstrip()

print("\nRight side")
my_hero = "daredevil   "
print(my_hero)
print(my_hero.rstrip()) 

print("\nleft side")
my_hero = "   daredevil"
print(my_hero)
print(my_hero.lstrip())

# strip() method can strip extra whitespaces from both sides
print("\nBoth sides")
my_hero = "   daredevil   "
print(my_hero)
print(my_hero.strip())
