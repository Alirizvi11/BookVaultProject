import requests
from app.db_config import get_connection
  # ✅ Updated import path

# ✅ Fallback image
fallback_url = "https://covers.openlibrary.org/b/id/10909258-L.jpg"

# ✅ Book cover mapping (title → image URL)
book_covers = {
    "Harry Potter": "https://covers.openlibrary.org/b/id/7984916-L.jpg",
    "The Hobbit": "https://covers.openlibrary.org/b/id/6979861-L.jpg",
    "Percy Jackson": "https://covers.openlibrary.org/b/id/8231856-L.jpg",
    "Pride and Prejudice": "https://covers.openlibrary.org/b/id/8226191-L.jpg",
    "Me Before You": "https://covers.openlibrary.org/b/id/8231857-L.jpg",
    "The Hunger Games": "https://covers.openlibrary.org/b/id/8231858-L.jpg",
    "The Silent Patient": "https://covers.openlibrary.org/b/id/8231859-L.jpg",
    "The Alchemist": "https://covers.openlibrary.org/b/id/10909258-L.jpg",
    "Clean Code": "https://covers.openlibrary.org/b/id/8231856-L.jpg",
    "Think and Grow Rich": "https://covers.openlibrary.org/b/id/8231860-L.jpg",
    "Atomic Habits": "https://covers.openlibrary.org/b/id/8231861-L.jpg",
    "The Subtle Art of Not Giving a F*ck": "https://covers.openlibrary.org/b/id/8231862-L.jpg",
    "The 7 Habits of Highly Effective People": "https://covers.openlibrary.org/b/id/8231863-L.jpg",
    "How to Win Friends and Influence People": "https://covers.openlibrary.org/b/id/8231864-L.jpg",
    "The Power of Habit": "https://covers.openlibrary.org/b/id/8231865-L.jpg",
    "The Lean Startup": "https://covers.openlibrary.org/b/id/8231866-L.jpg",
    "Zero to One": "https://covers.openlibrary.org/b/id/8231867-L.jpg",
    "The Hard Thing About Hard Things": "https://covers.openlibrary.org/b/id/8231868-L.jpg",
    "Good to Great": "https://covers.openlibrary.org/b/id/8231869-L.jpg",
    "The Innovator's Dilemma": "https://covers.openlibrary.org/b/id/8231870-L.jpg",
    "The Art of War": "https://covers.openlibrary.org/b/id/8231871-L.jpg",
    "Meditations": "https://covers.openlibrary.org/b/id/8231872-L.jpg",
    "Sapiens: A Brief History of Humankind": "https://covers.openlibrary.org/b/id/8231873-L.jpg",
    "Educated": "https://covers.openlibrary.org/b/id/8231874-L.jpg",
    "To Kill a Mockingbird": "https://covers.openlibrary.org/b/id/8226190-L.jpg",
    "1984": "https://covers.openlibrary.org/b/id/8226192-L.jpg",
    "The Great Gatsby": "https://covers.openlibrary.org/b/id/8226193-L.jpg",
    "The Catcher in the Rye": "https://covers.openlibrary.org/b/id/8226194-L.jpg",
    "The Lord of the Rings": "https://covers.openlibrary.org/b/id/8226195-L.jpg",
    "The Da Vinci Code": "https://covers.openlibrary.org/b/id/8226196-L.jpg",
    "The Kite Runner": "https://covers.openlibrary.org/b/id/8226197-L.jpg",
    "The Book Thief": "https://covers.openlibrary.org/b/id/8226198-L.jpg",
    "Brave New World": "https://covers.openlibrary.org/b/id/8226199-L.jpg",
    "Jane Eyre": "https://covers.openlibrary.org/b/id/8226200-L.jpg",
    "Wuthering Heights": "https://covers.openlibrary.org/b/id/8226201-L.jpg",
    "Moby Dick": "https://covers.openlibrary.org/b/id/8226202-L.jpg",
    "War and Peace": "https://covers.openlibrary.org/b/id/8226203-L.jpg",
    "Crime and Punishment": "https://covers.openlibrary.org/b/id/8226204-L.jpg",
    "The Odyssey": "https://covers.openlibrary.org/b/id/8226205-L.jpg",
    "Anna Karenina": "https://covers.openlibrary.org/b/id/8226206-L.jpg",
    "The Brothers Karamazov": "https://covers.openlibrary.org/b/id/8226207-L.jpg",
    "Don Quixote": "https://covers.openlibrary.org/b/id/8226208-L.jpg",
    "The Shining": "https://covers.openlibrary.org/b/id/8226209-L.jpg",
    "It": "https://covers.openlibrary.org/b/id/8226210-L.jpg",
    "Misery": "https://covers.openlibrary.org/b/id/8226211-L.jpg",
    "The Stand": "https://covers.openlibrary.org/b/id/8226212-L.jpg",
    "Game of Thrones": "https://covers.openlibrary.org/b/id/8226213-L.jpg",
    "A Clash of Kings": "https://covers.openlibrary.org/b/id/8226214-L.jpg",
    "A Storm of Swords": "https://covers.openlibrary.org/b/id/8226215-L.jpg",
    "The Fault in Our Stars": "https://covers.openlibrary.org/b/id/8226216-L.jpg",
    "Gone Girl": "https://covers.openlibrary.org/b/id/8226217-L.jpg",
    "Becomming": "https://covers.openlibrary.org/b/id/8226218-L.jpg",
    "Power of Now": "https://covers.openlibrary.org/b/id/8231875-L.jpg",
    "Rich Dad Poor Dad": "https://covers.openlibrary.org/b/id/8231876-L.jpg",
    "Wings of Fire": "https://covers.openlibrary.org/b/id/8231877-L.jpg",
    "The Monk Who Sold His Ferrari": "https://covers.openlibrary.org/b/id/8231878-L.jpg",
    "Ikigai": "https://covers.openlibrary.org/b/id/8231879-L.jpg",
    "Start with Why": "https://covers.openlibrary.org/b/id/8231880-L.jpg",
    "Life of Pi": "https://covers.openlibrary.org/b/id/8231881-L.jpg",
    "The Psychology of Money": "https://covers.openlibrary.org/b/id/8231882-L.jpg"
}

# ✅ Image URL validator
def is_valid_image(url: str) -> bool:
    try:
        res = requests.head(url, allow_redirects=True, timeout=5)
        return res.status_code == 200 and "image" in res.headers.get("content-type", "")
    except:
        return False

# ✅ Connect to DB
conn = get_connection()
cursor = conn.cursor()

# ✅ Seed covers with validation
for title, url in book_covers.items():
    final_url = url if is_valid_image(url) else fallback_url
    cursor.execute("""
        UPDATE books
        SET cover_url = ?
        WHERE LOWER(title) LIKE LOWER(?)
    """, (final_url, f"%{title}%"))

conn.commit()
cursor.close()
conn.close()

print("✅ Book cover URLs seeded successfully.")
