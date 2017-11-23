import util
import random

class Cluster:
    def __init__(self):
        """
        self.clusters will be a dictionary where self.clusters[coordinate] = cluster
        :param k: k clusters
        :param addresses: list of addresses to parse, for now just lat/lon coordinates
        """
        ## self.clusters[cluster] = list of coordinates
        self.clusters = {}
        ## self.centroids[cluster] = centroid
        self.centroids = {}

    def euclideanDistance(self,(x1, y1), (x2, y2)):
        return util.euclideanDistance((x1, y1), (x2, y2))

    def kmeans(self, addresses, k):
        for elt in addresses:
            ## randomly assign coordinates to cluster
            randomInt = random.randint(0, k - 1)
            if randomInt in self.clusters:
                self.clusters[randomInt].append(elt)
            else:
                self.clusters[randomInt] = [elt]
        ## update centroids given new clustering
        self.centroids = self.update(self.clusters)

        ## while the clustering assignments change continue algorithm
        while True:
            newClusters = self.assignment(addresses, self.centroids, k)
            if self.clusters == newClusters:
                return self.clusters, self.centroids
            else:
                ## update clusters using old centroids, then update centroids using new clusters
                self.clusters = newClusters
                self.centroids = self.update(self.clusters)


    def assignment(self, addresses, centroids, k):
        """
        Assign new clustering given new centroids
        :param self:
        :param centroids:
        :return:
        """
        newClusters = {}
        for (lat, long) in addresses:
            minDistance = float('Inf')
            minIndex = 0
            for i in range(k):
                if self.euclideanDistance((lat, long), centroids[i]) < minDistance:
                    minDistance = self.euclideanDistance((lat, long), centroids[i])
                    minIndex = i
            if minIndex in newClusters:
                newClusters[minIndex].append((lat, long))
            else:
                newClusters[minIndex] = [(lat, long)]
        return newClusters

    def update(self, clusters):
        """
        Updates centroids given new clustering
        :param self:
        :param clusters:
        :return:
        """
        centroids = {}
        for cluster, coordinates in clusters.iteritems():
            sumLat = 0
            sumLong = 0
            for coordinate in coordinates:
                sumLat += float(coordinate[0])
                sumLong += float(coordinate[1])
            centroids[cluster] = (sumLat/float(len(coordinates)), sumLong/float(len(coordinates)))
        return centroids
