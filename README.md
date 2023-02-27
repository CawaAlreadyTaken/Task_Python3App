# Task_Python3App

Riporto il testo del task, con alcune note:

Il task consiste nel creare lo scheletro di una singola applicazione in python 3 composta da:
- [x] almeno un un processo in grado di acquisire in modo asincrono un dato (ad esempio un post http, una connessione socket, la pressione di un tasto, etc) con un delay artificiale significativo per simulare complessità e carico ed in grado di popolare una semplice struttura dati di tipo timeserie con i dati ricevuti (timestamp e valore)
- [x] almeno un processo/funzione in grado di elaborare la time serie in ram sommando ad esempio i valori richiamabile e schedulabile
- [x] almeno un processo in grado di esporre una sorta di API http in grado di fornire, ad esempio, la somma generata prelevandola dal dataset

Con:
- [x] gestione della concorrenza con l'utilizzo di threads o multiprocesses
- [x] gestione delle eccezioni
- [ ] verifica dei processi attivi ed eventuale gestione del sub process morto
- [x] gestione dello shutdown pulito dell'applicazione in caso di elaborazioni in corso in un sub processo

Possibilmente:
- [x] senza scrivere nulla su disco
- [x] utilizzando pandas/numpy e il loro supporto alle timeseries
- [ ] abbozzando la generazione di metriche di funzionamento per tools tipo prometheus

Sarebbe ottimo:
- [x] se l'applicazione fosse in un repository github completa di yaml docker compose utilizzando alpine linux con virtualenv e tutto quello che ne consegue
