# Site de blog

Site de blog écrit avec python Flask, en suivant le tuto de la doc officielle :

<https://francoisbrucker.github.io/cours_informatique/>

## Pour l'installer

Importez le code sur votre ordinateur.

Placez dans le dossier *My_flask_web_app*, et créez un environnement python virtuel :

`python3 -m venv my-env`

Et activez-le.

Windows :

`my-env\Scripts\activate.bat`

Linux/MacOS :

`source my-env/bin/activate`

Puis, installez Flask :

`pip install Flask`

Et finalement, installez l'application :

`pip install -e .`

Vous pouvez run l'application avec la commande :

`flask --app flaskr run`