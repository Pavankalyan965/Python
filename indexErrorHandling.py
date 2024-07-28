vegetables = ['tomato','carrot','spinach','cabbage']

requestedVegetable = input("ENter your index")

while True:
    try:
        print("Your vegetable is:"+requestedVegetable)
        break
    except:
        print("not found")