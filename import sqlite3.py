import sqlite3

# 1. Kuunganisha na Database
conn = sqlite3.connect('wateja.db')
cursor = conn.cursor()

# 2. Kuumba jedwali linalokubali vyanzo vyote vitatu
cursor.execute('''
    CREATE TABLE IF NOT EXISTS wateja (
        user_id TEXT PRIMARY KEY,
        platform TEXT,      -- Hapa tutaandika kama ni 'telegram', 'whatsapp', au 'website'
        status TEXT,        -- Mfano: 'active' au 'expired'
        expiry_date TEXT
    )
''')
conn.commit()

# 3. Kazi ya kuandika mteja mpya kwenye database
def ongeza_mteja(user_id, platform):
    try:
        cursor.execute("INSERT INTO wateja (user_id, platform, status) VALUES (?, ?, ?)", 
                       (user_id, platform, 'active'))
        conn.commit()
        print(f"Mteja {user_id} kutoka {platform} ameongezwa!")
    except sqlite3.IntegrityError:
        print("Mteja huyu tayari yupo kwenye mfumo.")

# Mfano wa jinsi ya kutumia:
# ongeza_mteja("255712345678", "whatsapp")
# ongeza_mteja("123456789", "telegram")
# ongeza_mteja("user_wa_tovuti123", "website")