from gtts import gTTS
import os
import struct
import speech_recognition as sr
import pyaudio
import wave
from fuzzywuzzy import process
from enum import Enum
import pvporcupine
from datetime import datetime
import requests



def meteo():
    api_key = '2e46433c4d7e9005f9fd174f963b9922'
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Montreal,ca&lang=fr&units=metric&appid=' + api_key
    reponse = requests.get(url)
    data = reponse.json()
    temperature = round(data["main"]["temp"])
    return f'Il fait {temperature} degrés celsius'



def heure():
    now = datetime.now().strftime("%H:%M")
    return f"Il est {now}."


def wikipedia(terme):
    data = None
    return f"{terme} selon wikipedia. {data}"


def coingecko(cryptomonnaie):
    data = None
    return f"Le {cryptomonnaie} est évalué à {data} dollars canadiens"


class etat_lumiere(Enum):
    off = 0
    on = 1


class AssistantVocal:
    commandes_vocales = [
        u"ouvrir la lumière du salon", u"allumer la lumière du salon",
        u"fermer la lumière du salon", u"éteindre la lumière du salon",
        u"ouvrir la lumière du hall", u"allumer la lumière du hall",
        u"fermer la lumière du hall", u"éteindre la lumière du hall",
        u"quelle heure est-il", u"il est quelle heure",
        u"quel temps ou météo fait-il", u"quelle est la température",
        u"affiche état"
    ]

    def __init__(self) -> None:
        self.name = "Blueberry"
        self.owner = " Coppélia"
        self.hotwords = ["blueberry"]
        self.say_text(f"Bonjour!{self.owner}")
        self.lum_salon = etat_lumiere.off
        self.lum_hall = etat_lumiere.off
        self.wait_hotword()

    def say_text(self, texte, file_name="speaker.wav"):
        """
        -Transforme du texte (string) en format vocal (mp3) avec l'API de Google (gtts: pip install gtts).
        -Joue le fichier audio (mpg321: http://www.mpg123.de/download/) dans PATH ou repertoire local.
        """
        print(f"{self.name}: {texte}")
        tts = gTTS(texte, lang="fr")
        tts.save(file_name)
        cmd = f"mpg321 -q {file_name}"
        os.system(f"{cmd}")

    def listen_voice(self, RECORD_SECONDS: int = 4, WAVE_OUTPUT_FILENAME: str = "micro.wav") -> str:
        # --------- SETTING PARAMS FOR OUR AUDIO FILE ------------#
        FORMAT = pyaudio.paInt16  # format of wave
        CHANNELS = 1  # no. of audio channels
        RATE = 44100  # frame rate
        CHUNK = 1024  # frames per audio sample

        # ------------------- initialization ---------------------#
        audio = pyaudio.PyAudio()  # open a new stream for microphone

        # It creates a PortAudio Stream Wrapper class object
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, input=True,
                            frames_per_buffer=CHUNK)

        # ----------------- start of recording -------------------#
        self.say_text("J'écoute")
        frames = []
        for i in range(int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)  # read audio stream from microphone
            frames.append(data)  # append audio data to frames list

        # ------------------ end of recording --------------------#
        #self.say_text("donnez moi un instant")
        stream.stop_stream()  # stop the stream object
        stream.close()  # close the stream object
        audio.terminate()  # terminate PortAudio

        # --------------- saving audio to wave -------------------#
        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()

        # -------------- translate wave to text -----------------#
        r = sr.Recognizer()
        with sr.AudioFile(WAVE_OUTPUT_FILENAME) as source:
            audio_data = r.record(source)  # listen for the data (load audio to memory)
            text = r.recognize_google(audio_data, language="fr-FR")  # recognize (convert from speech to text)
        return text

    def is_command(self, text):
        commande, score = process.extractOne(text, AssistantVocal.commandes_vocales)
        if score < 75:
            self.say_text(f"{text} n'est pas une commande valide")
        else:
            print(f"Entendu: {text}\nCommande reconnue: {commande} (score:{score})")
            # Executer/Détailler les commandes ici commande(s)"
            # Commandes(commande)
            if commande == "fermer la lumière du salon" or commande == "éteindre la lumière du salon":
                self.lum_salon = etat_lumiere.off
                self.say_text("d'accord j'éteins la lumière du salon")
                print(self.lum_salon)

            if commande == "ouvrir la lumière du salon" or commande == "allumer la lumière du salon":
                self.lum_salon = etat_lumiere.on
                self.say_text("d'accord j'ouvre la lumière du salon")
                print(self.lum_salon)

            if commande == "fermer la lumière du hall" or commande == "éteindre la lumière du hall":
                self.lum_hall = etat_lumiere.off
                print(self.lum_hall)

            if commande == "ouvrir la lumière du hall" or commande == "allumer la lumière du hall":
                self.lum_hall = etat_lumiere.on
                print(self.lum_hall)

            if commande == "quelle heure est-il" or commande == "il est quelle heure":
                self.say_text(heure())

            if commande == "quel temps ou météo fait-il" or commande == "quelle est la température":
                self.say_text(meteo())

            if commande == "affiche état":
                print(self.lum_hall)
                print(self.lum_salon)
                print(f"Lumiere Hall: {self.lum_hall}")
                print(f"Lumiere Salon: {self.lum_salon}")

    def wait_hotword(self):
        porcupine = None
        pa = None
        audio_stream = None

        try:
            porcupine = pvporcupine.create(keywords=self.hotwords)
            # print(pvporcupine.KEYWORDS) # Show all available keywords
            print(self.hotwords)
            pa = pyaudio.PyAudio()
            audio_stream = pa.open(
                rate=porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=porcupine.frame_length)

            while True:
                pcm = audio_stream.read(porcupine.frame_length)
                pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
                keyword_index = porcupine.process(pcm)
                if keyword_index >= 0:
                    reponse = self.listen_voice()
                    self.is_command(reponse)
                    print(self.hotwords)

        finally:
            if porcupine is not None:
                porcupine.delete()
            if audio_stream is not None:
                audio_stream.close()
            if pa is not None:
                pa.terminate()


if __name__ == "__main__":
    assistant = AssistantVocal()
