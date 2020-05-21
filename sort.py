import pygame
import random
import button

pygame.init()


width = 800
height = 600
n = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("sorting algorithms")
myfont = pygame.font.SysFont('Comic Sans MS', 30)


arr = []
buttons = []
buttons.append(button.Button(100, 10, "bubblesort", screen))
buttons.append(button.Button(250, 10, "quick sort", screen))
buttons.append(button.Button(400, 10, "reset", screen))

def drawArray():
    screen.fill(pygame.Color(255, 255, 255))
    for i in range(len(arr)):
        pygame.draw.rect(screen, pygame.Color(0, 0, 0), (width / n * i, height - arr[i], round(width / n), arr[i]))

def drawButtons():
    for i in range(len(buttons)):
        buttons[i].draw()

def makeArray():
    global arr
    arr = []
    temp = []
    for i in range(n):
        temp.append(i + 1)

    for i in range(n):
        index = random.randint(0, len(temp)- 1)
        arr.append(temp[index])
        temp.pop(index)


def partion(low, high):
    i = low - 1

    for j in range(low, high):
        #check if arr[j] is less than the arr[high]
        if arr[j] <= arr[high]:
            #increase index of pivot
            i += 1

            arr[i], arr[j] = arr[j], arr[i]
            
            drawArray()
            drawButtons()
            pygame.display.update()
            
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(low, high):
    if low < high:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            

        pi = partion(low, high)

        quicksort(low, pi - 1)
        quicksort(pi + 1, high)

def switch(a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def bubbleSort():
    i = 0
    while i < n:
        for j in range(n - 1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
    
            if(arr[j + 1] < arr[j]):
                switch(j, j + 1)
                screen.fill(pygame.Color(255, 255, 255))
                drawArray()
                drawButtons()
                pygame.display.update()

makeArray()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            for i in range(len(buttons)):
                x, y = pygame.mouse.get_pos()
                if x > buttons[i].x and x < buttons[i].x + buttons[i].w:
                    if y > buttons[i].y and y < buttons[i].y + buttons[i].h:
                        if i == 0:
                            bubbleSort()
                        elif i == 1:
                            quicksort(0, n - 1)
                        else:
                            makeArray()

    drawArray()
    drawButtons()
    pygame.display.update()