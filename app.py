class Organizing:

    def __init__(self):


    def getSplitFileName(self, fname):
        return fname.splie("_")[1]

    def makeFolders(self, placesList):
        for place in placesList :
            if not os.path.existi(place):
                os.mkdir(place)
                
    pass


if __name__ = "__main__":
    obj = Organizing()
