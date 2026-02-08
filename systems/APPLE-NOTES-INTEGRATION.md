# Apple Notes Integration — Klaus System

## 📱 Så här fungerar det:

### Steg 1: Skriv på iPhone
1. Öppna **Anteckningar** (Apple Notes)
2. Skapa en ny anteckning i mappen **"Klaus Input"**
3. Skriv vad du vill att jag ska göra/komma ihåg

### Steg 2: När Mac startar
- Jag läser automatiskt alla nya anteckningar i "Klaus Input"
- Jag agerar på dem (skapar tasks, svarar, etc.)
- Jag markerar dem som "lästa" eller flyttar till "Klaus Done"

### Steg 3: Jag svarar
- Via Telegram (om du vill ha svar direkt)
- Eller lägger i en svars-mapp i Notes

---

## 🗂️ Mappstruktur:

```
Apple Notes:
├── Klaus Input       ← Du skriver här (från iPhone)
├── Klaus Done        ← Jag flyttar lästa anteckningar hit
├── Klaus Ideas       ← Jag lägger idéer/förslag här
└── [Dina andra mappar]
```

---

## ✍️ Mall för anteckningar:

```
**Datum:** 2026-02-08
**Typ:** Task / Idé / Fråga / Påminnelse

[Beskriv vad du vill]

**Prioritet:** Hög / Medium / Låg
**Deadline:** [Om det finns]
```

---

## 🔄 Synkning:

- iCloud synkar automatiskt mellan iPhone ↔ Mac
- Jag kollar "Klaus Input" vid varje uppstart
- Cron-jobb kan också kolla varje timme när Mac är på

---

*Skapad av Klaus | 2026-02-08*
