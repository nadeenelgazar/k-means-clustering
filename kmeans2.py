import numpy
from normalize import normalizeimages


class kmeans:
    #k is set to 3 and tolerance to 0.001 and max number of iteration to 4 if the user didnt send any of them
    def __init__(self, k=3, tolerance=0.001, maxIterantion=4):
        self.k = k
        self.tolerance = tolerance
        self.maxIteration = maxIterantion




    def fit(self,data):
        """""
            parameters are the data normalized already
            at the end of the function each class (cluster) is printed then tha size of each of them
            showing mean"commented"
            printing distorion for each iteration "commented"
            showing samples for each class"commented"
        """""
        #dictionary for centriods and choosing them i dont choose them randomly for the data in the report i changed this part
        self.centroids={}
        for i in range (self.k):

            self.centroids[i]=data[i]


        #looping until max iteration is reached of becoming less than tolerance
        for i in range(self.maxIteration):
            self.classes={}

            #making classes for each centriod
            for i in self.centroids:
                #to show mean
                #show_image(self.centroids[i])
                self.classes[i]=[]


            #calculating ecludian distance and choosing which distance is the smallest to be in this class
            for row in data:
                ecludianDistance=[]
                for centriod in self.centroids:
                   ecludianDistance.append(numpy.linalg.norm(row - self.centroids[centriod]))

                classification = ecludianDistance.index(min(ecludianDistance))
                self.classes[classification].append(row)

            #saving values of centriods in order to check tolerance at the end
            previousCentriods=dict(self.centroids)

            #calculate new centriods numpy.average with axis=0 do this as we do it in the last sheet
            for clas in self.classes:
                self.centroids[clas]=numpy.average(self.classes[clas],axis=0)

            stop=True

            #check tolerance for each centroid
            for centriod in self.centroids:
                if numpy.sum((self.centroids[centriod] - previousCentriods[centriod])/self.centroids[centriod]) > self.tolerance:
                    stop=False

            #to calculate distortion
            distortionvalve = 0
            for j in self.classes:
                distortionclass = 0
                for element in self.classes[j]:
                    x = element - self.centroids[j]
                    squared = x * x
                    distortionclass += squared

                distortionvalve += distortionclass
            #print(distortionvalve)
            if stop:
                break

        for i in self.classes:
            print("class number",i,"is",self.classes[i])

        for i in self.classes:
            print("size of",i,"class is: ",self.classes[i].__len__())

        #for printing samples from classes
        #for i in range(5):
            #show_image(self.classes[2][i])







def main():

    km=kmeans(3)
    normdict=normalizeimages()
    km.fit(normdict)


if __name__ == "__main__":
    main()