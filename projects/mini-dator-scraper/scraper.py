#!/usr/bin/env python3
"""
Mini-Dator Scraper för Blocket
Hittar begagnade Mac Mini, Intel NUC, etc. för Klaus 24/7-setup
"""

import requests
import json
import re
import time
from datetime import datetime
from typing import List, Dict, Optional

class BlocketScraper:
    def __init__(self):
        self.base_url = "https://www.blocket.se/recommerce/forsale/search"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'sv-SE,sv;q=0.9,en;q=0.8',
        }
        self.db_file = "/Users/duljan/.openclaw/workspace/projects/mini-dator-scraper/database.json"
        
    def load_database(self) -> List[Dict]:
        """Ladda tidigare hittade annonser"""
        try:
            with open(self.db_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def save_database(self, listings: List[Dict]):
        """Spara annonser till databas"""
        with open(self.db_file, 'w') as f:
            json.dump(listings, f, indent=2, ensure_ascii=False)
    
    def search_mac_mini(self) -> List[Dict]:
        """Sök efter Mac Mini på Blocket"""
        listings = []
        
        # Sökparametrar för Mac Mini
        params = {
            'q': 'mac mini',
            'sort': 'rel',  # Relevans
        }
        
        try:
            response = requests.get(
                self.base_url, 
                params=params, 
                headers=self.headers,
                timeout=10
            )
            response.raise_for_status()
            
            # Parse HTML (Blocket använder JavaScript, så detta är en förenkling)
            # I verkligheten behöver vi antingen:
            # 1. Använda Blockets API (om det finns)
            # 2. Använda Selenium/Playwright för JS-render
            # 3. Använda en proxy-tjänst som ScraperAPI
            
            # För nu, skapa en placeholder-struktur
            print(f"Status: {response.status_code}")
            print(f"URL: {response.url}")
            
        except Exception as e:
            print(f"Fel vid sökning: {e}")
        
        return listings
    
    def calculate_score(self, listing: Dict) -> Dict:
        """
        Beräkna total poäng för en annons
        
        Returnerar dict med:
        - total_score (0-100)
        - performance_score (0-100)
        - value_score (0-100)
        - availability_score (0-100)
        - power_score (0-100)
        - motivation (str)
        """
        result = {
            'total_score': 0,
            'performance_score': 0,
            'value_score': 0,
            'availability_score': 0,
            'power_score': 0,
            'motivation': ''
        }
        
        # Prestanda-poäng
        cpu_cores = listing.get('cpu_cores', 0)
        ram_gb = listing.get('ram_gb', 0)
        storage_gb = listing.get('storage_gb', 0)
        
        # CPU (max 50p)
        if cpu_cores >= 8:
            result['performance_score'] += 50
        elif cpu_cores >= 6:
            result['performance_score'] += 40
        elif cpu_cores >= 4:
            result['performance_score'] += 25
        
        # RAM (max 40p)
        if ram_gb >= 32:
            result['performance_score'] += 40
        elif ram_gb >= 16:
            result['performance_score'] += 30
        elif ram_gb >= 8:
            result['performance_score'] += 15
        
        # Lagring (max 10p)
        if storage_gb >= 512:
            result['performance_score'] += 10
        elif storage_gb >= 256:
            result['performance_score'] += 8
        elif storage_gb >= 128:
            result['performance_score'] += 5
        
        # Strömförbrukning (max 100p)
        model = listing.get('model', '').lower()
        if 'm2' in model or 'm1' in model:
            result['power_score'] = 100  # 6-7W
        elif 'intel nuc' in model:
            result['power_score'] = 70   # 10-15W
        elif 'mac mini' in model and 'intel' in model:
            result['power_score'] = 40   # 30-40W
        else:
            result['power_score'] = 20   # Stationär: 100W+
        
        # Värde-poäng (simplifierad)
        price = listing.get('price', 0)
        if price <= 2000:
            result['value_score'] = 90
        elif price <= 3000:
            result['value_score'] = 75
        elif price <= 4000:
            result['value_score'] = 60
        elif price <= 5000:
            result['value_score'] = 45
        else:
            result['value_score'] = 30
        
        # Tillgänglighet (placeholder)
        result['availability_score'] = 80  # Antar bra tillgänglighet
        
        # Total poäng (viktat)
        result['total_score'] = (
            result['performance_score'] * 0.4 +
            result['value_score'] * 0.35 +
            result['availability_score'] * 0.15 +
            result['power_score'] * 0.10
        )
        
        # Motivering
        reasons = []
        if result['performance_score'] >= 70:
            reasons.append("💪 Hög prestanda")
        if result['value_score'] >= 70:
            reasons.append("💰 Bra värde för pengarna")
        if result['power_score'] >= 80:
            reasons.append("🔋 Låg strömförbrukning (perfekt för 24/7)")
        if price <= 3000:
            reasons.append("💸 Prisvärt")
        
        result['motivation'] = " | ".join(reasons) if reasons else "OK deal"
        
        return result
    
    def should_notify(self, listing: Dict, score: Dict) -> bool:
        """Avgör om vi ska push-notifiera"""
        # Tröskel: 75 poäng
        if score['total_score'] >= 75:
            return True
        
        # Eller om det är en exceptionell deal
        if score['value_score'] >= 85 and listing.get('price', 99999) <= 2500:
            return True
        
        return False
    
    def format_telegram_message(self, listing: Dict, score: Dict) -> str:
        """Formatera notifiering för Telegram"""
        price = listing.get('price', 0)
        title = listing.get('title', 'Okänd')
        location = listing.get('location', 'Okänd plats')
        url = listing.get('url', '')
        model = listing.get('model', 'Okänd modell')
        
        message = f"""🏆 **SUPER-DEAL HITTAD!** 🏆

**{title}**
💰 **Pris:** {price:,} kr
📍 **Plats:** {location}
💻 **Modell:** {model}

📊 **Rankning: {score['total_score']:.1f}/100**
• Prestanda: {score['performance_score']:.0f}/100
• Värde: {score['value_score']:.0f}/100  
• Ström: {score['power_score']:.0f}/100

💡 **Varför den är bra:**
{score['motivation']}

🔗 [Se annons på Blocket]({url})

⏰ Hittad: {datetime.now().strftime('%Y-%m-%d %H:%M')}
"""
        return message
    
    def run(self):
        """Huvudloop — kör var 10:e minut"""
        print(f"[{datetime.now()}] Startar Mini-Dator Scraper...")
        
        # Ladda databas
        db = self.load_database()
        existing_ids = {item.get('id') for item in db}
        
        # Sök
        listings = self.search_mac_mini()
        
        new_notifications = []
        
        for listing in listings:
            listing_id = listing.get('id')
            
            # Hoppa över om redan sett
            if listing_id in existing_ids:
                continue
            
            # Beräkna poäng
            score = self.calculate_score(listing)
            listing['score'] = score
            listing['found_at'] = datetime.now().isoformat()
            
            # Lägg till i databas
            db.append(listing)
            
            # Notifiera om bra deal
            if self.should_notify(listing, score):
                message = self.format_telegram_message(listing, score)
                new_notifications.append(message)
                print(f"🚨 NOTIFIERING: {listing.get('title')} ({score['total_score']:.1f} poäng)")
        
        # Spara databas
        self.save_database(db)
        
        print(f"[{datetime.now()}] Klar. Hittade {len(listings)} annonser, {len(new_notifications)} notifieringar.")
        
        return new_notifications


if __name__ == "__main__":
    scraper = BlocketScraper()
    notifications = scraper.run()
    
    # Skriv ut notifieringar (för test)
    for msg in notifications:
        print("\n" + "="*50)
        print(msg)
