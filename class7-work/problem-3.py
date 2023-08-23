# 3 - Write a program that allows you to enter the height of 10 students, 
# then show the average height, and how many elements are above average, 
# how many are below average.

def main():
    heights = []

    for i in range(1, 11):
        height = float(input(f"Enter the height of student {i}: "))
        heights.append(height)

    average_height = sum(heights) / len(heights)

    above_average = 0
    below_average = 0
    for height in heights:
        if height > average_height:
            above_average += 1
        elif height < average_height:
            below_average += 1

    print(f"Average height: {average_height:.2f}")
    print(f"Number of students above average: {above_average}")
    print(f"Number of students below average: {below_average}")

main()
        