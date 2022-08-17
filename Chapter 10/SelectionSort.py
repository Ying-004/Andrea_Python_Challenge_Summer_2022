#  The function for sorting elements i nascending order
def selectionSort(lst):
    for i in range(len(lst) - 1):
        #  Find the minimum in the lst[i : len(lst)]
        currentMin = lst[i]
        currentMinIndex = i

        for j in range (i + 1, len(lst)):
            if currentMin > lst[j]:
                currentMin = lst[j]
                currentMinIndex = j

        # Swap lst[i with lst[currentMinIndex] if necessary
        if currentMinIndex != i:
            lst[currentMinIndex] = lst[i]
            lst[i] = currentMin