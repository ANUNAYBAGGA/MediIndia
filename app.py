from flask import Flask,render_template,redirect,url_for,request
from pymongo import MongoClient
from symptoms import randomforest



app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client.med
@app.route('/',methods=['GET','POST'])
def home():
    if request.method == "POST":
        if request.form.get("signin")=="signin":
            user = request.form["email"]
            passw = request.form["password"]

            return redirect(url_for('predict'))
    return render_template('index.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=="POST":
         if request.form.get("Submit")=="Submit":
             print("YES")
             l = list("0"*132)
             for i in range(132):
                 l[i] = int(l[i])
             try:
                 option = request.form["itching"]
             except:
                 option = 0
             l[0] = option
             try:
                option = request.form["skin rash"]
             except:
                option = 0
             l[1] = option
             try:
               option = request.form["skin eruptions"]
             except:
               option = 0
             l[2] = option
             try:
                option = request.form["sneezing"]
             except:
                option = 0
             l[3] = option
             try:
                option = request.form["shivering"]
             except:
                option = 0
             l[4] = option
             try:
                option = request.form["chills"]
             except:
                option = 0
             l[5] = option

             try:
                option = request.form["joint pain"]
             except:
                option = 0
             l[6] = option
             try:
                option = request.form["stomach pain"]
             except:
                option = 0
             l[7] = option
             try:
                option = request.form["acidity"]
             except:
                option = 0
             l[8] = option
             try:
                option = request.form["ulcers on tongue"]
             except:
                option = 0
             l[9] = option
             try:
                option = request.form["muscle wasting"]
             except:
                option = 0
             l[10] = option
             try:
                option = request.form["vomitting"]
             except:
                option = 0
             l[11] = option

             try:
                option = request.form["burning micturition"]
             except:
                option = 0
             l[12] = option
             try:
                option = request.form["spotting urination"]
             except:
                option = 0
             l[13] = option
             try:
                option = request.form["fatigue"]
             except:
                option = 0
             l[14] = option
             try:
                option = request.form["weight gain"]
             except:
                option = 0
             l[15] = option
             try:
                option = request.form["anxiety"]
             except:
                option = 0
             l[16] = option
             try:
                option = request.form["cold hands and feet"]
             except:
                option = 0
             l[17] = option
             try:
                option = request.form["mood swings"]
             except:
                option = 0
             l[18] = option
             try:
                option = request.form["weight loss"]
             except:
                option = 0
             l[19] = option
             try:
                option = request.form["restlessness"]
             except:
                option = 0
             l[20] = option
             try:
                option = request.form["lethargy"]
             except:
                option = 0
             l[21] = option
             try:
                option = request.form["patches in throat"]
             except:
                option = 0
             l[22] = option
             try:
                option = request.form["irregular sugar level"]
             except:
                option = 0
             l[23] = option
             try:
                option = request.form["cough"]
             except:
                option = 0
             l[24] = option
             try:
                option = request.form["high fever"]
             except:
                option = 0
             l[25] = option
             try:
                option = request.form["sunken eyes"]
             except:
                option = 0
             l[26] = option
             try:
                option = request.form["breathlessness"]
             except:
                option = 0
             l[27] = option
             try:
                option = request.form["sweating"]
             except:
                option = 0
             l[28] = option
             try:
                option = request.form["dehydration"]
             except:
                option = 0
             l[29] = option
             try:
                option = request.form["indigestion"]
             except:
                option = 0
             l[30] = option
             try:
                option = request.form["headache"]
             except:
                option = 0
             l[31] = option
             try:
                option = request.form["yellowish skin"]
             except:
                option = 0
             l[32] = option
             try:
                option = request.form["dark urnine"]
             except:
                option = 0
             l[33] = option
             try:
                option = request.form["nausea"]
             except:
                option = 0
             l[34] = option
             try:
                option = request.form["loss of appetite"]
             except:
                option = 0
             l[35] = option
             try:
                option = request.form["pain behind eyes"]
             except:
                option = 0
             l[36] = option
             try:
                option = request.form["back pain"]
             except:
                option = 0
             l[37] = option
             try:
                option = request.form["constipation"]
             except:
                option = 0
             l[38] = option
             try:
                option = request.form["abdominal pain"]
             except:
                option = 0
             l[39] = option
             try:
                option = request.form["diarrhoea"]
             except:
                option = 0
             l[40] = option
             try:
                option = request.form["mild fever"]
             except:
                option = 0
             l[41] = option
             try:
                option = request.form["yellow urine"]
             except:
                option = 0
             l[42] = option
             try:
                option = request.form["yellowing of eyes"]
             except:
                option = 0
             l[43] = option
             try:
                option = request.form["acute liver failure"]
             except:
                option = 0
             l[44] = option
             try:
                option = request.form["fluid overload"]
             except:
                option = 0
             l[45] = option
             try:
                option = request.form["swelling of stomach"]
             except:
                option = 0
             l[46] = option
             try:
                option = request.form["swelled lymph nodes"]
             except:
                option = 0
             l[47] = option
             try:
                option = request.form["malaise"]
             except:
                option = 0
             l[48] = option
             try:
                option = request.form["blurred and distorted vision"]
             except:
                option = 0
             l[49] = option
             try:
                option = request.form["phlegm"]
             except:
                option = 0
             l[50] = option
             try:
                option = request.form["throat irritation"]
             except:
                option = 0
             l[51] = option
             try:
                option = request.form["redness of eyes"]
             except:
                option = 0
             l[52] = option
             try:
                option = request.form["sinus pressure "]
             except:
                option = 0
             l[53] = option
             try:
                option = request.form["runny nose"]
             except:
                option = 0
             l[54] = option
             try:
                option = request.form["congestion"]
             except:
                option = 0
             l[55] = option
             try:
                option = request.form["chest pain"]
             except:
                option = 0
             l[56] = option
             try:
                option = request.form["weakness in limbs"]
             except:
                option = 0
             l[57] = option
             try:
                option = request.form["fast heart rate"]
             except:
                option = 0
             l[58] = option
             try:
                option = request.form["pain during bowel movements"]
             except:
                option = 0
             l[59] = option
             try:
                option = request.form["pain in anal region"]
             except:
                option = 0
             l[60] = option
             try:
                option = request.form["blood in stool"]
             except:
                option = 0
             l[61] = option
             try:
                option = request.form["irritation in anus"]
             except:
                option = 0
             l[62] = option
             try:
                option = request.form["neck pain"]
             except:
                option = 0
             l[63] = option
             try:
                option = request.form["dizziness"]
             except:
                option = 0
             l[64] = option
             try:
                option = request.form["cramps"]
             except:
                option = 0
             l[65] = option
             try:
                option = request.form["bruising"]
             except:
                option = 0
             l[66] = option
             try:
                option = request.form["obesity"]
             except:
                option = 0
             l[67] = option
             try:
                option = request.form["swollen legs"]
             except:
                option = 0
             l[68] = option
             try:
                option = request.form["swollen blood vessels"]
             except:
                option = 0
             l[69] = option
             try:
                option = request.form["puffy face and eyes"]
             except:
                option = 0
             l[70] = option
             try:
                option = request.form["enlarged thyroid"]
             except:
                option = 0
             l[71] = option
             try:
                option = request.form["brittle nails"]
             except:
                option = 0
             l[72] = option
             try:
                option = request.form["swollen extremeties"]
             except:
                option = 0
             l[73] = option
             try:
                option = request.form["excessive hunger"]
             except:
                option = 0
             l[74] = option
             try:
                option = request.form["extra marital contacts"]
             except:
                option = 0
             l[75] = option
             try:
                option = request.form["drying and tingling lips"]
             except:
                option = 0
             l[76] = option
             try:
                option = request.form["slurred speech"]
             except:
                option = 0
             l[77] = option
             try:
                option = request.form["knee pain"]
             except:
                option = 0
             l[78] = option
             try:
                option = request.form["hip joint pain"]
             except:
                option = 0
             l[79] = option
             try:
                option = request.form["muscle weekness"]
             except:
                option = 0
             l[80] = option
             try:
                option = request.form["stiff neck"]
             except:
                option = 0
             l[81] = option
             try:
                option = request.form["swelling joints"]
             except:
                option = 0
             l[82] = option
             try:
                option = request.form["movement stiffness"]
             except:
                option = 0
             l[83] = option
             try:
                option = request.form["spinning movements"]
             except:
                option = 0
             l[84] = option
             try:
                option = request.form["loss of balance"]
             except:
                option = 0
             l[85] = option
             try:
                option = request.form["unsteadiness"]
             except:
                option = 0
             l[86] = option
             try:
                option = request.form["weakness of one body side"]
             except:
                option = 0
             l[87] = option
             try:
                option = request.form["loss of smell"]
             except:
                option = 0
             l[88] = option
             try:
                option = request.form["bladder discomfort"]
             except:
                option = 0
             l[89] = option
             try:
                option = request.form["foul smell of urine"]
             except:
                option = 0
             l[90] = option
             try:
                option = request.form["continuous feel of urine"]
             except:
                option = 0
             l[91] = option
             try:
                option = request.form["passage of gases"]
             except:
                option = 0
             l[92] = option
             try:
                option = request.form["internal itching"]
             except:
                option = 0
             l[93] = option
             try:
                option = request.form["toxic look"]
             except:
                option = 0
             l[94] = option
             try:
                option = request.form["depression"]
             except:
                option = 0
             l[95] = option
             try:
                option = request.form["irritability"]
             except:
                option = 0
             l[96] = option
             try:
                option = request.form["muscle pain"]
             except:
                option = 0
             l[97] = option
             try:
                option = request.form["altered sensorium"]
             except:
                option = 0
             l[98] = option
             try:
                option = request.form["red spots over body"]
             except:
                option = 0
             l[99] = option
             try:
                option = request.form["belly pain"]
             except:
                option = 0
             l[100] = option
             try:
                option = request.form["abnormal menstruation"]
             except:
                option = 0
             l[101] = option
             try:
                option = request.form["dischromic patches"]
             except:
                option = 0
             l[102] = option
             try:
                option = request.form["watering from eyes"]
             except:
                option = 0
             l[103] = option
             try:
                option = request.form["increased appetite"]
             except:
                option = 0
             l[104] = option
             try:
                option = request.form["polyuria"]
             except:
                option = 0
             l[105] = option
             try:
                option = request.form["family history"]
             except:
                option = 0
             l[106] = option
             try:
                option = request.form["mucoid sputum"]
             except:
                option = 0
             l[107] = option
             try:
                option = request.form["rusty sputum"]
             except:
                option = 0
             l[108] = option
             try:
                option = request.form["lack of concentration"]
             except:
                option = 0
             l[109] = option
             try:
                option = request.form["visual disturbances"]
             except:
                option = 0
             l[110] = option
             try:
                option = request.form["recieving blood transfusion"]
             except:
                option = 0
             l[111] = option
             try:
                option = request.form["receiving unsterile injections"]
             except:
                option = 0
             l[112] = option
             try:
                option = request.form["coma"]
             except:
                option = 0
             l[113] = option
             try:
                option = request.form["stomach bleeding"]
             except:
                option = 0
             l[114] = option
             try:
                option = request.form["distention of abdomen"]
             except:
                option = 0
             l[115] = option
             try:
                option = request.form["Alcoholic hepatitis"]
             except:
                option = 0
             l[116] = option
             try:
                option = request.form["fluid overload"]
             except:
                option = 0
             l[117] = option
             try:
                option = request.form["blood in sputum"]
             except:
                option = 0
             l[118] = option
             try:
                option = request.form["prominent veins on calf"]
             except:
                option = 0
             l[119] = option
             try:
                option = request.form["palpitations"]
             except:
                option = 0
             l[120] = option
             try:
                option = request.form["painful walking"]
             except:
                option = 0
             l[121] = option
             try:
                option = request.form["pus filled pimples"]
             except:
                option = 0
             l[122] = option
             try:
                option = request.form["blackheads"]
             except:
                option = 0
             l[123] = option
             try:
                option = request.form["scurring"]
             except:
                option = 0
             l[124] = option
             try:
                option = request.form["skin peeling"]
             except:
                option = 0
             l[125] = option
             try:
                option = request.form["silver like dusting"]
             except:
                option = 0
             l[126] = option
             try:
                option = request.form["small dents in nails"]
             except:
                option = 0
             l[127] = option
             try:
                option = request.form["inflammatory nails"]
             except:
                option = 0
             l[128] = option
             try:
                option = request.form["blister"]
             except:
                option = 0
             l[129] = option
             try:
                option = request.form["red sore arround nose"]
             except:
                option = 0
             l[130] = option
             try:
                option = request.form["yellow crust ooze"]
             except:
                option = 0
             l[131] = option
             global data
             data = randomforest(l)
             print(data)
             return redirect(url_for('diagnosis'))







    return render_template('symptom.html')
@app.route('/diagnosis',methods=['GET','POST'])
def diagnosis():
    if data[0] == "Fungal infection":
        remedy = 'Cipla FourDerm Anti-fungal Cream and Clocip Anti-Bacterial & Anti-Fungal Clotrimazol Powder'
    if data[0] == "Allergy":
        remedy = 'Claritin, Zyrtec and Alavert, Allegra'
    if data[0] == "GERD":
        remedy = 'Antacids , Oral suspension medicines. , Anti-gas, anti-flatulence.'
    if data[0] == "Chronic cholestasis":
        remedy = 'Ursodeoxycholic acid (UDCA)'
    if data[0] == "Drug Reaction":
        remedy = 'Stop Taking the Drug that Triggered the Reaction , Use cool compresses on the area or have the person take cool showers.'
    if data[0] == "Peptic ulcer disease":
        remedy = 'Antibiotic medications to kill H. pylori-  clarithromycin (Biaxin) Medications that block acid production and promote healing-  lansoprazole (Prevacid) Medications to reduce acid production-  cimetidine (Tagamet HB) Medications that protect the lining of your stomach and small intestine-  sucralfate (Carafate)'
    if data[0] == "AIDS":
        remedy = 'Atripla Complera Genvoya'
    if data[0] == "Diabetes":
        remedy = 'acarbose (Precose) miglitol (Glyset)'
    if data[0] == "Gastroenteritis":
        remedy = 'metronidazole (Flagyl)'
    if data[0] == "Bronchial Asthma":
        remedy = 'Inhaler containing Flovent (fluticasone) OR Pulmicort (budesonide)'
    if data[0] == "Hypertension":
        remedy = 'enalapril (Vasotec) captopril (Capoten) lisinopril (Zestril and Prinivil)'
    if data[0] == "Migraine":
        remedy = 'Advil, Motrin'
    if data[0] == "Cervical spondylosis":
        remedy = 'Self-care , Warm compress, Ice packs, and Physical exercise'
    if data[0] == "Paralysis (brain hemorrhage)":
        remedy = 'heat, massage, and exercise to stimulate nerves and muscles'
    if data[0] == "Tuberculosis":
        remedy = 'Isoniazid (H/Inh) Rifampicin (R/Rif) (In the United States rifampicin is called rifampin) Pyrazinamide (Z/Pza)'
    if data[0] == "Common Cold":
        remedy = 'Benadryl Advil D-cold'
    if data[0] == "Piles":
        remedy = 'Proctosol-HC		Anucort-HC	Hydrocortisone'
    if data[0] == "Heart Attack":
        remedy = 'Aspirin Warfarin'
    if data[0] == "Hypothyroidism":
        remedy = 'levothyroxine    Synthroid		Armour Thyroid'
    if data[0] == "Varicose Veins":
        remedy = 'polidocanol  Sotradecol  Asclera'
    if data[0] == "Hypoglycemia":
        remedy = 'glucagon	GlucaGen	Proglycem'
    if data[0] == "Osteoarthristis":
        remedy = 'Acetaminophen (Tylenol)   Duloxetine (Cymbalta)    Ibuprofen (Advil, Motrin, Midol, Nuprin)'
    if data[0] == "Rheumatoid Arthritis":
        remedy = 'methotrexate  Celebrex'
    if data[0] == "Paroymsal Positional Vertigo":
        remedy = 'meclizine Antivert'
    if data[0] == "Acne":
        remedy = 'doxycycline'
    if data[0] == "Acne":
        remedy = 'doxycycline'
    if data[0] == "Urinary tract infection":
        remedy = 'ciprofloxacin  Cipro'
    if data[0] == "Psoriasis":
        remedy = 'clobetasol  Humira  '
    if data[0] == "Impetigo":
        remedy = 'Altabax  Ceftin'
    if data[0] == "Typhoid":
        remedy = 'Cipro  ceftriaxone'
    if data[0] == "hepatitis A":
        remedy = 'immune globulin intramuscular'
    if data[0] == "Hepatitis B":
        remedy = 'entecavir  Baraclude'
    if data[0] == "Hepatitis C":
        remedy = ' Harvoni   Sovaldi   ribavirin'
    if data[0] == "Jaundice":
        remedy = 'Luminal phenobarbital'
    if data[0] == "Malaria":
        remedy = 'artemether / lumefantrine  Coartem  Malarone'
    if data[0] == "Chicken pox":
        remedy = 'Tylenol (acetaminophen), which is available to purchase online, may help with symptoms of high temperature and pain. It is important to follow the instructions provided by the manufacturer. Aspirin containing products should NOT be used for chickenpox as this can lead to complications. Acetaminophen (Tylenol) can be used at any time during pregnancy.Avoiding dehydration: It is important to drink plenty of fluids, preferably water, to prevent dehydration. Some doctors recommend sugar-free popsicles or Pedialyte for children who are not drinking enough.'
    if data[0] == "Dengue":
        remedy = 'acetaminophen'







    return render_template('symptomResult.html',disease = data[0],remedy = remedy)




if __name__=='__main__':
    task = 0
    app.debug = True
    app.run(host = '0.0.0.0',port=5005)
