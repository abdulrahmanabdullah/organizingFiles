import os
class Organizing:

    def getFilesName(self, fname):
        return fname.split("_")[0]



    def makeDirectory(self, placesList):
        for place in placesList:
            if not os.path.exists(place):
                os.mkdir(place)

    def startOrganizing(self):
        listOfFiles = os.listdir()
        placesList = []
        for fileName in listOfFiles:
            place = self.getFilesName(fileName)
            if place not in placesList:
                placesList.append(place)
        self.makeDirectory(placesList)





if __name__ == "__main__" :
    t = Organizing()
    t.startOrganizing()
