# Task_Python3App

Riporto il testo del task, con alcune note:

Il task consiste nel creare lo scheletro di una singola applicazione in python 3 composta da:
- [x] almeno un un processo in grado di acquisire in modo asincrono un dato (ad esempio un post http, una connessione socket, la pressione di un tasto, etc) con un delay artificiale significativo per simulare complessità e carico ed in grado di popolare una semplice struttura dati di tipo timeserie con i dati ricevuti (timestamp e valore) (_Ho creato brevemente un backend su un mio server che risponda dopo 2 secondi di delay con un numero casuale tra [10 e 25]_)
- [x] almeno un processo/funzione in grado di elaborare la time serie in ram sommando ad esempio i valori richiamabile e schedulabile (_Il tempo di schedule e' specificabile nel costruttore della classe_)
- [x] almeno un processo in grado di esporre una sorta di API http in grado di fornire, ad esempio, la somma generata prelevandola dal dataset (_Non ricordando la nuova libreria di cui mi avevi parlato, ho utilizzato Flask. La route per la chiamata get e' a: http://127.0.0.1:4567/getSum_)

Con:
- [x] gestione della concorrenza con l'utilizzo di threads o multiprocesses (_Ho utilizzato la libreria threading di python3. Ho creato una classe che estende i Thread appositamente per la chiamata http, dato che il funzionamento asincrono della libreria requests non e' comodissimo_)
- [x] gestione delle eccezioni (_Le uniche eccezioni che mi sembravano possibili erano la pressione di ctrlC da parte dell'utente e un eventuale errore di connessione quando viene effettuata la richiesta http_)
- [x] verifica dei processi attivi ed eventuale gestione del sub process morto
- [x] gestione dello shutdown pulito dell'applicazione in caso di elaborazioni in corso in un sub processo (_Ho gestito la pressione di ctrlC da parte dell'utente, e rendendo i Thread dei "Daemon", vengono terminati quando viene terminato il padre_)

Possibilmente:
- [x] senza scrivere nulla su disco
- [x] utilizzando pandas/numpy e il loro supporto alle timeseries (_Ho utilizzado pandas con le pandas.Series()_)
- [ ] abbozzando la generazione di metriche di funzionamento per tools tipo prometheus (_Questo punto non mi era ben chiaro: ho cercato prometheus e ho circa capito cosa sia, ma non saprei come generare metriche di funzionamento per tool simili_)

Sarebbe ottimo:
- [x] se l'applicazione fosse in un repository github completa di yaml docker compose utilizzando alpine linux con virtualenv e tutto quello che ne consegue (_Non mi era ben chiaro come mai proprio alpine linux. In ogni caso, non ho mai lavorato troppo con i docker e ho dovuto informarmi_)
