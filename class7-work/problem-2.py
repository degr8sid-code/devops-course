# 2-WRITE AN ALGORITHM THAT INVOKES ANOTHER ONE TO BE CALLED "ADD", 
# THAT RECEIVES TWO NUMBERS. THE "ADD" ALGORITHM MUST ADD THE PARAMETERS. 
# THE INVOKING ALGORITHM SHOULD RECEIVE BACK THAT VALUE AND SHOW IT ON SCREEN.
def main():
    num1 = 5
    num2 = 10
    addNum = add(num1,num2)
    print(addNum)

def add(num1,num2):
    addNum = num1 + num2
    return addNum

main()