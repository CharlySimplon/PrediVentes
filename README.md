# API DATA

</div>

- [A. Prédiction des besoins de production](#production)

- [B. Répartition des tâches](#repartition)

- [C. Lecteur d'étiquette](#lecteur)

***

# A. Prédiction des besoins de production <a id="production"></a>

<img align="right" src="/img/production.jpg" width=350>

L'API va requêter la BDD d'un magasin et récupérer les informations pertinentes (ex : jour de vente, prix de vente, quantitée vendue, etc) afin de générer un dataset permettant au modèle de retourner un fichier de prédictions en besoin de production par périodes données (date de début & date de fin).

( Les prédictions en besoin de production renvoyées à l'API Back vont lui permettre de calculer les besoins en matières premières et en conditionnements. )
<br clear="right"/>



***

# B. Répartition des tâches <a id="repartition"></a>

<img align="right" src="/img/repartition.jpg" width=350>

L'API va requêter la BDD d'un magasin et récupérer les informations pertinentes (ex : temps que nécessite une tâche, niveau de compétence requis, employés, etc) afin de répartir et prioriser les tâches des employés de manière efficiente pour la semaine à venir en fonction des besoins en production.
<br clear="right"/>


***

# C. Lecteur d'étiquette <a id="lecteur"></a>

<img align="right" src="/img/lecteur.png" width=300>

L'API va récupérer la photo d'une étiquette, faire une reconnaissance optique des caractères (lettres et numéros) qui y sont inscrits et renvoyer les informations suivantes à l'API Back :

- Numéro de lot
- Date limite de consommation (DLC)
- Un booléen sur la comparaison entre la liste d'ingrédients de l'étiquette et la liste d'ingrédients attendus dans la BDD.

<br clear="right"/>


