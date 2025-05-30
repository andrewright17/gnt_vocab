import sqlite3
import csv
import os
import sqlite3

# Get repo root by going up from script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.abspath(os.path.join(script_dir, '..'))

# Define DB path relative to repo root
db_path = os.path.join(repo_root, 'data', 'gnt.db')

# Ensure the data/ directory exists
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Connect to DB
conn = sqlite3.connect(db_path)


# Path to your TSV file
tsv_file_path = os.path.join(repo_root, 'data', 'lemma_95.tsv')

cursor = conn.cursor()

# Create the lemma table
cursor.execute('''
CREATE TABLE IF NOT EXISTS lemma (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lemma TEXT NOT NULL,
    count INTEGER,
    gloss TEXT
)
''')
conn.commit()

# Load data from TSV and insert into the lemma table
with open(tsv_file_path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter='\t')
    for row in reader:
        cursor.execute('''
            INSERT INTO lemma (lemma, count, gloss)
            VALUES (?, ?, ?)
        ''', (row['lemma'], int(row['count']), row['gloss']))

conn.commit()
conn.close()

