# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen=Screen()
#
# print(my_screen.canvheight)
# my_screen.exitonclick()
#

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water", "Fire"])

table.align = "l"

print(table)

print(table.get_string(fields=["Pokemon"]))

# print second row and third row
print(table.get_string(start=1, end=3))


