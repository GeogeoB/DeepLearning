# Deep Learning Project

**Brenne Geoffrey, Coux Juliette, Debethune Celian, Gaven Loris, Zémiri Flavian**

Projet réalisé dans le cadre d'un cours de l'Enseeiht dans le but de classifier le genres d'affiches de films via du Deep Learning.

## Content

* `films.csv` 

Liste csv de 5000 films extraits de _letterboxd.com_ avec l'addon webScraper.

| web-scraper-order | web-scraper-start-url | films | films-href | title |genres | image-src | number |
| --- | --- | --- | --- | --- | --- | --- | --- | 


* `film_analyse.ipynb` 

Fichier jupyter permettant le pré-traitement du fichier films.csv. Ce fichier permet tout d'abord de choisir n (dans notre cas n=9) genres de films qui maximisent le nombre de films gardés et minimise le nombre de films qui partagent plusieurs catégories choisis, pour cela on utilise :


$$(c1,\dots,cn) = argmax \prod_{i=1}^N \dfrac{ C_i}{\sum\limits_{j=1, i \neq j}^N C_{ij}} \cdot \tilde{\mu} \cdot \tilde{m}$$

avec $C_i$ le nombre de film de genre i

$C_{ij}$ le nombre de film de genre i et j

$\tilde{\mu}$ la moyenne du nombre de film par classe qui ne sont pas contenu dans les autres classes

$\tilde{m}$ la médian du nombre de film par classe qui ne sont pas contenu dans les autres classes

**Après** avoir calculer les n genres, le fichier renvoit la liste `films_choisis.csv` des films qui ont dans leurs genres seulement un des n genres choisis.
C'est à dire que si les genres choisis sont "horreur" et "comédie", le film "ça" de genre horreur et drama est sélectionné et labélisé horreur, alors que le film Scary-movie de genre horreur et Comédie ne sera pas retenu.


* `films_choisis.csv` 

Liste des films séléctionnés et re-labelisés par `film_analyse.ipynb`

| film_id | genre | image | bdd |
| --- | --- | --- | --- |

* `download.py` 

Télécharge les affiches de film de `films_choisis.csv`  et les range dans le bon dossier de `./bdd`

* `./bdd/*`

Dossier contenant les affiches de film selectionné et trié par genre (On n'a sélectionné que un genre par film par le pré-traitement)

* `chargement_donnees.ipynb`

Script python chargeant les affiches dans 3 matrices d'entrainement, de test et de validation pour utilisation ultèrieure.

* `README.md` ce fichier
