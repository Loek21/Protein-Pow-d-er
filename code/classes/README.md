## Classes
# Introduction
The classes folder contains two .py files that hold the class objects that all algorithms use. It forms the datastructure of all programs.

# Element.py
Element.py contains an object that is used to refer to one 'element' in a string. So in the protein string 'HPPHHP', each character represents one element object.
Each element object at least contains the 'character' it refers to and it's XYZ coordinates.

# Lattice.py
all element objects are then collected in a lattice object. Through that lattice object, the element objects can be conveniently called in different ways, such as a list or a dictionairy.
In a way, this is a multifuctional datastructure that allows the developers to call the element objects in a convenient way for their algorithm.
