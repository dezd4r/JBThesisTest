from Map import MyMap

def main():
    numberOfCells = int(input("Insert your number of cells: "))
    heightOfcell = int(input("Insert your Cell's height: "))
    field = MyMap(numberOfCells, heightOfcell)
    field.run_window()

if __name__ == '__main__':
    main()
