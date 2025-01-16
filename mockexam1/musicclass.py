'''music class'''

class Song:
    def __init__(self, name, genre, durations):
        self.name = name
        self.genre = genre
        self.duraations = str(durations // 60) + f".{durations - ((durations // 60) *  60):02d}"

    def show_info(self):
        print(f"{self.name} <|> {self.genre} <|> {self.duraations}")

Rickroll = Song(input(), input(), int(input()))
Rickroll.show_info()
