Stock Price Variation Calculator
Descrizione
Questo script Python calcola la variazione percentuale tra il prezzo di apertura e il prezzo di chiusura di un'azione utilizzando i dati forniti da Alpha Vantage API. Può essere utilizzato per monitorare le fluttuazioni giornaliere dei prezzi delle azioni, ad esempio, per Tesla Inc. (TSLA).

Funzionalità
Carica la chiave API da un file .env.
Fa una richiesta all'API di Alpha Vantage per ottenere i dati di un'azione specificata (prezzo di apertura e chiusura).
Calcola la variazione percentuale tra il prezzo di apertura e il prezzo di chiusura.
Stampa il risultato in modo leggibile.
Prerequisiti
Per eseguire questo script, è necessario avere Python 3.x e alcune librerie Python installate:

requests: Per fare richieste HTTP all'API di Alpha Vantage.
python-dotenv: Per caricare la chiave API da un file .env.
Installazione delle dipendenze
Assicurati di avere un ambiente virtuale Python attivo e installa le dipendenze necessarie:

bash
Copia codice
pip install requests python-dotenv
Ottenere una chiave API da Alpha Vantage
Vai su Alpha Vantage per ottenere una chiave API gratuita.

Salva la chiave API in un file .env nella directory principale del progetto come segue:

.env

makefile
Copia codice
API_KEY=your_api_key_here
Utilizzo
Crea un file .env nella stessa directory del tuo script e aggiungi la tua chiave API:

makefile
Copia codice
API_KEY=your_api_key_here
Esegui lo script:

bash
Copia codice
python stock_price_calculator.py
Lo script stamperà il prezzo di apertura, il prezzo di chiusura e la variazione percentuale per l'azione selezionata (ad esempio, Tesla Inc. - TSLA).

Esempio di output:
yaml
Copia codice
Prezzo di apertura di ieri: 150.00
Prezzo di chiusura di ieri: 160.00
Variazione percentuale: 6.67%
