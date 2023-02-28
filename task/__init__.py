from flask import Flask
import pandas as pd
from threading import Thread
from time import sleep
from sys import stderr
import requests
import signal

app = Flask(__name__)

dataReceivedNumber = 0

def handler(signum, frame):
    msg = f"[*] Ctrl-c was pressed. Total number of data received: {dataReceivedNumber}"
    print(msg)
    exit(0)

class MakeRequest(Thread):
    def __init__(self, dataManager):
        super().__init__()
        self.dataManager = dataManager

    def updateData(self, integerData):
        newTimeSeries = pd.Series([integerData], index=[pd.Timestamp.now()]) # Creo una nuova pd.Series che sara' da concatenare
        self.dataManager.updateData(newTimeSeries)

    def getData(self):
        try:
            # Questa richiesta otterra' (dopo 2 secondi di sleep) un randint tra [10 e 25)
            response = requests.get("https://task.cawa.dev/")
        except requests.exceptions.ConnectionError:
            print("[!] Connection error: can't retrieve data.", file=stderr)
            return
        if response.status_code == 200:
            global dataReceivedNumber
            dataReceivedNumber+=1
            self.updateData(int(response.text))
            print(f"[*] Data acquired correctly. Data length: {len(response.content)}") # Response.content ritorna i bytes
        else:
            print(f"[!] Error in data acquisition. Status code: {response.status_code}", file=stderr)

    def run(self):
        self.getData()


class DataGetter(Thread):
    def __init__(self, sleepingTime, dataManager):
        super().__init__()
        self.scheduledSleepingTime = sleepingTime
        self.dataManager = dataManager

    def run(self):
        while True:
            makeRequest = MakeRequest(dataManager)
            makeRequest.start()
            sleep(self.scheduledSleepingTime)

class DataManager(Thread):
    def __init__(self, sleepingTime, dataObject):
        super().__init__()
        self.scheduledSleepingTime = sleepingTime
        self.data = dataObject
        self.sum = 0

    def updateData(self, data):
        self.data = pd.concat([self.data, data]) # Usiamo concat dato che append e' deprecato

    def calculateSum(self):
        self.sum = self.data.sum()

    def run(self):
        while True:
            self.calculateSum()
            sleep(self.scheduledSleepingTime)

def runApp():
    app.run(port=5000)

@app.route('/getSum')
def getSum():
    global dataManager
    dataManager.calculateSum()  # Vogliamo avere i dati piu' recenti, quando vengono richiesti
    return str(dataManager.sum)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, handler)
    data = pd.Series([],dtype=pd.Int32Dtype()) # crea una pandas.Series vuota
    dataManager = DataManager(10, data)
    dataGetter = DataGetter(5, dataManager)
    flaskManager = Thread(target=runApp)

    # Queste tre righe assicurano che il sistema possa essere terminato con ctrlC senza alcun processo zombie
    dataGetter.daemon = True
    dataManager.daemon = True
    flaskManager.daemon = True

    dataGetter.start()
    dataManager.start()
    flaskManager.start()
    while True:
        dgAlive = dataGetter.is_alive()
        dmAlive = dataManager.is_alive()
        fmAlive = flaskManager.is_alive()
        if not dgAlive:
            print("[!] Data getter thread is dead!", file=stderr)
        if not dmAlive:
            print("[!] Data manager thread is dead!", file=stderr)
        if not fmAlive:
            print("[!] Flask manager thread is dead!", file=stderr)
        if not (dgAlive or dmAlive or fmAlive):
            print("[!] All threads are dead. Quitting program...", file=stderr)
            exit(0)
        sleep(1) # Ogni secondo, il padre controlla che i figli siano ancora in esecuzione

