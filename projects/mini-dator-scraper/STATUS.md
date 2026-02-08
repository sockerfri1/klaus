# Mini-Dator Scraper — Projektstatus

## ✅ KLART

### Komponenter
- [x] `scraper.py` — Huvudscraper för Blocket
- [x] `demo.py` — Demo med exempel-data
- [x] `README.md` — Dokumentation
- [x] Ranknings-algoritm (prestanda, värde, ström, tillgänglighet)
- [x] Telegram-notifiering (tröskel ≥75 poäng)
- [x] Cron-jobb (var 10:e minut)

### Ranknings-kriterier
| Faktor | Vikt | Max poäng |
|--------|------|-----------|
| Prestanda (CPU/RAM/SSD) | 40% | 100 |
| Värde (pris/kvalitet) | 35% | 100 |
| Tillgänglighet | 15% | 100 |
| Strömförbrukning | 10% | 100 |

### Prioriterade datorer
1. **Mac Mini M1/M2** — 100p ström (6-7W), tyst, snabb
2. **Intel NUC** — 70p ström (10-15W), kompakt, bra pris
3. **Mac Mini Intel** — 40p ström (30-40W), äldre men stabil

## ⚠️ VIKTIGT — Blocket-blockering

Blocket använder **JavaScript** för att ladda annonser. Direkt HTTP-requests ger inte riktiga annonser.

### Lösningar:
1. **Selenium/Playwright** — Automatiserad browser (kräver GUI)
2. **Blocket API** — Om det finns officiellt API
3. **ScraperAPI/ScrapingBee** — Betaltjänst som hanterar JS
4. **Browser automation via OpenClaw** — Använda browser-verktyget

### Rekommendation:
Använd **OpenClaw browser** när det är tillgängligt, eller sätta upp en **ScraperAPI**-nyckel (~$49/månad för 100k requests).

## 🔄 Cron-jobb
- **ID:** b52f7466-1191-49bd-bf5b-d42ce3d500dd
- **Frekvens:** Var 10:e minut
- **Status:** Aktiv

## 📱 Demo-resultat

Exempel på notifiering för Mac Mini M1:
```
🏆 SUPER-DEAL HITTAD! 🏆

Mac Mini M1 8GB RAM 256GB SSD
💰 Pris: 3,500 kr
📍 Plats: Stockholm
💻 Modell: Mac Mini M1 (2020)

📊 Rankning: 82.5/100
• Prestanda: 73/100
• Värde: 60/100  
• Ström: 100/100

💡 Varför den är bra:
💪 Hög prestanda | 🔋 Låg strömförbrukning

🔗 [Se annons på Blocket](...)
```

## 📝 Nästa steg

1. [ ] Fixa Blocket-scraping (Selenium/API/ScraperAPI)
2. [ ] Testa med riktiga annonser
3. [ ] Justera ranknings-algoritm baserat på resultat
4. [ ] Lägg till fler källor (Tradera, Facebook Marketplace)
5. [ ] Skapa webb-dashboard för att se alla hittade deals

---

*Projekt startat: 2026-02-08*
