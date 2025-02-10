### 📌 **Python - Input/Output**  
**Projet : Manipulation des fichiers et JSON en Python**  

---

## 📖 **Description**  
Ce projet vise à explorer les concepts fondamentaux liés aux **entrées/sorties (I/O)** en Python, en particulier la lecture et l’écriture de fichiers. Il aborde également la sérialisation et la désérialisation des objets avec **JSON**, ainsi que l’accès aux **paramètres de ligne de commande**.  

Vous apprendrez à :  
✅ Lire et écrire dans des fichiers en utilisant différentes méthodes.  
✅ Manipuler des fichiers avec le mot-clé `with`.  
✅ Convertir des structures de données Python en JSON et inversement.  
✅ Gérer les arguments de la ligne de commande dans un script Python.  

---

## 🎯 **Objectifs d’apprentissage**  

### 🔹 **Manipulation des fichiers**  
- Ouvrir un fichier avec `open("nom_fichier", "mode")`.  
- Lire un fichier en entier (`read()`), ligne par ligne (`readline()`, `readlines()`).  
- Écrire (`write()`, `writelines()`) et ajouter du texte (`append`) dans un fichier.  
- Déplacer le curseur dans un fichier (`seek()`).  
- Fermer correctement un fichier après utilisation (`close()`).  
- Utiliser **le contexte `with`** pour éviter les fuites mémoire.  

### 🔹 **JSON et Sérialisation**  
- Comprendre **ce qu'est JSON** et pourquoi il est utile.  
- Convertir un objet Python en JSON (`json.dumps()`) et enregistrer dans un fichier (`json.dump()`).  
- Charger un fichier JSON et le convertir en objet Python (`json.load()`).  

### 🔹 **Accès aux arguments de ligne de commande**  
- Récupérer les paramètres passés à un script Python avec `sys.argv`.  

---

## 📜 **Exigences du projet**  
✔ **Langage :** Python 3.8.5 (Ubuntu 20.04 LTS)  
✔ **Style de code :** Conforme à **pycodestyle (v2.7.0)**  
✔ **Exécutable :** Tous les fichiers doivent commencer par `#!/usr/bin/python3`  
✔ **Tests :**  
   - Tous les tests doivent être stockés dans un répertoire **`tests/`**  
   - Les modules, classes et fonctions doivent être correctement documentés  
   - Les tests doivent être exécutables avec `python3 -m doctest ./tests/*`  

---

## 📌 **Tâches**  

### **1️⃣ Lire un fichier**  
📌 Écrire une fonction `read_file(filename="")` qui **lit un fichier texte** et l’affiche sur la sortie standard.  

💡 **Méthodes utilisées :**  
- `with open(filename, "r") as f: f.read()`  

---

### **2️⃣ Écrire dans un fichier**  
📌 Fonction `write_file(filename="", text="")` qui **écrit du texte dans un fichier** et retourne le nombre de caractères écrits.  
✅ **Si le fichier existe, il est écrasé**.  
✅ **Si le fichier n’existe pas, il est créé**.  

💡 **Méthodes utilisées :**  
- `with open(filename, "w") as f: f.write(text)`  

---

### **3️⃣ Ajouter du texte à un fichier**  
📌 Fonction `append_write(filename="", text="")` qui **ajoute du texte à la fin d’un fichier**.  

💡 **Méthodes utilisées :**  
- `with open(filename, "a") as f: f.write(text)`  

---

### **4️⃣ Sérialisation JSON**  
📌 Fonction `to_json_string(my_obj)` qui convertit un objet Python en **chaîne JSON**.  
✅ Utilisation de `json.dumps()`  

---

### **5️⃣ Désérialisation JSON**  
📌 Fonction `from_json_string(my_str)` qui **convertit une chaîne JSON en objet Python**.  
✅ Utilisation de `json.loads()`  

---

### **6️⃣ Enregistrer un objet dans un fichier JSON**  
📌 Fonction `save_to_json_file(my_obj, filename)` qui **écrit un objet Python dans un fichier sous format JSON**.  
✅ Utilisation de `json.dump()`  

