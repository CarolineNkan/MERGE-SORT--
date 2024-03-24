# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:07:21 2024

@author: User
"""

import tkinter as tk
import time

def merge_sort(arr, canvas):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, canvas)
        merge_sort(right_half, canvas)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        canvas.delete("all")
        for idx, val in enumerate(arr):
            canvas.create_text((20 + idx * 20, 20), text=str(val))

        # Delay for visualization
        canvas.update()
        time.sleep(0.5)

# Example usage
arr = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]

root = tk.Tk()
canvas = tk.Canvas(root, width=len(arr) * 20, height=40)
canvas.pack()

merge_sort(arr, canvas)
root.mainloop()
