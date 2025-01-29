import sqlite3
import pandas as pd

def create_tables():
    """Create SQLite tables for all worksheets."""
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    
    # Physicians Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Physicians (
            Name TEXT PRIMARY KEY,
            Speciality TEXT,
            Degree TEXT
        )
    ''')
    
    # Schedules Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Schedules (
            Doctor_Name TEXT PRIMARY KEY,
            Monday TEXT,
            Tuesday TEXT,
            Wednesday TEXT,
            Thursday TEXT,
            Friday TEXT,
            Saturday TEXT,
            Sunday TEXT
        )
    ''')
    
    # Specialities Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Specialities (
            Speciality_Name TEXT PRIMARY KEY,
            Definition TEXT
        )
    ''')
    
    # Pricelist Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Pricelist (
            Service_Name TEXT PRIMARY KEY,
            Price_USD REAL
        )
    ''')
    
    conn.commit()
    conn.close()

def load_data_from_excel():
    """Load data from Xyris_HIS_data.xlsx into the database."""
    excel_file = "C://Users//micka//Downloads//Pain-Go-HIS-main//Pain-Go-HIS-main//Xyris HIS_data.xlsx"

    
    # Load Physicians data
    df_physicians = pd.read_excel(excel_file, sheet_name='Physicians')
    df_physicians.to_sql('Physicians', sqlite3.connect('hospital.db'), if_exists='replace', index=False)
    
    # Load Schedules data
    df_schedules = pd.read_excel(excel_file, sheet_name='Schedules')
    df_schedules.to_sql('Schedules', sqlite3.connect('hospital.db'), if_exists='replace', index=False)
    
    # Load Specialities data
    df_specialities = pd.read_excel(excel_file, sheet_name='Specialities')
    df_specialities.to_sql('Specialities', sqlite3.connect('hospital.db'), if_exists='replace', index=False)
    
    # Load Pricelist data
    df_pricelist = pd.read_excel(excel_file, sheet_name='Pricelist')
    df_pricelist.to_sql('Pricelist', sqlite3.connect('hospital.db'), if_exists='replace', index=False)

if __name__ == '__main__':
    create_tables()
    load_data_from_excel()
    print("Database initialized successfully!")