---

### **7️⃣ Charger un objet depuis un fichier JSON**  
📌 Fonction `load_from_json_file(filename)` qui **lit un fichier JSON et recrée l’objet Python correspondant**.  
✅ Utilisation de `json.load()`  

---

### **8️⃣ Gérer une liste d’arguments via un fichier JSON**  
📌 Script `7-add_item.py` qui :  
- Charge une liste depuis `add_item.json`  
- Ajoute **tous les arguments passés en ligne de commande**  
- Enregistre la nouvelle liste dans `add_item.json`  

✅ Utilisation de `sys.argv` pour récupérer les arguments.  

---

### **9️⃣ Classe `Student` vers JSON**  
📌 Création d’une **classe `Student`** avec :  
- **Attributs publics** : `first_name`, `last_name`, `age`  
- **Méthode `to_json()`** : Retourne un **dictionnaire** représentant l’étudiant  

💡 **Sérialisation JSON simplifiée avec `__dict__`**  

---

### **🔟 Filtrer les attributs JSON d’un `Student`**  
📌 Amélioration de `to_json(attrs=None)`, qui :  
- Retourne **tous les attributs** si `attrs=None`  
- Retourne **uniquement les attributs spécifiés** si `attrs` est une liste  

---

### **1️⃣1️⃣ Sérialisation et rechargement d’un objet `Student`**  
📌 Ajout de la méthode `reload_from_json(self, json)` pour :  
- Remplacer **tous les attributs** de l’instance à partir d’un dictionnaire JSON.  

✅ **Concept de sérialisation/désérialisation** pour **sauvegarder/recharger un objet en JSON**.  

---

### **1️⃣2️⃣ Triangle de Pascal**  
📌 Implémenter `pascal_triangle(n)`, qui **génère le triangle de Pascal** sous forme de **liste de listes**.  

Exemple avec `n = 5` :  
```python
[
 [1],
 [1, 1],
 [1, 2, 1],
 [1, 3, 3, 1],
 [1, 4, 6, 4, 1]
]
```  

💡 **Utilisation de boucles pour générer chaque ligne à partir de la précédente.**  

---

## 🛠 **Technologies utilisées**  
🔹 Python 3.8+  
🔹 JSON  
🔹 Manipulation de fichiers  

---

## ✅ **Bonnes pratiques et conseils**  
✔ **Utiliser `with open()`** : Évite d’oublier `close()` et protège contre les erreurs.  
✔ **Respecter `pycodestyle`** : Code propre et bien structuré.  
✔ **Bien documenter les fonctions et classes**.  
✔ **Utiliser `json.load()` et `json.dump()`** pour la sérialisation JSON.  
✔ **Toujours tester avec des fichiers différents pour vérifier la robustesse**.  

---

## 📂 **Structure du projet**  
```
📁 python-input_output
 ├── 0-read_file.py
 ├── 1-write_file.py
 ├── 2-append_write.py
 ├── 3-to_json_string.py
 ├── 4-from_json_string.py
 ├── 5-save_to_json_file.py
 ├── 6-load_from_json_file.py
 ├── 7-add_item.py
 ├── 8-class_to_json.py
 ├── 9-student.py
 ├── 10-student.py
 ├── 11-student.py
 ├── 12-pascal_triangle.py
 ├── tests/  # Dossier contenant les fichiers de test
 └── README.md  # Ce fichier
```

---

## 🎯 **Conclusion**  
Ce projet permet de **maîtriser la manipulation des fichiers**, la **sérialisation JSON**, et l’**accès aux arguments de ligne de commande** en Python. 🚀  

📌 **Prochaines étapes** :  
🔹 Approfondir la gestion des erreurs dans la manipulation des fichiers.  
🔹 Explorer d’autres formats comme **CSV et XML**.  
🔹 Automatiser des tâches avec **Python et JSON**.  

---

### **Auteur**  
✍ **Projet réalisé dans le cadre de Holberton School.** 🚀