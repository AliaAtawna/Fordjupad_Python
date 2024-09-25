# Kunskapskontroll 2 - ETL Pipeline

## Projektöversikt
Detta projekt är en ETL-pipeline som hämtar finansiell data från Alpha Vantage API, bearbetar data för att beräkna prisförändringar, och lagrar den bearbetade datan i en CSV-fil. Projektet är automatiserat med Windows Task Scheduler och inkluderar felhantering samt loggning.

## Projektstruktur
```plaintext
kunskapskontroll_2/
│
├── data/
│   └── processed_data.csv          # Bearbetad finansiell data
│
├── logs/
│   └── etl_pipeline.log            # Loggfil för pipeline-körningar
│
├── tests/
│   └── test_etl.py                 # Automatiska tester för pipelinen
│
├── extract_data.py                 # Modul för att hämta data från API
├── load_data.py                    # Modul för att spara den bearbetade datan
├── transform_data.py               # Modul för att bearbeta datan
├── main.py                         # Huvudfil som kör hela pipelinen
├── run_pipeline.bat                # Batch-fil för att köra pipelinen automatiskt
├── setup.bat                       # Batch-fil för att sätta upp miljön
├── requirements.txt                # Lista med beroenden (pandas, requests, etc.)
├── sjalvutvardering.txt            # Självutvärdering av projektet
└── README.md                       # Projektbeskrivning och struktur

## Hur man kör projektet
1. **Setup**: Kör `setup.bat` för att installera alla beroenden och aktivera den virtuella miljön.
2. **Kör pipelinen manuellt**: Kör `main.py` för att exekvera pipelinen.
3. **Automatisering**: Pipen är schemalagd via Windows Task Scheduler för att köras automatiskt vid angivna tider.
4. **Testa pipelinen**: Kör `pytest tests/test_etl.py` för att köra automatiska tester.

## Krav
- Python 3.11+
- `pandas`
- `requests`
- `pytest`
