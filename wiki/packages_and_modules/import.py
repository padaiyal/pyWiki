# from package1.add import add
from wiki.packages_and_modules.package1 import *  # Import all statement

print("Going to add ...")
print(add.add(2, 300))
# print(subtract.subtract(2, 300)) # Won't work as it isn't imported with the import all statement.
