
def collectHats():
    hats = ["red", "red", "blue", "blue", "yellow", "red", "blue", "yellow", "green", "black", "blue", "red", "yellow", "blue", "black", "black", "red", "green", "yellow"]
    return hats

def process(hats):
    hat_count = {}
    for i in hats:
        if i in hat_count:
            hat_count[i] += 1
        else:
            #add color to hat_count nnd increase value by one.
            hat_count[i] = 1
    return hat_count
    
def display(hat_count):
    for i, j in hat_count.items():
        print(f"{i.capitalize()} hats: {j}")

hat_data = collectHats()
processed_data = process(hat_data)
display(processed_data)
