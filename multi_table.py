import pandas


class MultiTable:
    __slots__ = ['_mod_n', '_dist']

    def __init__(self, n):
        self._mod_n = n
        self._dist = {}
        self._populate_dist()

    def _populate_dist(self):
        for x in range(self._mod_n):
            self._dist[x] = [(x * y) % self._mod_n for y in range(self._mod_n)]
        return self._dist

    def square(self, a):
        """finds the equivalent of the square root of a in the ring Z mod n"""
        ans = []
        if a < 0:
            a = a % self._mod_n
        for k in range(self._mod_n):
            if self._dist[k][k] == a:
                ans.append(k)
        return ans

    def fraction(self, a, b):
        """
        finds the equivalent of the fraction a/b in the ring Z mod n
        but doesn't check for fraction equaling zero
        """
        ans = []
        a = a % self._mod_n
        b = b % self._mod_n
        for k in range(self._mod_n):
            if self._dist[b][k] == a:
                ans.append(k)
        return ans

    def __str__(self):
        return pandas.DataFrame(self._dist).to_string()


if __name__ == '__main__':

    for num in range(2, 101):
        mod = MultiTable(num)
        print("{}: {}".format(num, mod.square(-1)))

    mod = MultiTable(10)
    print(mod)
