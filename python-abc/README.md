# **Python - Abstract Classes and Interfaces**

## **Description**
Ce projet explore les concepts avancés de la **programmation orientée objet (OOP)** en Python, notamment :
- **Les classes abstraites** et leur rôle dans la définition d'interfaces communes.
- **Le duck typing** et son utilisation en Python.
- **L'héritage et la surcharge de méthodes**.
- **L'extension des classes Python standard**.
- **L'héritage multiple et les mixins**.

Ce projet vise à améliorer la compréhension et l'application des principes de conception orientée objet en Python.

---

## **Objectifs d'apprentissage**
À la fin de ce projet, tu devrais être capable de :
✔ Comprendre et appliquer les **classes abstraites** en Python.  
✔ Utiliser les **interfaces et le duck typing** pour des conceptions flexibles.  
✔ Étendre des **classes standard** comme `list`, `iterator`.  
✔ Maîtriser **l'héritage multiple et les mixins**.  
✔ Comprendre l'**ordre de résolution des méthodes (MRO)**.  

---

## **Pré-requis**
- **Python 3.x** installé
- Connaissance des bases de la programmation orientée objet
- Familiarité avec les modules **abc**, **super()**, **isinstance()**, et **__mro__** en Python.

---

## **Installation**
1. **Cloner le dépôt GitHub :**
   ```bash
   git clone https://github.com/hmeyd/holbertonschool-higher_level_programming.git
   cd holbertonschool-higher_level_programming/python-abc
   ```

2. **Exécuter les fichiers de test :**
   ```bash
   python3 main_00_abc.py
   python3 main_01_duck_typing.py
   python3 main_02_verboselist.py
   python3 main_03_countediterator.py
   python3 main_04_flyingfish.py
   python3 main_05_dragon.py
   ```

---

## **Contenu du projet**
| Fichier | Description |
|---------|------------|
| `task_00_abc.py` | Implémente une classe abstraite `Animal` et ses sous-classes `Dog` et `Cat`. |
| `task_01_duck_typing.py` | Déclare une classe `Shape` et ses sous-classes `Circle` et `Rectangle`, avec du **duck typing**. |
| `task_02_verboselist.py` | Étend la classe `list` en `VerboseList` pour afficher des notifications lors des modifications. |
| `task_03_countediterator.py` | Crée un `CountedIterator` pour suivre le nombre d'éléments itérés. |
| `task_04_flyingfish.py` | Implémente `FlyingFish`, héritant de `Fish` et `Bird`, et analyse le MRO. |
| `task_05_dragon.py` | Utilise des **mixins** pour donner à `Dragon` la capacité de voler et nager. |

---

## **Exemples d'utilisation**
### **0. Classes Abstraites - `task_00_abc.py`**
```python
bobby = Dog()
garfield = Cat()

print(bobby.sound())  # Bark
print(garfield.sound())  # Meow

animal = Animal()  # TypeError: Can't instantiate abstract class Animal
```

### **1. Duck Typing - `task_01_duck_typing.py`**
```python
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)  
# Output: 
# Area: 78.54
# Perimeter: 31.41

shape_info(rectangle)  
# Output:
# Area: 28
# Perimeter: 22
```

### **2. Liste améliorée - `task_02_verboselist.py`**
```python
vl = VerboseList([1, 2, 3])
vl.append(4)  # Output: Added [4] to the list.
vl.remove(2)  # Output: Removed [2] from the list.
```

### **3. Itérateur compté - `task_03_countediterator.py`**
```python
data = [1, 2, 3, 4]
counted_iter = CountedIterator(data)

for item in counted_iter:
    print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
```

### **4. Poisson volant - `task_04_flyingfish.py`**
```python
flying_fish = FlyingFish()
flying_fish.swim()  # Output: The flying fish is swimming!
flying_fish.fly()  # Output: The flying fish is soaring!
```

### **5. Dragon avec Mixins - `task_05_dragon.py`**
```python
dragon = Dragon()
dragon.swim()  # Output: The creature swims!
dragon.fly()   # Output: The creature flies!
dragon.roar()  # Output: The dragon roars!
```

---

## **Commandes utiles**
- **Lister les méthodes disponibles dans une classe :**
  ```python
  print(dir(ClassName))
  ```
- **Afficher l'ordre de résolution des méthodes (`MRO`) :**
  ```python
  print(ClassName.__mro__)
  ```
- **Exécuter un script de test :**
  ```bash
  python3 main_XX_nom_du_fichier.py
  ```

---

## **Auteurs**
- **Javier Valenzani** (Projet original)  
- **hmeyd** (Implémentation et corrections)  

---

## **Licence**
📜 Ce projet est sous licence **MIT**. Vous pouvez l'utiliser et le modifier librement.
