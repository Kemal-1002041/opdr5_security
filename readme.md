# Encryptie Applicatie - Symmetrische Encryptie met Cryptography

Deze applicatie maakt gebruik van de `cryptography`-bibliotheek in Python om berichten veilig te versleutelen (encryptie) en te ontsleutelen (decryptie). Het biedt een eenvoudig te gebruiken menu waarmee gebruikers kunnen kiezen tussen het versleutelen en ontsleutelen van berichten. Deze applicatie implementeert symmetrische encryptie.

## Inhoudsopgave

- [Overzicht](#overzicht)
- [Installatie](#installatie)
- [Gebruik](#gebruik)
- [Encryptiemethode](#encryptiemethode)
- [Toekomstige uitbreidingen](#toekomstige-uitbreidingen)

## Overzicht

Deze applicatie biedt gebruikers de mogelijkheid om berichten te versleutelen en te ontsleutelen met behulp van **symmetrische encryptie**. De sleutel die hiervoor nodig is, wordt automatisch gegenereerd en opgeslagen in een bestand (`secret.key`), zodat dezelfde sleutel later kan worden gebruikt om berichten te ontsleutelen. 

De volgende functionaliteiten zijn inbegrepen:
- **Versleuteling**: Voer een bericht in en de applicatie versleutelt dit met een gegenereerde sleutel.
- **Ontsleuteling**: Voer een versleuteld bericht in en de applicatie maakt het oorspronkelijke bericht weer leesbaar.

## Installatie

Zorg ervoor dat de Python-bibliotheek `cryptography` is geïnstalleerd om het programma te laten werken.

1. Installeer de `cryptography`-bibliotheek:
   pip3 install cryptography

2.	Download of clone het project naar je lokale machine.

3.	Voer het Python-script uit:

    python3 genereer_key.py
    python3 opdr5.py

4.  In de hoofdmenu kan je kiezen wat je wilt
    --- Hoofdmenu ---
1. Versleutel een bericht
2. Ontsleutel een bericht
3. Afsluiten