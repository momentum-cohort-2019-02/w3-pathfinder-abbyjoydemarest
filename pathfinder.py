from PIL import Image

class Map:

    """ this class holds the information for making a map"""
    def __init__(self, filename):
        self.filename = filename
        self.elevations = self.get_elevations(filename)
        self.max_elevation = self.get_max_elevation()
        self.min_elevation = self.get_min_elevation()


    def get_elevations(self, filename):
        self.elevations = []
        with open(filename) as file:
            for line in file:
                self.elevations.append([int(e) for e in line.strip().split(" ")])
        return self.elevations


    def get_max_elevation(self):
        self.max_elevation = max([max(row) for row in self.elevations])
        return self.max_elevation
    

    def get_min_elevation(self):
        self.min_elevation = min([min(row) for row in self.elevations])
        return self.min_elevation


    def define_elevation(self, x, y):
        return self.elevations[y][x]
        

    def get_intensity(self, x, y):
        return int((self.elevations(x, y) - self.min_elevation) / (self.max_elevation - self.min_elevation) * 255)

class MapImage:

    """ this class is the image of the map """
    #bring in self, the map, and the name of the picture you are making?
    def __init__(self, map):
        
        self.map = map
        #make a new image when this is called. so Image.new('RGBA', width and height of image)
        self.im = Image.new('RGBA', (len(self.map.elevations[0]), len(self.map.elevations)))

    
    def draw_the_map(self):
        #do putpixel
        for x in range(len(self.map.get_elevations())):
            for y in range(len(self.map.get_elevations())):
                self.im.putpixel((x, y), (self.map.get_intensity(x, y), self.map.get_intensity(x, y), self.map.get_intensity(x, y)))
                #save the image
        self.im.save('elevations_map.png')


class PathFinder:

    """ this class creates the path to put on the image"""


    def __init__(self):
        pass


if __name__ == "__main__":

    map_key = Map('elevation_small.txt')
    print(map_key.get_intensity, map_key.get_max_elevation, map_key.get_min_elevation)
    make_map = MapImage(map_key)