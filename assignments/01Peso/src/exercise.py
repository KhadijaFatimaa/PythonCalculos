def main():
    #escribe tu código abajo de esta línea
    print('Hola')
currentweight = float(input("Input your current weight: "))

idealweight = float(input("Input your ideal weight: "))

DietTimeframe = float(input("For how many months will you be in the program?: "))

print("You will need to lose: ",((currentweight - idealweight)/DietTimeframe), "Kilograms per month")
if __name__ == '__main__':
    main()
