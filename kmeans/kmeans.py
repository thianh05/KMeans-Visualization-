import pygame
from random import randint
import math
from sklearn.cluster import KMeans

def distance(p1,p2):
    return math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))

pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("kmeans visualization")

running = True
clock = pygame.time.Clock()


# Màu sắc
BACKGROUND = (214, 214, 214)
BLACK = (0, 0, 0)
BACKGROUND_PANEL = (249, 255, 230)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (147, 153, 35)
PURPLE = (255,0,255)
SKY = (0,255,255)
ORANGE = (255,125,25)
GRAPE = (100,25,125)
GRASS = (55,155,65)

COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, SKY, ORANGE, GRAPE, GRASS]

font = pygame. font. SysFont('sans', 40)
font_small = pygame. font.SysFont('sans', 20)
text_plus = font.render('+', True, WHITE)
text_minus = font.render('-', True, WHITE)
text_run = font.render("Run", True, WHITE)
text_random = font.render("Random", True, WHITE)
text_algorithm = font.render("Algorithm", True, WHITE)
text_reset = font.render("Reset", True, WHITE)

#--------------
K = 0
error = 0
points = [] 
clusters = []
labels = []

#--------------

while running:
    clock.tick(60)
    screen.fill(BACKGROUND)
    
    # --- DRAW INTERFACE ---
    # khung ngoài (đen)
    pygame.draw.rect(screen, BLACK, (50, 50, 700, 500))
    # panel bên trong
    pygame.draw.rect(screen, BACKGROUND_PANEL, (55, 55, 690, 490))

    # K button +
    pygame.draw.rect(screen, BLACK, (850, 50, 50, 50))
    screen.blit(text_plus, (860, 50))

    # K button -
    pygame.draw.rect(screen, BLACK, (950, 50, 50, 50))
    screen.blit(text_minus, (960, 50))

    # K value
    text_k = font.render("K = " + str(K), True, BLACK)
    screen.blit(text_k, (1050, 50))

    # Run Button
    pygame.draw.rect(screen, BLACK, (850, 150, 150, 50))
    screen.blit(text_run, (900, 150))

    # Random Button
    pygame.draw.rect(screen, BLACK, (850, 250, 150, 50))
    screen.blit(text_random, (850, 250))

    # Algorithm Button
    pygame.draw.rect(screen, BLACK, (850, 350, 150, 50))
    screen.blit(text_algorithm, (860, 350))

    # Reset Button
    pygame.draw.rect(screen, BLACK, (850, 450, 150, 50))
    screen.blit(text_reset, (880, 450))

    # --- Lấy tọa độ chuột ---
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # --- Bắt sự kiện ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Create point on panel
            if 50 < mouse_x < 750 and 50 < mouse_y < 550:
                labels = []
                point = [mouse_x - 50, mouse_y - 50]  # quy về tọa độ panel
                points.append(point)
                print(points)

            # Change K button +
            if 850 < mouse_x < 900 and 50 < mouse_y < 100:
                if K < 8 :
                    K += 1
                print("Press K +")

            # Change K button -
            if 950 < mouse_x < 1000 and 50 < mouse_y < 100:
                if K > 0:
                    K -= 1
                print("Press K -")

            # Run button
            if 850 < mouse_x < 1000 and 150 < mouse_y < 200:
                labels = []

                if len(clusters) == 0:
                    continue
                # Assign point to closet clusters
                for p in points:
                    distance_to_clusters = []
                    for c in clusters:
                        dis = distance(p, c)
                        distance_to_clusters.append(dis)

                    min_distance = min(distance_to_clusters)
                    label = distance_to_clusters.index(min_distance)
                    labels.append(label)
                # Update clusters
                for i in range(K):
                    sum_x = 0
                    sum_y = 0
                    count = 0
                    for j in range(len(points)):
                        if j < len(labels) and labels[j] == i:
                            sum_x += points[j][0]
                            sum_y += points[j][1]
                            count += 1 
                    if count != 0:
                        new_cluster_x = sum_x / count
                        new_cluster_y = sum_y / count
                        clusters[i] = [new_cluster_x, new_cluster_y]

                print("Run pressed")
            # Random button
            if 850 < mouse_x < 1000 and 250 < mouse_y < 300:
                labels = []
                clusters =[]
                for i in range (K):
                    random_point = [randint(0,700), randint(0,500)]
                    clusters.append(random_point)
                print("Random Pressed")

            # Algorithm button
            if 850 < mouse_x < 1000 and 350 < mouse_y < 400:
                if K > 0 and len(points) >= K:
                    kmeans = KMeans(n_clusters=K).fit(points)
                    labels = kmeans.predict(points) 
                    clusters = kmeans.cluster_centers_ 
                    print("Algorithm button pressed")

            # Reset button
            if 850 < mouse_x < 1000 and 450 < mouse_y < 500:
                K = 0
                error = 0
                labels = []
                points = []
                clusters = [] 
                print("Reset pressed, K reset to 0 and points cleared")
    # --- Draw Clusters --- 
    for i in range(len(clusters)):
        pygame.draw.circle(screen, COLORS[i], (int(clusters[i][0])+ 50 , int(clusters[i][1]) + 50), 10)

    # --- Draw point ----
    for p in points:
        pygame.draw.circle(screen, BLACK, (p[0] + 50, p[1] + 50), 6)

        if len(labels) == 0:
            pygame.draw.circle(screen, WHITE, (p[0] + 50, p[1] + 50), 5)
        else:
            pygame.draw.circle(screen, COLORS[labels[points.index(p)]], (p[0] + 50, p[1] + 50), 5)

    # Calculate and draw Error
    error = 0
    if len(clusters) > 0 and len(labels) > 0:


        for i in range (len(points)):
            error += distance( points[i] , clusters[labels[i]])
    
    text_error = font.render("Error = " + str(int(error)), True, BLACK)
    screen.blit(text_error, (850, 550))
    pygame.display.flip()

pygame.quit()
