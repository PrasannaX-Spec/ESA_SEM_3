def largest_smallest(a,b,c):
    return max(a,b,c), min(a,b,c)

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    
    maximum, minimum = largest_smallest(a, b, c)
    print("Results:")
    print(f"Largest number is: {maximum}")
    print(f"Smallest number is: {minimum}")

if __name__ == "__main__":
    main()