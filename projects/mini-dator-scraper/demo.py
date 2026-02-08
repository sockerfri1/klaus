#!/usr/bin/env python3
"""
Demo/test av Mini-Dator Scraper
Visar hur systemet fungerar med exempel-data
"""

import json
from datetime import datetime

# Exempel-annonser (som vi skulle hitta på Blocket)
sample_listings = [
    {
        "id": "blocket_12345",
        "title": "Mac Mini M1 8GB RAM 256GB SSD",
        "price": 2500,
        "location": "Stockholm",
        "model": "Mac Mini M1 (2020)",
        "cpu_cores": 8,
        "ram_gb": 8,
        "storage_gb": 256,
        "url": "https://www.blocket.se/annons/12345",
        "seller_rating": 4.8
    },
    {
        "id": "blocket_12346", 
        "title": "Intel NUC i5 16GB RAM 512GB SSD",
        "price": 2800,
        "location": "Göteborg",
        "model": "Intel NUC 10i5",
        "cpu_cores": 4,
        "ram_gb": 16,
        "storage_gb": 512,
        "url": "https://www.blocket.se/annons/12346",
        "seller_rating": 4.5
    },
    {
        "id": "blocket_12347",
        "title": "Mac Mini Intel i7 32GB RAM 1TB SSD",
        "price": 4500,
        "location": "Malmö",
        "model": "Mac Mini Intel (2018)",
        "cpu_cores": 6,
        "ram_gb": 32,
        "storage_gb": 1000,
        "url": "https://www.blocket.se/annons/12347",
        "seller_rating": 4.9
    },
    {
        "id": "blocket_12348",
        "title": "Gammal stationär PC",
        "price": 1500,
        "location": "Uppsala",
        "model": "HP Desktop i3",
        "cpu_cores": 2,
        "ram_gb": 4,
        "storage_gb": 128,
        "url": "https://www.blocket.se/annons/12348",
        "seller_rating": 3.5
    }
]

def calculate_score(listing):
    """Beräkna poäng (samma som i scraper.py)"""
    result = {
        'total_score': 0,
        'performance_score': 0,
        'value_score': 0,
        'availability_score': 80,
        'power_score': 0,
        'motivation': ''
    }
    
    cpu_cores = listing.get('cpu_cores', 0)
    ram_gb = listing.get('ram_gb', 0)
    storage_gb = listing.get('storage_gb', 0)
    price = listing.get('price', 0)
    model = listing.get('model', '').lower()
    
    # CPU
    if cpu_cores >= 8:
        result['performance_score'] += 50
    elif cpu_cores >= 6:
        result['performance_score'] += 40
    elif cpu_cores >= 4:
        result['performance_score'] += 25
    
    # RAM
    if ram_gb >= 32:
        result['performance_score'] += 40
    elif ram_gb >= 16:
        result['performance_score'] += 30
    elif ram_gb >= 8:
        result['performance_score'] += 15
    
    # Lagring
    if storage_gb >= 512:
        result['performance_score'] += 10
    elif storage_gb >= 256:
        result['performance_score'] += 8
    elif storage_gb >= 128:
        result['performance_score'] += 5
    
    # Ström
    if 'm2' in model or 'm1' in model:
        result['power_score'] = 100
    elif 'intel nuc' in model:
        result['power_score'] = 70
    elif 'mac mini' in model and 'intel' in model:
        result['power_score'] = 40
    else:
        result['power_score'] = 20
    
    # Värde
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
    
    # Total
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
        reasons.append("💰 Bra värde")
    if result['power_score'] >= 80:
        reasons.append("🔋 Låg strömförbrukning")
    if price <= 3000:
        reasons.append("💸 Prisvärt")
    
    result['motivation'] = " | ".join(reasons) if reasons else "OK deal"
    
    return result

def format_telegram_message(listing, score):
    """Formatera notifiering"""
    return f"""🏆 **SUPER-DEAL HITTAD!** 🏆

**{listing['title']}**
💰 **Pris:** {listing['price']:,} kr
📍 **Plats:** {listing['location']}
💻 **Modell:** {listing['model']}

📊 **Rankning: {score['total_score']:.1f}/100**
• Prestanda: {score['performance_score']:.0f}/100
• Värde: {score['value_score']:.0f}/100  
• Ström: {score['power_score']:.0f}/100

💡 **Varför den är bra:**
{score['motivation']}

🔗 [Se annons på Blocket]({listing['url']})

⏰ Hittad: {datetime.now().strftime('%Y-%m-%d %H:%M')}
"""

def main():
    print("="*60)
    print("🖥️  MINI-DATOR SCRAPER — DEMO")
    print("="*60)
    print()
    
    print("Söker efter lämpliga datorer för Klaus 24/7-setup...")
    print(f"Tid: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    notifications = []
    
    for listing in sample_listings:
        score = calculate_score(listing)
        
        print(f"📦 {listing['title']}")
        print(f"   💰 {listing['price']:,} kr | 📍 {listing['location']}")
        print(f"   📊 Total poäng: {score['total_score']:.1f}/100")
        print(f"   💡 {score['motivation']}")
        
        # Notifiera om >= 75 poäng
        if score['total_score'] >= 75:
            print(f"   🚨 **NOTIFIERAR VIA TELEGRAM**")
            notifications.append(format_telegram_message(listing, score))
        else:
            print(f"   ⏭️  Under tröskel (75), ingen notifiering")
        
        print()
    
    print("="*60)
    print(f"✅ Klar! {len(notifications)} notifieringar skickade.")
    print("="*60)
    print()
    
    if notifications:
        print("📱 EXEMPEL PÅ TELEGRAM-NOTIFIERING:")
        print("-"*60)
        print(notifications[0])
        print("-"*60)

if __name__ == "__main__":
    main()
