# ON MODULARIZATION AND VARIABLES SCOPE.
# WRITE AN ALGORITHM THAT INVOKES ANOTHER ONE, AND THE INVOKED ONE PRINTS A VALUE.
def algo_1():
    print("this will invoke algorithm 2")
    algo_2()

def algo_2():
    print("this is algo 2")

algo_1()