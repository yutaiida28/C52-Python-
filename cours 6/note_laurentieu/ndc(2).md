self.\_\_nom_variable

pourquoi mettre un \_\_ ?

1 - Pour que la variable soit protected, mais en réalité, elle n'est pas vraiment private en python, car on peut toujours y accèder grâce au name Mangling. Ce n est pas une vraie protection comme en java ou c++

class Legume:
def **init**(self):
self.\_\_patate = "cachée"
self.\_carotte = "semi-cachée"
self.tomate = "publique"

legume = Legume()

print(legume.tomate) # OK -> "publique"
print(legume.\_carotte) # OK -> "semi-cachée" (mais convention = ne pas toucher)
print(legume.**patate) # ERREUR -> AttributeError
print(legume.\_Legume**patate) # OK -> "cachée"

class A:
def **init**(self):
self.**data = 42 # devient self.\_A**data

class B(A):
def **init**(self):
super().**init**()
self.**data = 99 # devient self.\_B**data

Comment utiliser des Getters ?

En utilisant les @property

class Compte:
def **init**(self, solde):
self.\_\_solde = solde # Attribut "caché"

    @property
    def solde(self):
        """Getter : permet de lire le solde sans accès direct"""
        return self.__solde

    @solde.setter
    def solde(self, valeur):
        """Setter : permet de contrôler l'écriture"""
        if valeur < 0:
            raise ValueError("Le solde ne peut pas être négatif")
        self.__solde = valeur

c = Compte(100)

print(c.solde) # passe par le getter -> 100

c.solde = 200 # passe par le setter -> OK
print(c.solde) # 200

c.solde = -50 # Erreur : ValueError, car il y a un if avec le ValueError

A quoi sert le Emit

tu cree un sigmal avec une variable

tu utilise la variable et tu .emit la nouvelle valeur

tu prends la variable et tu la connecte a la fonction

class MaClasse(QWidget):
mon_signal = QtCore.Signal(int)

    def ma_methode(self, valeur):  # Pas de @Slot
        print(f"Reçu : {valeur}")

    def __init__(self):
        self.mon_signal.connect(self.ma_methode)  # ✅ Ça marche !
        self.mon_signal.emit(42)
