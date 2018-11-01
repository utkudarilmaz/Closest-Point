import random
import math


class Point():

    def __init__(self, x=None, y=None):

        if x and y is not None:
            self.x = x
            self.y = y
        else:
            self.x = random.randint(-10, 10)
            self.y = random.randint(-10, 10)


    def distance(n1, n2):
        distance = math.sqrt((n2.x - n1.x)**2 + (n2.y - n1.y)**2)
        return distance


class Collection():

    def __init__(self):

        self.points = []
        self.userPoint = Point(0, 0)
        self.closestPoints = []
        self.totalPoint = len(self.points)


    def user_point(self):
        try:
            userX = int(input("X point: "))
            userY = int(input("Y point: "))
            if userX > 10 or userX < -10 or userY > 10 or userY < -10:
                raise ValueError
            self.userPoint = Point(userX, userY)

        except ValueError:
            print("Lutfen -10 ila 10 arasinda degerler giriniz!")
            return self.user_point()


    def generate_point(self, total):
        for i in range(total):
            collection.points.append(Point())

        self.totalPoint = len(self.points)


    def find_closest(self):

        for i in range(self.totalPoint):

            if len(self.closestPoints) < 5:
                self.closestPoints.append(self.points[i])
            else:
                for j in range(5):
                    if (Point.distance(self.userPoint, self.points[i]) <
                        Point.distance(self.userPoint, self.closestPoints[j])):
                        del self.closestPoints[j]
                        self.closestPoints.append(self.points[i])

                        break


    def print_closest(self):
        for i in range(5):
            print("(" + str(self.userPoint.x) + "," + str(self.userPoint.y) +
                  ")" + " closest point: " +
                  "(" + str(self.closestPoints[i].x) + "," +
                  str(self.closestPoints[i].y) + ")" +
                  " Distance: " + str(Point.distance(self.userPoint,
                                                    self.closestPoints[i])))


if __name__ == "__main__":

    collection = Collection()
    collection.generate_point(100)
    collection.user_point()
    collection.find_closest()
    collection.print_closest()
