import os
os.system("cls")
var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

# 1. Mencari data pada index tertentu
print("1. Data pada index tertentu:")
print(f"Arsel di Index {var.index('Arsel')}")
print(f"Avivah di Index {var.index('Avivah')}")
print(f"Daiva di Index {var.index('Daiva')}\n")

# 2. Mencari data pada nested list dengan jump search
def jump_search(arr, x):
    n = len(arr)
    step = int(n ** 0.5)
    prev = 0
    while arr[min(step, n)-1][0] < x:
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1
    while arr[prev][1] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev][1] == x:
        return prev
    return -1

print("2. Mencari data pada nested list:")
wahyu_index = jump_search(var[3], "Wahyu")
wibi_index = jump_search(var[3], "Wibi")
print(f"Wahyu di Index 3 pada kolom 0: {var[3].index('Wahyu')}")
print(f"Wibi di Index 3 pada kolom 1: {var[3].index('Wibi')}")
