contents = []

# Read the input
while True:
    try:
        line = list(map(int, input().split(' ')))
    except EOFError:
        break
    contents.append(line)

# Remove the first line of the input and save the remaining lines
instances = contents[1:]

def CountSort(instance):
    # If the instance is a single element, return it and 0
    if len(instance) == 1:
        return instance, 0
    # If the instance is more than one element
    else:
        # Split the instance into two halves
        A1 = instance[:len(instance)//2]
        A2 = instance[len(instance)//2:]

        # Recursively call CountSort on the two halves
        A1, c1 = CountSort(A1)
        A2, c2 = CountSort(A2)

        # Merge the two halves and count the number of inversions
        A, c = MergeCount(A1, A2)

        # Return the sorted instance and the number of inversions
        return A, c1 + c2 + c

def MergeCount(A1, A2):
    # Initialize the sorted instance and the number of inversions
    S = []
    c = 0
    # print("A1, A2:", A1, A2)
    while len(A1) > 0 or len(A2) > 0:
        # If A1 is empty, append the first element of A2 to S
        if len(A1) == 0:
            S.append(A2.pop(0))
        # If A2 is empty, append the first element of A1 to S
        elif len(A2) == 0:
            S.append(A1.pop(0))
        elif A1[0] > A2[0]:
            # If the first element of A2 is smaller, pop it from A2 and append it to S, and increment c by the length of A1
            S.append(A2.pop(0))
            c += len(A1)
        else:
            # If the first element of A1 is smaller, pop it from A1 and append it to S
            S.append(A1.pop(0))
    return S, c

for i in range(1, len(instances), 2):
    A, c = CountSort(instances[i])
    print(c)







            


