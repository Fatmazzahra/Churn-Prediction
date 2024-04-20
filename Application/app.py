from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import logging 

import pickle
model =pickle.load(open("Model/final_modelxgb.pkl", "rb"))


app = Flask(__name__, static_folder='static', static_url_path='/static')

logging.basicConfig(level=logging.INFO)

@app.route('/')
def hello_world():
    return render_template('prediction.html')

@app.route('/predict', methods=['POST'])
def predict():
   

    field_data_types = {
    'nb_jours_abonne': int,
    'genre': str,
    'age': int,
    'marie': str,
    'nb_appel_jour': int,
    'duree_appel_jour': float,
    'cout_appel_jour': float,
    'nb_appel_soiree': int,
    'duree_appel_soiree': float,
    'cout_appel_soiree': float,
    'nb_appel_nuit': int,
    'duree_appel_nuit': float,
    'cout_appel_nuit': float,
    'nb_appel_inter': int,
    'duree_appel_inter': float,
    'cout_appel_inter': float,
    'active_msg_vocaux': str,
    'nb_msg_vocaux': int,
    'nb_reclamation': int,
    'offer_type': str
    }

    init_features = {}
    for field, data_type in field_data_types.items():
            value = request.form.get(field)
            
            app.logger.debug("Field: %s, Value: %s", field, value)
            if value is None:
                return f"Entrée invalide pour '{field}'"
            if data_type == int:
                if value.isdigit():
                    init_features[field] = int(value)
                else:
                    return f"Entrée invalide pour '{field}'"
            elif data_type == float:
                try:
                    init_features[field] = float(value)
                except ValueError:
                    return f"Entrée invalide pour '{field}'"
            else:
             init_features[field] = value
    

    if init_features['active_msg_vocaux'] == "oui":
        init_features['active_msg_vocaux'] = 1
    else:
        init_features['active_msg_vocaux'] = 0
    
    if init_features['marie'] == "oui":
        init_features['marie'] = 1
    else:
        init_features['marie'] = 0
  

    if init_features['genre'] == "homme":
        init_features['genre'] = 0
    else:
        init_features['genre'] = 1
    
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
    offer_type = init_features['offer_type']
    if offer_type in option_map:
        init_features['offer_type'] = float(option_map[offer_type])
    else:
        raise ValueError("Offer type not found in option map.")
    
     # Make a prediction
    final_features = np.array(list(init_features.values())).reshape(1, -1)  # Convert to numpy array and reshape
    prediction = model.predict(final_features)[0]  # Access the first element of the prediction array
    
    # Determine the prediction message
    if prediction == 1:
       message = " Le client résiliera son abonnement"
    else:
       message = " Le client ne résiliera pas son abonnement"
    
    
    return render_template('prediction.html', prediction_text='Résultat de prédiction: {}'.format(message))
 



@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')                                       




if __name__ == '__main__':
    app.run(debug=True)
   




    
   
