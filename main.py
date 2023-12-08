import pygame
import graph

conv = 0
lines = []

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Convolution Visual")
screen = pygame.display.set_mode((1100,600))
color = (100,200,200)
graph1 = graph.Graph(50, 400, pygame.Rect(50,300,100,100),pygame.Rect(200,300,120,100))
graph2 = graph.Graph(550, 400, pygame.Rect(0,0,0,0),pygame.Rect(0,0,0,0))
trace_X = graph1.x
exit = False

assert graph1.obj1.w <= graph1.obj2.w , 'RECT 1 WIDHT MUST BE <= RECT2 WIDHT, CHANGE THIS IN GRAPH1 INIZIALIZATION LINE 12 OF MAIN.PY, SOON I WILL FIX THIS PROBLEM'
assert graph1.obj1.w + graph1.obj2.w < 300 , 'MAKE THE SUM OF THE WIDHT OF THE RECTS < 300 TO ACHIVE BETTER RESULTS, SOON I WILL FIX THIS PROBLEM'


max_w = min(graph1.obj1.w, graph1.obj2.w)

while not exit:
	
    screen.fill(color)
    graph1.display(screen)
    graph2.display(screen)
    graph.DrawChart(screen, lines)
    pygame.display.flip()
    eventso = pygame.key.get_pressed()
    if(eventso[pygame.K_LEFT]):
        graph.MoveL(graph1)
    if(eventso[pygame.K_RIGHT]):
        graph.MoveR(graph1)
    if(graph.detenctCollide(graph1.obj1, graph1.obj2)):
        area_x = min((graph1.obj1.x + graph1.obj1.w)- graph1.obj2.x , max_w, (graph1.obj2.x + graph1.obj2.w) - graph1.obj1.x)
        area_y = min(graph1.obj1.height , graph1.obj1.height)
        area = area_x * area_y
        graph1.traceChart(area,lines, graph2)
    
    for event in pygame.event.get():
		       
        if(event.type == pygame.QUIT):
            exit = True

    clock.tick(250)

	    
