import tkinter as tk
from tkinter import ttk
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Koneksi ke database MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Topan#97",
    database="fp_DTS_enc"
)
cursor = conn.cursor()

# Fungsi untuk mengambil data dari database
def fetch_data():
    query = "SELECT * FROM CourseData"
    cursor.execute(query)
    data = cursor.fetchall()
    # Dapatkan kolom dari kursor untuk mencocokkan dengan data yang dikembalikan
    columns = [desc[0] for desc in cursor.description]
    return pd.DataFrame(data, columns=columns)

# Fungsi untuk membuat heatmap korelasi
def plot_correlation_heatmap():
    data = fetch_data()
    correlation = data.corr()
    sns.heatmap(correlation, annot=True)
    plt.title('Correlation Heatmap')
    plt.show()

# Fungsi untuk membuat scatter plot
def plot_scatter():
    data = fetch_data()
    x_var = x_var_dropdown.get()
    y_var = y_var_dropdown.get()
    sns.scatterplot(x=x_var, y=y_var, data=data)
    plt.title(f'Scatter Plot: {x_var} vs {y_var}')
    plt.xlabel(x_var)
    plt.ylabel(y_var)
    plt.show()

# Fungsi untuk membuat bar chart
def plot_bar_chart():
    data = fetch_data()
    x_var = x_var_dropdown.get()
    y_var = y_var_dropdown.get()
    sns.barplot(x=x_var, y=y_var, data=data)
    plt.title(f'Bar Chart: {y_var} by {x_var}')
    plt.show()

# Fungsi untuk membuat box plot
def plot_box_plot():
    data = fetch_data()
    x_var = x_var_dropdown.get()
    y_var = y_var_dropdown.get()
    sns.boxplot(x=x_var, y=y_var, data=data)
    plt.title(f'Box Plot: {y_var} by {x_var}')
    plt.show()

# Fungsi untuk membuat histogram
def plot_histogram():
    data = fetch_data()
    x_var = x_var_dropdown.get()
    data[x_var].hist()
    plt.title(f'Histogram of {x_var}')
    plt.xlabel(x_var)
    plt.ylabel('Frequency')
    plt.show()

# Fungsi untuk membuat line plot
def plot_line_plot():
    data = fetch_data()
    x_var = x_var_dropdown.get()
    y_var = y_var_dropdown.get()
    data.groupby(x_var)[y_var].mean().plot(kind='line')
    plt.title(f'Line Plot: Average {y_var} by {x_var}')
    plt.xlabel(x_var)
    plt.ylabel(f'Average {y_var}')
    plt.show()

# Fungsi untuk menampilkan visualisasi berdasarkan pilihan pengguna
def plot_visualization():
    vis_type = vis_type_var.get()
    if vis_type == "Heatmap":
        plot_correlation_heatmap()
    elif vis_type == "Scatter Plot":
        plot_scatter()
    elif vis_type == "Bar Chart":
        plot_bar_chart()
    elif vis_type == "Box Plot":
        plot_box_plot()
    elif vis_type == "Histogram":
        plot_histogram()
    elif vis_type == "Line Plot":
        plot_line_plot()

# Antarmuka TkInter
root = tk.Tk()
root.title("Course Analysis Dashboard")
root.geometry("800x600")

# Dropdown untuk memilih variabel sumbu X
x_var_label = ttk.Label(root, text="Select X-axis Variable:")
x_var_label.pack()
x_var_dropdown = ttk.Combobox(root, values=[
    'CourseCategory', 'TimeSpentOnCourse', 'NumberOfVideosWatched',
    'NumberOfQuizzesTaken', 'QuizScores', 'DeviceType', 'CompletionRate'
])
x_var_dropdown.current(0)
x_var_dropdown.pack()

# Dropdown untuk memilih variabel sumbu Y
y_var_label = ttk.Label(root, text="Select Y-axis Variable:")
y_var_label.pack()
y_var_dropdown = ttk.Combobox(root, values=[
    'CourseCategory', 'TimeSpentOnCourse', 'NumberOfVideosWatched',
    'NumberOfQuizzesTaken', 'QuizScores', 'DeviceType', 'CompletionRate'
])
y_var_dropdown.current(1)
y_var_dropdown.pack()

# Dropdown untuk memilih jenis visualisasi
vis_type_label = ttk.Label(root, text="Select Visualization Type:")
vis_type_label.pack()
vis_type_var = tk.StringVar()
vis_type_dropdown = ttk.Combobox(root, textvariable=vis_type_var, values=[
    "Heatmap", "Scatter Plot", "Bar Chart", "Box Plot", "Histogram", "Line Plot"
])
vis_type_dropdown.current(0)
vis_type_dropdown.pack()

# Tombol untuk menampilkan visualisasi
btn_visualize = ttk.Button(root, text="Show Visualization", command=plot_visualization)
btn_visualize.pack()

root.mainloop()
