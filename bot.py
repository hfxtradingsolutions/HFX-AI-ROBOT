<<<<<<< HEAD
import sqlite3
import datetime
from googleapiclient.discovery import build

# --- 1. SANIDI DATABASE ---
conn = sqlite3.connect('wateja.db')
cursor = conn.cursor()

# Hii ni hatua mpya ya kurekebisha database yako ya zamani
cursor.execute('''
    CREATE TABLE IF NOT EXISTS wateja (
        user_id TEXT PRIMARY KEY,
        start_date TIMESTAMP,
        is_paid TEXT DEFAULT 'false'
    )
''')

# Hii inaongeza column ikikosekana
try:
    cursor.execute("ALTER TABLE wateja ADD COLUMN start_date TIMESTAMP")
    conn.commit()
except sqlite3.OperationalError:
    pass # Column tayari ipo

conn.commit()

# --- 2. API YA YOUTUBE ---
API_KEY = 'AIzaSyA926vcpYAdoEbd6xUi-ewYaB1cxlw6AJs'
youtube = build('youtube', 'v3', developerKey=API_KEY)

# --- 3. KAZI YA KUTAFUTA VIDEO ---
def pata_linki_za_video(query):
    request = youtube.search().list(part="snippet", q=query, type="video", maxResults=3)
    response = request.execute()
    
    matokeo = "--- VIDEO ZILIZOPATIKANA ---\n"
    for item in response.get('items', []):
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        matokeo += f"Video: {title}\nLink: https://www.youtube.com/watch?v={video_id}\n\n"
    return matokeo

# --- 4. LOGIC YA TRIAL (Siku 3) ---
def tafuta_video(user_id, query):
    cursor.execute("SELECT start_date, is_paid FROM wateja WHERE user_id = ?", (user_id,))
    data = cursor.fetchone()
    
    now = datetime.datetime.now()

    # Kama mteja ni mpya, anza trial yake ya siku 3
    if data is None:
        start_date = now.isoformat()
        cursor.execute("INSERT INTO wateja (user_id, start_date, is_paid) VALUES (?, ?, ?)", (user_id, start_date, 'false'))
        conn.commit()
        return f"Karibu! Una siku 3 za bure. \n{pata_linki_za_video(query)}"

    start_date_str, is_paid = data
    start_date = datetime.datetime.fromisoformat(start_date_str)
    
    # Angalia kama trial imeisha (siku 3 = 72 hours)
    days_passed = (now - start_date).days
    
    if is_paid == 'true':
        return f"Karibu tena VIP! \n{pata_linki_za_video(query)}"
    
    if days_passed < 3:
        return f"Upo kwenye siku zako za bure ({3 - days_passed} zimebaki). \n{pata_linki_za_video(query)}"
    else:
        return "Trial yako imeisha! Tafadhali unganisha kadi yako ya malipo."

# --- 5. BOT LOOP ---
def start_bot():
    print("Bot ya HFX AI inasikiliza...")
    while True:
        user_input = input("Weka swali lako (au 'exit' kutoka): ")
        if user_input.lower() == 'exit':
            break
        matokeo = tafuta_video("user_123", user_input)
        print(matokeo)

if __name__ == "__main__":
=======
import sqlite3
import datetime
from googleapiclient.discovery import build

# --- 1. SANIDI DATABASE ---
conn = sqlite3.connect('wateja.db')
cursor = conn.cursor()

# Hii ni hatua mpya ya kurekebisha database yako ya zamani
cursor.execute('''
    CREATE TABLE IF NOT EXISTS wateja (
        user_id TEXT PRIMARY KEY,
        start_date TIMESTAMP,
        is_paid TEXT DEFAULT 'false'
    )
''')

# Hii inaongeza column ikikosekana
try:
    cursor.execute("ALTER TABLE wateja ADD COLUMN start_date TIMESTAMP")
    conn.commit()
except sqlite3.OperationalError:
    pass # Column tayari ipo

conn.commit()

# --- 2. API YA YOUTUBE ---
API_KEY = 'AIzaSyA926vcpYAdoEbd6xUi-ewYaB1cxlw6AJs'
youtube = build('youtube', 'v3', developerKey=API_KEY)

# --- 3. KAZI YA KUTAFUTA VIDEO ---
def pata_linki_za_video(query):
    request = youtube.search().list(part="snippet", q=query, type="video", maxResults=3)
    response = request.execute()
    
    matokeo = "--- VIDEO ZILIZOPATIKANA ---\n"
    for item in response.get('items', []):
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        matokeo += f"Video: {title}\nLink: https://www.youtube.com/watch?v={video_id}\n\n"
    return matokeo

# --- 4. LOGIC YA TRIAL (Siku 3) ---
def tafuta_video(user_id, query):
    cursor.execute("SELECT start_date, is_paid FROM wateja WHERE user_id = ?", (user_id,))
    data = cursor.fetchone()
    
    now = datetime.datetime.now()

    # Kama mteja ni mpya, anza trial yake ya siku 3
    if data is None:
        start_date = now.isoformat()
        cursor.execute("INSERT INTO wateja (user_id, start_date, is_paid) VALUES (?, ?, ?)", (user_id, start_date, 'false'))
        conn.commit()
        return f"Karibu! Una siku 3 za bure. \n{pata_linki_za_video(query)}"

    start_date_str, is_paid = data
    start_date = datetime.datetime.fromisoformat(start_date_str)
    
    # Angalia kama trial imeisha (siku 3 = 72 hours)
    days_passed = (now - start_date).days
    
    if is_paid == 'true':
        return f"Karibu tena VIP! \n{pata_linki_za_video(query)}"
    
    if days_passed < 3:
        return f"Upo kwenye siku zako za bure ({3 - days_passed} zimebaki). \n{pata_linki_za_video(query)}"
    else:
        return "Trial yako imeisha! Tafadhali unganisha kadi yako ya malipo."

# --- 5. BOT LOOP ---
def start_bot():
    print("Bot ya HFX AI inasikiliza...")
    while True:
        user_input = input("Weka swali lako (au 'exit' kutoka): ")#
        if user_input.lower() == 'exit':
            break
        matokeo = tafuta_video("user_123", user_input)
        print(matokeo)

if __name__ == "__main__":
>>>>>>> 742c857 (fix module)
    start_bot()