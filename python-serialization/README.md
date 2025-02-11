# Python - Serialization

---

## **Description**
Ce projet vise à explorer les concepts fondamentaux de la **sérialisation** et du **marshaling**, qui sont essentiels pour le stockage et la transmission efficace des données. Vous apprendrez à transformer des structures de données en formats compatibles avec les fichiers et les réseaux.

Dans ce projet, vous allez découvrir comment :
- **Convertir des objets Python en formats sérialisés** (JSON, Pickle, CSV, XML)
- **Sauvegarder et charger des objets à partir de fichiers**
- **Comprendre les implications de la sérialisation sur la performance et l’interopérabilité**

---

## **📌 Concepts abordés**
- **Marshaling** : Transformer un objet mémoire en un format standardisé pour le stockage ou la transmission.
- **Sérialisation** : Convertir des objets ou des structures en un format pouvant être stocké ou transmis (JSON, Pickle, XML...).
- **Désérialisation** : Reconstruire un objet à partir d’une structure sérialisée.
- **Formats de sérialisation** : JSON, Pickle, XML, CSV.

---

## **🎯 Objectifs d’apprentissage**
✔ Comprendre la différence entre **marshaling** et **sérialisation**  
✔ Implémenter la **sérialisation et la désérialisation** en Python  
✔ Utiliser différents formats de sérialisation : **JSON, Pickle, CSV, XML**  
✔ Gérer les erreurs et assurer la **compatibilité des données**  

---

## **📚 Ressources utiles**
🔗 [Real Python - Serialization](https://realpython.com/python-json/)  
🔗 [Python Pickle Documentation](https://docs.python.org/3/library/pickle.html)  
🔗 [Corey Schafer - Pickle Tutorial](https://www.youtube.com/watch?v=2Tw39kZIbhs)  
🔗 [Python CSV Guide](https://realpython.com/python-csv/)  
🔗 [Python XML ElementTree Guide](https://docs.python.org/3/library/xml.etree.elementtree.html)  

---

## **📌 Tâches du projet**

### **0️⃣ Basic Serialization**
📁 **Fichier** : `task_00_basic_serialization.py`  
💡 **Objectif** : Sérialiser un dictionnaire Python en JSON et l’enregistrer dans un fichier.  

**Instructions :**
- Écrire une fonction `serialize_and_save_to_file(data, filename)` pour **convertir et sauvegarder** un dictionnaire en JSON.
- Écrire une fonction `load_and_deserialize(filename)` pour **charger et désérialiser** un fichier JSON en dictionnaire.
- Si le fichier existe déjà, il doit être **remplacé**.

```python
def serialize_and_save_to_file(data, filename):
    pass  # Implémentation à faire

def load_and_deserialize(filename):
    pass  # Implémentation à faire
```

**Exécution :**
```bash
$ python3 main_00_json.py
Data serialized and saved to 'data.json'.
Deserialized Data:
{'name': 'John Doe', 'age': 30, 'city': 'New York'}
```

---

### **1️⃣ Pickling Custom Classes**
📁 **Fichier** : `task_01_pickle.py`  
💡 **Objectif** : Sérialiser un objet personnalisé avec `pickle`.

**Instructions :**
- Créer une classe `CustomObject` avec les attributs :
  - `name` (chaîne)
  - `age` (entier)
  - `is_student` (booléen)
- Ajouter une méthode `display()` pour afficher l’objet.
- Ajouter :
  - `serialize(self, filename)`: Sérialise l’objet en fichier.
  - `@classmethod deserialize(cls, filename)`: Charge un objet depuis un fichier.

```python
class CustomObject:
    def serialize(self, filename):
        pass  # Implémentation à faire

    @classmethod
    def deserialize(cls, filename):
        pass  # Implémentation à faire
```

**Exécution :**
```bash
$ python3 main_01_pickle.py
Original Object:
Name: John
Age: 25
Is Student: True

Deserialized Object:
Name: John
Age: 25
Is Student: True
```

---

### **2️⃣ Converting CSV Data to JSON**
📁 **Fichier** : `task_02_csv.py`  
💡 **Objectif** : Lire un fichier **CSV** et le convertir en **JSON**.

**Instructions :**
- Lire un fichier CSV avec `csv.DictReader`
- Convertir chaque ligne en **dictionnaire**
- Sauvegarder en JSON (`data.json`)
- Retourner `True` en cas de succès, `False` en cas d'erreur.

```python
def convert_csv_to_json(csv_filename):
    pass  # Implémentation à faire
```

**Exécution :**
```bash
$ python3 main_02_csv.py
Data from data.csv has been converted to data.json
```

📂 **Exemple de `data.json` généré :**
```json
[
    {"name": "John", "age": "28", "city": "New York"},
    {"name": "Alice", "age": "24", "city": "Los Angeles"},
    {"name": "Bob", "age": "22", "city": "Chicago"},
    {"name": "Eve", "age": "30", "city": "San Francisco"}
]
```

---

### **3️⃣ Serializing and Deserializing with XML**
📁 **Fichier** : `task_03_xml.py`  
💡 **Objectif** : Utiliser **XML** comme format de sérialisation.

**Instructions :**
- `serialize_to_xml(dictionary, filename)` : Sérialise un dictionnaire en XML.
- `deserialize_from_xml(filename)` : Charge un dictionnaire à partir d’un fichier XML.

```python
def serialize_to_xml(dictionary, filename):
    pass  # Implémentation à faire

def deserialize_from_xml(filename):
    pass  # Implémentation à faire
```

**Exécution :**
```bash
$ python3 main_03_xml.py
Dictionary serialized to data.xml

Deserialized Data:
{'name': 'John', 'age': '28', 'city': 'New York'}
```

📂 **Exemple de `data.xml` généré :**
```xml
<data>
    <name>John</name>
    <age>28</age>
    <city>New York</city>
</data>
```

---

## **📁 Organisation du projet**
```
📂 holbertonschool-higher_level_programming
 ├── 📂 python-serialization
 │   ├── task_00_basic_serialization.py
 │   ├── task_01_pickle.py
 │   ├── task_02_csv.py
 │   ├── task_03_xml.py
 │   ├── main_00_json.py
 │   ├── main_01_pickle.py
 │   ├── main_02_csv.py
 │   ├── main_03_xml.py
```

---

## **✅ Validation et scoring**
🎯 **Score maximum** : 14 points  
📌 **Vérifiez que toutes les fonctionnalités sont implémentées correctement** avant la soumission.  

---

## **🚀 Conclusion**
À la fin de ce projet, vous aurez une **compréhension approfondie** des techniques de **sérialisation et désérialisation** en Python. Ces compétences sont essentielles pour :
- **Stocker des données de manière persistante**
- **Échanger des informations entre différentes applications**
- **Optimiser le transport de données sur le réseau**

💡 **Prêt à coder ? Lancez-vous !** 🚀