# Stock Price Variation Calculator

## Descrizione
Questo script Python calcola la **variazione percentuale** tra il prezzo di apertura e il prezzo di chiusura di un'azione utilizzando i dati forniti da **Alpha Vantage API**. Può essere utilizzato per monitorare le fluttuazioni giornaliere dei prezzi delle azioni, ad esempio, per Tesla Inc. (TSLA).

## Funzionalità
- Carica la chiave API da un file `.env`.
- Fa una richiesta all'API di Alpha Vantage per ottenere i dati di un'azione specificata (prezzo di apertura e chiusura).
- Calcola la variazione percentuale tra il prezzo di apertura e il prezzo di chiusura.
- Stampa il risultato in modo leggibile.

## Prerequisiti
Per eseguire questo script, è necessario avere Python 3.x e alcune librerie Python installate:

- `requests`: Per fare richieste HTTP all'API di Alpha Vantage.
- `python-dotenv`: Per caricare la chiave API da un file `.env`.

### Installazione delle dipendenze
Assicurati di avere un ambiente virtuale Python attivo e installa le dipendenze necessarie:

```bash
pip install requests python-dotenv
