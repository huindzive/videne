class dziesma:
    def __init__(self,name,artist,album,lenght):
        self.name = name
        self.artist = artist
        self.lenght = lenght
        self.album = album

    def print1(self):
        print(self.artist, ' - ', self.name)

    def print2(self):
        print(self.name,' - ', self.lenght)

    def print3(self):
        print(self.album,' - ',self.artist)

muzika = dziesma('lane boy','21 pilots','blurryface','4.13')

muzika.print1()
muzika.print2()
muzika.print3()