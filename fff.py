print("helo")

## linear search
print("Hello, World!")

def linearSearch(ls, value):
    for i in range(len(ls)):
        if ls[i] == value:
            return i
        
    return -1

