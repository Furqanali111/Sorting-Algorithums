import time
def bubblesor(arr):
    n=len(arr)

    for i in range(0,n-1):

        for j in range(0,n-1-i):

            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge(a, b):
    i = j = 0
    sorted_list = []
    while i < len(a) and j < len(b):    #we deleted the len_a and len_b variable
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    while i < len(a):
        sorted_list.append(a[i])
        i += 1
    while j < len(b):
        sorted_list.append(b[j])
        j += 1
    return sorted_list


def division(arr):
    if len(arr) <= 1:
        return arr
    left = arr[:len(arr) // 2] #we removed the mid variable
    right = arr[len(arr) // 2:]
    left = division(left)
    right = division(right)
    return merge(left, right)

def selectionsort(arr):

    for i in range(len(arr)):
        min_indx=i
        for j in range(i+1,len(arr)):
            if arr[min_indx]>arr[j]:
                min_indx=j
                
        arr[i],arr[min_indx]=arr[min_indx],arr[i]
    print("Selection Sort result = ",arr)

if __name__=="__main__":
  a = [12, 11, 13, 5, 6,40,60,23,1232,1,32323,4,6543,0]

  t=time.time()
  print("Array to be sorted = ",a)
  print("Merge Sort result = ",division(a))
  print("Total time by merge sort :", time.time() - t)
  print()
  print("Array to be sorted = ",a)


  b=time.time()
  selectionsort(a)
  print("Total time by selection sort :", time.time() - b)
  print()
  print("Array to be sorted = ",a)

  s=time.time()
  print("Insertion Sort result = ",insertion_sort(a))
  print("Total time by insertion_sort sort :", time.time() - s)
  print()
  print("Array to be sorted = ",a)

  d=time.time()
  print("Bubble Sort result = ",bubblesor(a))
  print("Total time by bubblesort sort :", time.time() - d)

