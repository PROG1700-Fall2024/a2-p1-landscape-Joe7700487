#Program 1 – Landscape Calculator
#A landscaping company needs a program that computes the price of landscaping for a new housing development. 

#Student #:     0500154
#Student Name:  Joseph Petrash


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    # init variables
    print("Landscape Calculator")
    houseNumber = int(input("House Number: "))
    length = float(input("Plot length in feet: "))
    width = float(input("Plot width in feet: "))
    area = length * width
    grassType = input("Type of grass: ").lower()
    trees = int(input("Number of trees: "))
    total = 1000

    # if the area is more than 5000 sqr feet, add $500
    if (area > 5000):
        total = total + 500
    else:
        pass
    
    # add correct grass rate based off user input
    if (grassType == "fescue"):
        total = total + area * 0.05
    elif (grassType == "bentgrass"):
        total = total + area * 0.02
    elif (grassType == "campus"):
        total = total + area * 0.01
    else:
        print("invalid grass type")

    # add $100 for every tree
    total = total + trees * 100

    # print final output
    print("Total cost for house #{0}: ${1:.2f}".format(houseNumber, total))
    # YOUR CODE ENDS HERE
main()

# A landscaping company needs a program that computes the price of landscaping for a new housing development. 
# Work orders are based on: address, plot length and width in feet, type of grass (“fescue”, “bentgrass” or “campus”), 
# and number of trees. The price is computed as follows:
# There is a base labour charge of $1000. 
# If the surface (length * width) is over 5000 square feet, add $500.
# The cost is calculated per square foot. 
# If the grass is “fescue” the cost is $0.05; for “bentgrass” it is $0.02; “campus” is $0.01.
# Each tree requested has a $100 charge.