import sqlite3

def init():
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()#مؤشر

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS machines (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name_en TEXT NOT NULL,
            video_url TEXT NOT NULL,
            target_muscle TEXT NOT NULL,
            description TEXT
        )
    ''')

    data = [
        ('Chest Press Machine', '/static/videos/chest_press.mp4', 'Chest', 'Sit straight, grip handles, and push forward.'),
        ('Lat Pulldown Machine', '/static/videos/lat_pulldown.mp4', 'Back', 'Grip wide, pull bar down to upper chest, then release slowly.'),
        ('Leg Press Machine', '/static/videos/leg_press.mp4', 'Legs', 'Place feet shoulder-width apart, push platform away, and return slowly.')
    ]

    cursor.executemany('INSERT INTO machines (name_en, video_url, target_muscle, description) VALUES (?, ?, ?, ?)', data)
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init()