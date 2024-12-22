from flask import Flask, render_template
from ..app import app 
import requests


@app.route("/retrieve_wikidata/<id>")
def retrieve_wikidata(id):
    wikidata_url = "https://www.wikidata.org/w/api.php"

    #parametres
    params = {
       'action':'wbgetentities',
       'ids':id,
       'format':'json'}
    
    try:
        #requete
        response = requests.get(wikidata_url, params=params)
        response.raise_for_status()

        #lire donnees
        data = response.json()

        #metadonnees
        content_type = response.headers.get('Content-Type','unknown')
        status_code = response.status_code

            #vérifier valeurs -> entities = clé de ce qui est renvoyé par l'API
        if 'entities' in data and id in data['entities']:
            entity_data = data['entities'][id]
            error_message = None
            
            #erreur si pb avec l'identifiant tapé dans la barre de recherche
        else: 
            entity_data = None
            error_message = f"Aucune donnée trouvée pour l'identifiant {id}"
    
        return render_template('wikidata.html',
                            content_type = content_type,
                            id = id,
                            status_code = status_code,
                            entity_data = entity_data,
                            error_message = error_message)
    
    except requests.RequestException:
        return render_template('wikidata.html',
                               error_message = "Erreur")
