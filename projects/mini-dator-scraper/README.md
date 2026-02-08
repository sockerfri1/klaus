# Projekt: Mini-Dator Scraper — Klaus 24/7 Setup

## Mål
Hitta den bästa mini-datorn (Mac Mini, Intel NUC, etc.) för att köra Klaus 24/7.

## Krav på dator
- **Pris:** Max 3000-5000 kr (begagnat)
- **CPU:** Minst 4 kärnor (Intel i5/i7 eller Apple M1/M2)
- **RAM:** Minst 8 GB (helst 16 GB)
- **Lagring:** SSD (minst 128 GB)
- **Strömförbrukning:** Låg (viktigt för 24/7 drift)
- **OS:** macOS, Linux, eller Windows (som kan köra Linux)

## Ranknings-algoritm

```
Total Poäng = (Prestanda × 0.4) + (Värde × 0.35) + (Tillgänglighet × 0.15) + (Ström × 0.10)
```

### Prestanda (0-100)
- CPU-kärnor: 4+ = 25p, 6+ = 40p, 8+ = 50p
- RAM: 8GB = 15p, 16GB = 30p, 32GB+ = 40p
- SSD: 128GB = 5p, 256GB = 8p, 512GB+ = 10p

### Värde (0-100)
- Pris/Prestanda-förhållande
- Jämförelse med liknande annonser
- Nypris vs begagnatpris

### Tillgänglighet (0-100)
- Finns i Sverige
- Snabb leverans
- Säljarens rating

### Strömförbrukning (0-100)
- Mac Mini M1/M2: 100p (6-7W)
- Intel NUC: 70p (10-15W)
- Gammal Mac Mini Intel: 40p (30-40W)
- Stationär PC: 20p (100W+)

## Push-notifiering

**Tröskel:** Total poäng ≥ 75

**Notifiering innehåller:**
- 🏆 Rankning och total poäng
- 💰 Pris och plats
- 📊 Specifikationer
- 🔗 Länk till annons
- 💡 Varför den är bra (motivering)
- ⏰ Tid kvar (om auktion)

## Teknisk setup

### Källor
1. **Blocket.se** — primär källa (störst i Sverige)
2. **Tradera** — auktioner
3. **Facebook Marketplace** — om möjligt
4. **Prisjakt/Pricerunner** — jämförelsepriser

### Uppdateringsfrekvens
- **Var 10:e minut:** Scrape och analysera
- **Direkt push:** Vid poäng ≥ 75
- **Daglig sammanfattning:** Alla hittade annonser

### Filstruktur
```
projects/
└── mini-dator-scraper/
    ├── scraper.py
    ├── ranker.py
    ├── notifier.py
    ├── database.json
    └── README.md
```

---

*Projekt startat: 2026-02-08*
