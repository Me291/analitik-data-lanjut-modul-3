import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul aplikasi
st.title('Streamlit Simple App')

# Menambahkan navigasi di sidebar
page = st.sidebar.radio("Pilih halaman", ["Dataset", "Visualisasi"])

if page == "Dataset":
    st.header("Halaman Dataset")
    
    # Baca file Excel
    data = pd.read_excel("pddikti_example.xlsx")
    
    # Tampilkan data di Streamlit
    st.write(data)
    
elif page == "Visualisasi":
    st.header("Halaman Visualisasi")
    
    # Menonaktifkan peringatan terkait penggunaan pyplot global
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Baca file Excel
    data = pd.read_excel("pddikti_example.xlsx")

    # Filter berdasarkan universitas
    selected_university = st.selectbox('Pilih Universitas', data['universitas'].unique())
    filtered_data = data[data['universitas'] == selected_university]

    # Buat visualisasi
    plt.figure(figsize=(12, 6))

    for prog_studi in filtered_data['program_studi'].unique():
        subset = filtered_data[filtered_data['program_studi'] == prog_studi]
        
        # Urutkan data berdasarkan 'id' dengan urutan menurun
        subset = subset.sort_values(by="id", ascending=False)
        
        # Plot data
        plt.plot(subset['semester'], subset['jumlah'], label=prog_studi)

    plt.title(f"Visualisasi Data untuk {selected_university}")
    plt.xlabel('Semester')
    plt.xticks(rotation=90)  # Rotasi label sumbu x menjadi vertikal
    plt.ylabel('Jumlah')
    plt.legend()

    # Tampilkan plot di Streamlit
    st.pyplot()
