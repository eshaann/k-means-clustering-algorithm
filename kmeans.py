import csv
import random
import math
def distance (pointl, point2):
    return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

def k_means clustering (csv_file, k, max_iterations=100):
    # Read point
    points []
    with open (csv_file, 'r') as file:
        reader = csv.reader (file)
        for row in reader:
            if len(row) >= 2:
                point = [float (row[0]), float (row[1])]
                points.append(point)
    
    #set centroids randomly
    centroids = random.sample (points, k)
    for z in range (max_iterations):
        # Assign nearest centroid to each point
        labels = []
        for point in points:
            distances = [distance (point, centroid) for centroid in centroids] 
            label = distances.index (min (distances))
            labels.append(label)
        
        #Update centroids 
        new_centroids = []
        for i in range (k):
            cluster_points = [point for point, label in zip(points, a) if label == i]
            centroid = [sum(coord) / len(cluster_points) for coord in zip(*cluster_points)]
            new_centroids.append(centroid)

        # Check if it stopped moving
        if centroids == new_centroids: 
            break
        centroids = new_centroids
    sum_of_squared_dist = 0.0
    for point, label in zip(points, labels): 
        dist = distance (point, centroids [label]) 
        sum_of_squared_dist += dist ** 2
    print ("D^2 Final", sum_of_squared_dist)
    return centroids, labels
#INSERT YOUR LINK BELOW!!!
csv_file = '/BrooklynTech/Classwork/SomeTextFiles/coordinates.csv'
#ADJUST K AS YOU WANT!!!
k = 2
centroids, labels = k_means_clustering (csv_file, k)
print ("Final Centroids:")
for centroid in centroids:
    print (centroid)
