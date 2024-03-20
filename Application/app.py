from flask import Flask, render_template, jsonify,request
import pickle
import numpy as np

app = Flask(__name__)

model =pickle.load(open("Model/final_modelxgb.pkl", "rb"))

@app.route('/',methods=['GET'])
def hello_world():
    return render_template('prediction.html')

@app.route('/predict', methods=['POST'])
def predict():
    

    # Extract form data
    nb_jours_abonne_str = request.form.get('nb_jours_abonne')
    if nb_jours_abonne_str and nb_jours_abonne_str.isdigit():
        nb_jours_abonne = int(nb_jours_abonne_str)
    else: return "Entrée invalide pour 'nb_jours_abonne'"

    genre = request.form.get('genre')

    age_str = request.form.get('age')
    if age_str and age_str.isdigit():
        age = int(age_str)
    else: return "Entrée invalide pour 'age'"

    marie = request.form.get('marie')

    nb_appel_jour_str = request.form.get('nb_appel_jour')
    if nb_appel_jour_str and nb_appel_jour_str.isdigit():
        nb_appel_jour = int(nb_appel_jour_str)
    else: return "Entrée invalide pour 'nb_appel_jour'"

    duree_appel_jour_str = request.form.get('duree_appel_jour')
    if duree_appel_jour_str:
        duree_appel_jour = float(duree_appel_jour_str)
    else: return "Entrée invalide pour 'duree_appel_jour'"

    cout_appel_jour_str = request.form.get('cout_appel_jour')
    if cout_appel_jour_str:
        cout_appel_jour = float(cout_appel_jour_str)
    else: return "Entrée invalide pour 'cout_appel_jour'"

    nb_appel_soiree_str = request.form.get('nb_appel_soiree')
    if nb_appel_soiree_str:
        nb_appel_soiree = int(nb_appel_soiree_str)
    else: return "Entrée invalide pour 'nb_appel_soiree'"

    duree_appel_soiree_str = request.form.get('duree_appel_soiree')
    if duree_appel_soiree_str:
        duree_appel_soiree = float(duree_appel_soiree_str)
    else: return "Entrée invalide pour 'duree_appel_soiree'"

    cout_appel_soiree_str = request.form.get('cout_appel_soiree')
    if cout_appel_soiree_str:
         cout_appel_soiree = float(cout_appel_soiree_str)
    else: return "Entrée invalide pour 'cout_appel_soiree'"

    nb_appel_nuit_str = request.form.get('nb_appel_nuit')
    if nb_appel_nuit_str:
         nb_appel_nuit = int(nb_appel_nuit_str)
    else: return "Entrée invalide pour 'nb_appel_nuit'"

    duree_appel_nuit_str = request.form.get('duree_appel_nuit')
    if duree_appel_nuit_str:
        duree_appel_nuit = float(duree_appel_nuit_str)
    else: return "Entrée invalide pour 'duree_appel_nuit'"

    cout_appel_nuit_str = request.form.get('cout_appel_nuit')
    if cout_appel_nuit_str:
        cout_appel_nuit = float(cout_appel_nuit_str)
    else: return "Entrée invalide pour 'cout_appel_nuit'"

    nb_appel_inter_str = request.form.get('nb_appel_inter')
    if nb_appel_inter_str:
         nb_appel_inter = int(nb_appel_inter_str)
    else: return "Entrée invalide pour 'nb_appel_inter'"

    duree_appel_inter_str = request.form.get('duree_appel_inter')
    if duree_appel_inter_str:
           duree_appel_inter = float(duree_appel_inter_str)
    else: return "Entrée invalide pour 'duree_appel_inter'"

    cout_appel_inter_str = request.form.get('cout_appel_inter')
    if cout_appel_inter_str:
         cout_appel_inter = float(cout_appel_inter_str)
    else: return "Entrée invalide pour 'cout_appel_inter'"

    
    nb_msg_vocaux_str = request.form.get('nb_msg_vocaux')
    if nb_msg_vocaux_str and nb_msg_vocaux_str.isdigit():
        nb_msg_vocaux = int(nb_msg_vocaux_str)
    else: return "Entrée invalide pour 'nb_reclamation'"

    offer_type = request.form.get('offer_type')
    nb_msg_vocaux = int(request.form.get('nb_msg_vocaux'))
    nb_reclamation = int(request.form.get('nb_reclamation'))

    active_msg_vocaux = request.form.get('active_msg_vocaux')

    if active_msg_vocaux == "oui" :active_msg_vocaux = "1"
    else: active_msg_vocaux= "0"

    if marie =="oui" : marie ="1"
    else: marie = "0"

    if genre =="homme" :gnere ="0"
    else: genre ="1"

    option_map = {
    "Hayya": "0.16666666666666666",
    "PRE - 1=11":"0.13934426229508196",
    "PRE - 900 bonus": "0.12213740458015267",
    "PRE - AHLA": "0.14485981308411214",
    "PRE - Binetna": "0.11673151750972763",
    "PRE - Classic": "0.13595166163141995",
    "PRE - Club Optimum Plus": "0.14634146341463414",
    "PRE - Corporate Optimum Family": "0.16602316602316602",
    "PRE - CSS 1000% New": "0.061224489795918366",
    "PRE - CSS Mobile 1000%": "0.16326530612244897",
    "PRE - CSSM 35mil/min": "0.141176471",
    "PRE - Day Pass": "0.17370892018779344",
    "PRE - Doublé": "0.13440860215053763",
    "PRE - Double Reinstal": "0.13440860215053763",
    "PRE - E.M. 1000%": "0.094827586206896547",
    "PRE - Elissa 300%": "0.1428571428571429",
    "PRE - Employe TT": "0.0989010989010989",
    "PRE - ESS 1000% New": "0.22580645161290322",
    "PRE - ESS Mobile 35mil/min": "0.125",
    "PRE - Jawhara 35Mil": "0.05",
    "PRE - New Elissa": "0.33333333333333337",
    "PRE - offre 40": "0.25",
    "PRE - Offre WL5": "0.066666667",
    "PRE - Oulidha 1000%": "0.11627906976744186",
    "PRE - Oulidha 2000%": "0.20454545454545456",
    "PRE - Pack cle 4G": "0.13207547169811321",
    "PRE - Pass Etudiant": "0.18548387096774194",
    "PRE - Taraji Mobile 1500%": "0.11398963730569948",
    "PRE - Tawwa": "0.17410714285714285",
    "PRE - TM 35mil/min": "0.15342465753424658",
    "PRE - Touriste SIM": "0.14285714285714285",
    "PRE - Trankil ELISSA": "0.12087912087912088",
    "PRE - Trankil TT": "0.15384615384615385",
    "PRE - TT 1000%": "0.13846153846153847",
    "PRE - TT 1500%": "0",
    "PRE - TT 2000%": "0.095238095238095233",
    "PRE - TT 300%": "0.19444444444444445",
    "PRE - Vendor_RE": "0.098591549295774641",
    "SMS discount": "0.13157894736842105",
    }
    
    if offer_type in option_map: offer_type = option_map[offer_type]
    else: offer_type = "default_value"

    prediction = int(model.predict([[nb_jours_abonne,genre,age,marie,nb_appel_inter,
                                 nb_appel_jour,nb_appel_nuit,nb_appel_soiree,nb_reclamation,nb_msg_vocaux,
                                 duree_appel_inter,duree_appel_jour,duree_appel_nuit,duree_appel_soiree,cout_appel_inter,
                                 cout_appel_jour,cout_appel_nuit,cout_appel_soiree,offer_type,int(active_msg_vocaux)]]))
    
    message_resiliation="Résultat de prédiction: Le client résiliera son abonnement"
    message_non_resiliation="Résultat de prédiction: Le client ne résiliera pas son abonnement"

    if prediction == 1:
        message = message_resiliation
    else:
        message = message_non_resiliation
    

   
    return render_template('prediction.html', prediction = message)


if __name__ == '__main__':
    app.run(debug=True)
    



    
   
