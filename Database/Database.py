import sqlite3

class Person:

    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()

        # Tabloyu oluştur
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS infos (
            p_id INT PRIMARY KEY,
            p_name VARCHAR(255),
            p_surname VARCHAR(255)
        )
        """)

        # Veriyi ekle
        self.cursor.execute("INSERT INTO infos (p_id, p_name, p_surname) VALUES (?, ?, ?)", 
                            (self.id, self.name, self.surname))

        # Veriyi oku
        self.cursor.execute("SELECT * FROM infos")
        rows = self.cursor.fetchall()

        # Sonuçları yazdır
        print(rows)

        # Bağlantıyı kapat
        self.connection.commit()
        self.connection.close()


# Sınıfı kullan
no_one = Person(4, "Abdurrahman", "Karadag")
