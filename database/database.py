import sqlite3


DATABASE_NAME = "database/examforge.db"


# ============================================
# DATABASE CONNECTION
# ============================================

def get_connection():

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    connection.row_factory = sqlite3.Row

    return connection


# ============================================
# CREATE TABLES
# ============================================

def create_tables():

    connection = get_connection()

    cursor = connection.cursor()


    # ========================================
    # QUESTIONS TABLE
    # ========================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS questions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            question TEXT NOT NULL,

            subject TEXT NOT NULL,

            unit INTEGER NOT NULL,

            topic TEXT NOT NULL,

            difficulty TEXT NOT NULL,

            marks INTEGER NOT NULL,

            priority INTEGER DEFAULT 1,

            usage_count INTEGER DEFAULT 0

        )
        """
    )


    # ========================================
    # PAPER HISTORY TABLE
    # ========================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS paper_history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            total_marks INTEGER NOT NULL,

            easy_count INTEGER NOT NULL,

            medium_count INTEGER NOT NULL,

            hard_count INTEGER NOT NULL,

            method TEXT NOT NULL,

            question_count INTEGER NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """
    )


    connection.commit()

    connection.close()


# ============================================
# RUN DATABASE SETUP
# ============================================

if __name__ == "__main__":

    create_tables()

    print(
        "Database tables created successfully!"
    )