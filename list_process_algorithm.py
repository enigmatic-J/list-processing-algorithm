# List processing algorithm
def list_process(items_range):
    items = []
    for i in range(0, items_range):
        input_item = str(input("enter name of item to list: "))
        items.append(input_item)
    items_range = 0
    print("\nItem list: \n")
    for i in items:
        items_range += 1
        print("item{} : {}".format(items_range,i))
    
        
