import pygame
import random

def DrawChart(screen ,lines):
    for l in lines:
        pygame.draw.line(screen, (0,0,0), (l[0][0], l[0][1]) , (l[1][0], l[1][1]), 5)

def detenctCollide(r1,r2):
    if pygame.Rect.colliderect(r1,r2):
        return True
def MoveR(graph):
    if(graph.obj1.x + graph.obj1.w < graph.x + graph.w):
        graph.obj1.x += 1

def MoveL(graph):
    if(graph.obj1.x > graph.x):
        graph.obj1.x -= 1

class Graph:
    def __init__(self,x,y,obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2
        self.x = x
        self.y = y
        self.h = 300
        self.w = 450
        self.color1 = (random.randint(3,200),random.randint(3,200),random.randint(3,200))
        self.color2 = (random.randint(3,200),random.randint(3,200),random.randint(3,200))
        self.conv_area_trace = 0
        self.h_conv = self.h
        self.x_conv = self.x

    def display(self, screen):

        pygame.draw.line(screen, (0,0,0), (self.x, self.y), (self.x, self.y - self.h), 5)
        pygame.draw.line(screen, (0,0,0), (self.x, self.y), (self.x + self.w, self.y), 5)
        pygame.draw.rect(screen,self.color1, self.obj1)
        pygame.draw.rect(screen,self.color2, self.obj2)

    def traceChart(self, convArea, lines, graph2):
        
        if(self.obj1.x < self.obj2.x and self.obj1.x + self.obj1.w > self.obj2.x):
            if(lines == []):
                lines.append([[graph2.x, graph2.y],[graph2.x +1, self.y - (convArea // 100)], self.obj1.x + self.obj1.w])
            else:
                if(lines[0][2] < self.obj1.x + self.obj1.w):
                    lines[0][1][1] = self.y - (convArea // 100)
                    lines[0][1][0] += 1
                    lines[0][2] = self.obj1.x + self.obj1.w
                else:
                    pass
            
        elif(self.obj1.x >= self.obj2.x and self.obj1.x + self.obj1.w <= self.obj2.x + self.obj2.w):
            if(len(lines) == 1):
                lines.append([[lines[0][1][0], lines[0][1][1]],[lines[0][1][0]+1,lines[0][1][1]], self.obj1.x + self.obj1.w])
            else:
                if(lines[1][2] < self.obj1.x + self.obj1.w):
                    lines[1][1][0] += 1
                    lines[1][2] = self.obj1.x + self.obj1.w
        elif(self.obj1.x + self.obj1.w > self.obj2.x + self.obj2.w and self.obj1.x < self.obj2.x + self.obj2.w):
            if(len(lines) == 2):
                lines.append([[lines[1][1][0], lines[1][1][1]],[lines[1][1][0]+1,lines[1][1][1]], self.obj1.x + self.obj1.w])
            else:
                if(lines[2][2] < self.obj1.x + self.obj1.w):
                    lines[2][2] = self.obj1.x + self.obj1.w
                    lines[2][1][1] = self.y - (convArea // 100)
                    lines[2][1][0] += 1