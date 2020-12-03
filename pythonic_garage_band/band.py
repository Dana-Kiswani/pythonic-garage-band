from abc import abstractmethod, ABC


class Band(ABC):
    kolshiArr = []
# A Band instance should have a name attribute which is a string.
# A Band instance should have a members attribute
    """
    MAIN CONSTRUCTOR
    """

    def __init__(self, name, miembros, lyric):
        self.name = name
        self.miembros = miembros
        self.lyric = lyric

        Band.kolshiArr.append(self)
        # --------------------------

# Use Python classes to model a Band made up of different kinds of musicians

    """
    play_solos method that asks each member musician to play a solo, in the order they were added to band.
    """

    def play_solos(self):

        solooo = []
        for d in self.miembros:
            solooo.append(d.play_solo())
        return solooo
        # -----------

    def play_lyric(self):
        return self.lyric
        # ----------------

    def __str__(self):
        return '{} band, the miembros are {}. Check out thier lyric: {}!'.format(self.name, self.miembros, self.lyric)

        # ---------------

    def __repr__(self):

        return f'{self.name} band, the miembros are {self.miembros}. Check out thier lyric: {self.lyric}'

# -------------------------------------------------------------------
    @classmethod
    def to_list(cls):
        return cls.kolshiArr

class Musician(ABC):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


# I WANNA START WITH 'GUITARIST'
class Guitarist(Musician):

    def play_solo(self):
        return "PweeeeeeeeeeeeeeeeWwWwWwwWWWWWWwwwwwwwww"

    def get_gizmo(self):
        return "Guitar"


# THEN BASSIST
class Bassist(Musician):

    def __init__(self, name, gizmo):
        self.gizmo = gizmo
        super().__init__(name)

    def play_solo(self):
        return "WjWJjwjajajawiwiwiiw"

    def get_gizmo(self):
        return self.gizmo
        

# AND THE LAST ONE IS DRUMMER
class Drummer(Musician):

    def play_solo(self):
        return "PoOoMmMmM pPOMMmmmm PummmMMM"

    def get_gizmo(self):
        return "Drum"


# ----------------------------------
if __name__ == "__main__":
    enrique_iglesias = Guitarist("enrique_iglesias")
    print(f'The Guitarist is {enrique_iglesias}')
    print(f'And she plays ..{enrique_iglesias.get_gizmo()}🎸')
    print(f'Its sounds like 🎵... {enrique_iglesias.play_solo()}...🎶')
    print('-----------------------------------------------------')

    # Michael_Bublé = Bassist("Michael_Bublé")
    # print(f'The Guitarist is {Michael_Bublé}')
    # print(f'And she plays ..{Michael_Bublé.get_gizmo()}🎤')
    # print(f'Its sounds like 🎵... {Michael_Bublé.play_solo()}...🎶')

    avril_lavigne = Drummer("avril_lavigne")
    print(f'The Guitarist is {avril_lavigne}')
    print(f'And she plays ..{avril_lavigne.get_gizmo()}')
    print(f'Its sounds like 🎵... {avril_lavigne.play_solo()}...🎶')
    print('-----------------------------------------------------')
