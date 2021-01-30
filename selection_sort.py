L = [1,5,3,4,2,0,8,6,7]
def selection_sort(L):
    for i in range(len(L)-1):
        print("\n\n", "-"*50, "Iteration", i)
        min_index = i
        for j in range(i, -1, -1):
            print("\n","*"*80,[L])
            if L[j] > L[min_index]:
                L[j], L[min_index] = L[min_index], L[j]
                min_index = j
                print("Swapped", L[j], L[min_index])
                print("Array is now", L)
print(L)
selection_sort(L)
print(L)
