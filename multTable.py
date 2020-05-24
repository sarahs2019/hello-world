import pandas

class multTable():

    __slots__ = ['_modn', '__dist']

    def __init__(self, n):
        self._modn = n
        self.__dist = {}

    @property
    def modn(self):
        return self._modn

    @property
    def dist(self):
        return self.__dist

    def _myDist(self):
        eleList = list(range(self.modn))
        for x in eleList:
            self.dist[x] = [(x*y)%self.modn for y in range(self.modn)]
        return self.dist

    def sqrt(self, a):
        '''finds the equivalent of the square root of a in the ring Z mod n'''
        ans = []
        if a < 0:
            a = a%self.modn
        for k in range(self.modn):
            if self.dist[k][k] == a:
                ans.append(k)
        return ans

    def frac(self, a, b):
        '''finds the equivalent of the fraction a/b in the ring Z mod n'''
        # but doesn't check for fractions equaling zero
        ans = []
        a = a%self.modn
        b = b%self.modn
        for k in range(self.modn):
            if self.dist[b][k] == a:
                ans.append(k)
        return ans

    def __repr__(self):
        '''uses pandas module to print each multTable object in a table'''
        self._myDist()
        return pandas.DataFrame(self.dist)


if __name__ == '__main__':

    for x in range(2,101):
        modx = multTable(x)
        modx._myDist()
        print("{}: {}".format(x, modx.sqrt(-1)))

    mod3 = multTable(10)
    mod3._myDist()
    print(pandas.DataFrame(mod3.dist))
