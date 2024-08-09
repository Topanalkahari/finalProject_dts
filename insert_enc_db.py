import pandas as pd
import mysql.connector
from mysql.connector import Error

# Load data dari file CSV
csv_file = 'course_data_enc.csv'
data = pd.read_csv(csv_file)

# Koneksi ke database MySQL
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Topan#97',
        database='fp_DTS_enc'
    )

    if conn.is_connected():
        cursor = conn.cursor()

        # Buat query untuk memasukkan data
        for i, row in data.iterrows():
            sql = """
            INSERT INTO CourseData (CourseCategory, TimeSpentOnCourse, NumberOfVideosWatched, NumberOfQuizzesTaken, QuizScores, CompletionRate, DeviceType, CourseCompletion)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, tuple(row))

        # Commit perubahan
        conn.commit()
        print("Data berhasil diimpor ke database.")

except Error as e:
    print(f"Error: {e}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()