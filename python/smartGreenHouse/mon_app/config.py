from database import Database
#import secrets



USERNAME = "Copp"
PASSWORD = "abc"
WEBSERVER_URL = "http://127.0.0.1:5000"
DATABASE_URI =  "mongodb://localhost:27017/"
USB_PORTS = ["/dev/ttyACM0", "COM3", "COM4"]
PLANTES = ["Persil", "Basilique", "Tomates", "Concombres"]

user = {'user': USERNAME,
        'passwd': PASSWORD,
        'webserver': WEBSERVER_URL,
        'database_uri':  DATABASE_URI,
        'ports': USB_PORTS,
        'plantes': PLANTES,
        "auto_humidité": {"auto": [0, 0, 0, 0], "minimum": [15, 15, 55, 55], "duree": [15, 15, 55, 55]},
        "auto_journalier": {"auto": [0, 0, 0, 0], "debut": [7.5, 7.5, 7.5, 7.5], "duree": [10, 10, 55, 55]}
        }



# db = Database("mongodb://localhost:27017/")
# db.user_data.drop()
# db.add_user(user)
