Tiles_Description = [
    "Small black granite",
    "Small grey marble",
    "Small  powder blue",
    "Medium sunset yellow",
    "Medium berry red",
    "Medium glittery purple",
    "Large oak wood effect",
    "Large black granite",
    "Large bamboo effect",
    "Extra-large white marble",
]

Price_per_box = [
    19.50,
    25.95, 
    35.75,
    12.50,
    11.00,
    52.95,
    65.00,
    58.98,
    85.00,
    62.75,
]
Height = []
Width = []
# Task 1
count = 0
Number_of_tiles = len(Tiles_Description)
print("Which of the following tiles do you wanna buy?: ")
while count < Number_of_tiles:
    Identification_code = count + 1
    print(str(Identification_code) + ". " + str(Tiles_Description[count]) + " $" + str(Price_per_box[count]))
    count = count + 1

#Task 2
Area = 0
i =0
walls = int(input("How many walls do you wish to tile?: "))
while walls > 0: 
    Height.append(float(input("What is the height the wall(s) you want to tile?: ")))
    Width.append(float(input("What is the width of the wall(s) you want to tile?: ")))
    print("----------------------------------------------------------------------------------------")
    Area = Height[i] * Width[i] + Area
    walls = walls - 1
    i = i + 1
print("----------------------------------------------------------------------------------------")
User_tile_wrong = int(input("Type in the Sr. Number of the tile you want to buy (Ex--> 7): "))
User_tile = User_tile_wrong - 1
print("----------------------------------------------------------------------------------------")
print("The area of your wall is " + str(Area))
def cost(User_tile, Area):
    if(Area % 1 >= 0.5):
        Packs_needed = (Area // 1) + 1
    else:
        Packs_needed = Area // 1
    Price = Price_per_box[User_tile]
    Cost = Price * Packs_needed
    waste = ((Packs_needed - Area)/Packs_needed)*100
    print("You will need " + str(Packs_needed) + " packs of tiles")
    print("The Cost of your purchase is " + " $" + str(Cost))
    print(str(waste) + "% of tiles packs will be wasted")
cost(User_tile, Area)