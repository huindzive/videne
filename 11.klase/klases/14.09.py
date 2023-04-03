class sub:
    def __init__(self,s):
        self.cost = s

    def monthly(self,m):
        return m * self.cost

spotify = sub(6.99)

print(spotify.monthly(12))