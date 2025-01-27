class Square:
    """
    Classe pour définir un carré avec une taille et une position optionnelle.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise un carré avec une taille et une position.
s
        Args:
            size (int): Taille du côté du carré (doit être >= 0).
            position (tuple): Position (décalage) sous forme de tuple (x, y).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(n, int) and n >= 0 for n in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Retourne l'aire du carré.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Affiche une représentation du carré en utilisant '#' et
        tient compte de la position (décalage).
        """
        if self.size == 0:
            print("")
            return
        print("\n" * self.position[1], end="")
        for _ in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)
