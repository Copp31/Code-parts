from flask import Flask, render_template, request, make_response, redirect

from arduino import Arduino
from database import Database
from config import *

app = Flask(__name__)

try:
    ard = Arduino("COM3")
except Exception as e:
    try:
        ard = Arduino("/dev/ttyACM0")
        print("Couldn't connect with 'COM3', trying with '/dev/ttyACM0'")
    except Exception as ee:
        print(e)
        print(ee)
        print("Couldn't connect to Serial port")
        import sys
        sys.exit()

try:
    db = Database("mongodb://localhost:27017/")

except Exception as e:
    print("Error with Database communication")


@app.route("/")
def index():
    ard_data = ard.data
    print('ard_data', ard_data)
    user_data = db.read_user({})
    plante1 = user_data['plantes'][0]
    plante2 = user_data['plantes'][1]
    plante3 = user_data['plantes'][2]
    plante4 = user_data['plantes'][3]
    humidite1 = ard_data["humidite"][0]
    humidite2 = ard_data["humidite"][1]
    humidite3 = ard_data["humidite"][2]
    humidite4 = ard_data["humidite"][3]
    return render_template("index.html",
                           plante1 = plante1,
                           plante2 = plante2,
                           plante3 = plante3,
                           plante4 = plante4,
                           humidite1 = humidite1,
                           humidite2 = humidite2,
                           humidite3 = humidite3,
                           humidite4 = humidite4)

@app.route("/plante/<id>", methods=["GET", "POST"])
def plante(id):
    try:
        user_data = db.read_user({})
        nom = user_data["plantes"][int(id) - 1]

        modes_auto = user_data['auto_journalier']['auto']

        # print('user_data')

    except:
        nom = f"Plante {id}"

    if request.method == "POST":
        document = user_data['auto_journalier']

        etat = request.form['etat']
        if etat == "Activer Auto":
            modes_auto[int(id)-1] = 1
            document['auto'] = modes_auto
            print(document)
            db.update_user({}, {"auto_journalier": document})
        else:
            modes_auto[int(id) - 1] = 0
            document['auto'] = modes_auto
            print(document)
            db.update_user({}, {"auto_journalier": document})




        # db.update_user({},updated_document)
        return redirect("#")

    elif request.method == "GET":
        temperature = 0
        humidite = 0
        etat_pompe = 0

        try:
            db_data = db.read_data({}, 1500)

            # ard_state = ard.state
            # temperature = ard_state["sensors"][4]
            # humidite = ard_state["sensors"][int(id)-1]
            # etat_pompe = ard_state["pompes"][int(id)-1]

            ard_data = ard.data
            temperature = ard_data["temperature"]
            humidite = ard_data["humidite"][int(id) - 1]
            etat_pompe = ard_data["pompes"][int(id) - 1]


        except Exception as e:
            print("erreur", e)



        return render_template("plante.html",
                               user_data = user_data,
                               nom = nom,
                               id = int(id),
                               humidite = humidite,
                               temperature = temperature,
                               etat_pompe = etat_pompe,
                               db_data = db_data
                               )

@app.route("/historique")
def historique():
    arduino_data = db.read_data({},24)
    return render_template("historique.html", arduino_data=arduino_data)


@app.route("/configurations", methods=["GET", "POST"])
def configurations():
    if request.method == "POST":
        print("tyea")
        print(request)
        print(request.form)
        updated_document = {"plantes": [request.form["plante1"],
                                         request.form["plante2"],
                                         request.form["plante3"],
                                         request.form["plante4"]],
                            "auto_journalier": {'debut': [request.form["plante1-heure"],
                                                          request.form["plante2-heure"],
                                                          request.form["plante3-heure"],
                                                          request.form["plante4-heure"]],
                                                'duree': [request.form["plante1-duree"],
                                                          request.form["plante2-duree"],
                                                          request.form["plante3-duree"],
                                                          request.form["plante4-duree"]]
                                                }
                            }



        print(updated_document)

        db.update_user({},updated_document)


        return redirect("/")
    elif request.method == "GET":
        user_data = db.read_user({})
        print(user_data)
        return render_template("configuration.html",
                               user_data=user_data)




@app.route("/arduino/state")
def arduino_state():
    return ard.state

@app.route("/arduino/data")
def arduino_data():
    return ard.data

@app.route("/arduino/cmd/<cmd>")
def arduino_switch_pump(cmd:str):
    id:int = int(cmd[0])
    try:
        ard.set_cmd(cmd)
        if id < 5:
            # time.sleep(1.5)
            return redirect(WEBSERVER_URL + f"/plante/{id}")
        else:
            return redirect(WEBSERVER_URL)
    except:
        return make_response("Didn't work correctly!", 200)


@app.route("/arduino/state")
def arduino():
    return ard.state

if __name__ == "__main__":
    from threading import Thread
    import time, datetime

    def database_update_function():

        while True:
            data = ard.data
            data["date"] = datetime.datetime.now()
            db.add_data(data)
            time.sleep(60)


    database_update_thread = Thread(target=database_update_function)

    ard.run()
    database_update_thread.start()
    app.run()
    print("fin")