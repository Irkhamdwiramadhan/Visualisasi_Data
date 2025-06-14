import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Supermarket", layout="wide")

st.title("📊 Dashboard Analisis Supermarket Sales")
st.markdown("Upload file CSV dari dataset penjualan supermarket Anda untuk melihat analisis interaktif.")

uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Hapus kolom yang tidak dibutuhkan jika ada
    if 'gross margin percentage' in df.columns:
        df.drop(columns=['gross margin percentage'], inplace=True)

    st.subheader("🧾 Dataset")
    st.dataframe(df, use_container_width=True)

    # Distribusi jumlah transaksi per kota
    st.subheader("🏙️ Distribusi Jumlah Transaksi per Kota")
    city_counts = df['City'].value_counts()
    fig1, ax1 = plt.subplots()
    colors = ['#66c2a5', '#fc8d62', '#8da0cb']
    ax1.pie(city_counts.values, labels=city_counts.index, colors=colors, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

    # Jumlah transaksi per product line
    st.subheader("🛒 Jumlah Transaksi per Product Line")
    product_counts = df['Product line'].value_counts()
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    bars = ax2.bar(product_counts.index, product_counts.values, color='#8da0cb')
    ax2.set_xlabel('Product Line')
    ax2.set_ylabel('Jumlah Transaksi')
    ax2.set_title('Jumlah Transaksi per Product Line')
    plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2, height + 1, str(height), ha='center', va='bottom')
    st.pyplot(fig2)
else:
    st.warning("Silakan upload file CSV terlebih dahulu.")
