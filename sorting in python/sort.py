import pygame
import random
import sys
import time

# Constants
SCREEN_WIDTH = 910
SCREEN_HEIGHT = 750
ARR_SIZE = 130
RECT_SIZE = 7

# Initialize pygame
pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sorting Visualizer")
clock = pygame.time.Clock()

# Global variables
arr = [0] * ARR_SIZE
Barr = [0] * ARR_SIZE
complete = False

def visualize(x=-1, y=-1, z=-1):
    window.fill((0, 0, 0))

    for i in range(0, SCREEN_WIDTH, RECT_SIZE):
        j = i // RECT_SIZE
        rect_height = arr[j]
        color = (170, 183, 184)  # Default color

        if complete:
            color = (100, 180, 100)
        elif j == x or j == z:
            color = (100, 180, 100)
        elif j == y:
            color = (165, 105, 189)
        
        pygame.draw.rect(window, color, pygame.Rect(i, SCREEN_HEIGHT - rect_height, RECT_SIZE, rect_height))
    
    pygame.display.flip()

def inplace_heap_sort(input_arr):
    n = len(input_arr)
    # Build max heap
    for i in range(1, n):
        child_index = i
        parent_index = (child_index - 1) // 2
        while child_index > 0:
            if input_arr[child_index] > input_arr[parent_index]:
                input_arr[parent_index], input_arr[child_index] = input_arr[child_index], input_arr[parent_index]
                visualize(parent_index, child_index)
                pygame.time.delay(40)
                child_index = parent_index
                parent_index = (child_index - 1) // 2
            else:
                break

    # Heap sort
    for heap_last in range(n - 1, -1, -1):
        input_arr[0], input_arr[heap_last] = input_arr[heap_last], input_arr[0]
        parent_index = 0
        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2
        
        while left_child_index < heap_last:
            max_index = parent_index
            if input_arr[left_child_index] > input_arr[max_index]:
                max_index = left_child_index
            if right_child_index < heap_last and input_arr[right_child_index] > input_arr[max_index]:
                max_index = right_child_index
            if max_index == parent_index:
                break

            input_arr[parent_index], input_arr[max_index] = input_arr[max_index], input_arr[parent_index]
            visualize(max_index, parent_index, heap_last)
            pygame.time.delay(40)
            parent_index = max_index
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

def partition_array(arr, si, ei):
    count_small = sum(1 for i in range(si + 1, ei + 1) if arr[i] <= arr[si])
    c = si + count_small
    arr[si], arr[c] = arr[c], arr[si]
    visualize(c, si)

    i, j = si, ei
    while i < c and j > c:
        if arr[i] <= arr[c]:
            i += 1
        elif arr[j] > arr[c]:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            visualize(i, j)
            pygame.time.delay(70)
            i += 1
            j -= 1
    return c

def quick_sort(arr, si, ei):
    if si >= ei:
        return
    c = partition_array(arr, si, ei)
    quick_sort(arr, si, c - 1)
    quick_sort(arr, c + 1, ei)

def merge2_sorted_arrays(arr, si, ei):
    mid = (si + ei) // 2
    left = arr[si:mid + 1]
    right = arr[mid + 1:ei + 1]
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[si + k] = left[i]
            visualize(-1, si + k)
            i += 1
        else:
            arr[si + k] = right[j]
            visualize(-1, si + k)
            j += 1
        k += 1
    while i < len(left):
        arr[si + k] = left[i]
        visualize(-1, si + k)
        i += 1
        k += 1
    while j < len(right):
        arr[si + k] = right[j]
        visualize(-1, si + k)
        j += 1
        k += 1

def merge_sort(arr, si, ei):
    if si >= ei:
        return
    mid = (si + ei) // 2
    merge_sort(arr, si, mid)
    merge_sort(arr, mid + 1, ei)
    merge2_sorted_arrays(arr, si, ei)

def bubble_sort():
    for i in range(ARR_SIZE - 1):
        for j in range(ARR_SIZE - 1 - i):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                visualize(j + 1, j, ARR_SIZE - 1 - i)
            pygame.time.delay(1)

def insertion_sort():
    for i in range(1, ARR_SIZE):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
            visualize(i, j + 1)
            pygame.time.delay(5)
        arr[j + 1] = temp

def selection_sort():
    for i in range(ARR_SIZE - 1):
        min_index = i
        for j in range(i + 1, ARR_SIZE):
            if arr[j] < arr[min_index]:
                min_index = j
                visualize(i, min_index)
            pygame.time.delay(1)
        arr[i], arr[min_index] = arr[min_index], arr[i]

def load_arr():
    global arr
    arr = Barr.copy()

def randomize_and_save_array():
    global Barr
    Barr = [random.randint(0, SCREEN_HEIGHT) for _ in range(ARR_SIZE)]

def execute():
    global complete
    randomize_and_save_array()
    load_arr()
    quit = False

    while not quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
                complete = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit = True
                    complete = False
                    print("\nEXITING SORTING VISUALIZER.\n")
                elif event.key == pygame.K_0:
                    randomize_and_save_array()
                    complete = False
                    load_arr()
                    print("\nNEW RANDOM LIST GENERATED.\n")
                elif event.key == pygame.K_1:
                    load_arr()
                    print("\nSELECTION SORT STARTED.\n")
                    complete = False
                    selection_sort()
                    complete = True
                    print("\nSELECTION SORT COMPLETE.\n")
                elif event.key == pygame.K_2:
                    load_arr()
                    print("\nINSERTION SORT STARTED.\n")
                    complete = False
                    insertion_sort()
                    complete = True
                    print("\nINSERTION SORT COMPLETE.\n")
                elif event.key == pygame.K_3:
                    load_arr()
                    print("\nBUBBLE SORT STARTED.\n")
                    complete = False
                    bubble_sort()
                    complete = True
                    print("\nBUBBLE SORT COMPLETE.\n")
                elif event.key == pygame.K_4:
                    load_arr()
                    print("\nMERGE SORT STARTED.\n")
                    complete = False
                    merge_sort(arr, 0, ARR_SIZE - 1)
                    complete = True
                    print("\nMERGE SORT COMPLETE.\n")
                elif event.key == pygame.K_5:
                    load_arr()
                    print("\nQUICK SORT STARTED.\n")
                    complete = False
                    quick_sort(arr, 0, ARR_SIZE - 1)
                    complete = True
                    print("\nQUICK SORT COMPLETE.\n")
                elif event.key == pygame.K_6:
                    load_arr()
                    print("\nHEAP SORT STARTED.\n")
                    complete = False
                    inplace_heap_sort(arr)
                    complete = True
                    print("\nHEAP SORT COMPLETE.\n")
        visualize()

def controls():
    print("WARNING: Giving repetitive commands may cause latency and the visualizer may behave unexpectedly. Please give a new command only after the current command's execution is done.\n")
    print("Available Controls inside Sorting Visualizer:-")
    print("    Use 0 to Generate a different randomized list.")
    print("    Use 1 to start Selection Sort Algorithm.")
