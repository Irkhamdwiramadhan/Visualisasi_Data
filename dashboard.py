import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("supermarket_sales - Sheet1 (1).csv")

# Konfigurasi halaman
st.set_page_config(
    page_title="Dashboard Analisis Data Supermarket",
    page_icon="🧺",
    layout="wide"
)

# === Tambahan CSS Custom ===
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f8f9fa;
    }
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1, h2, h3, h4 {
        color: #333333;
    }
    .stApp {
        background-color: #ffffff;
    }
    .info-box {
        background-color: #eef2f7;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        border: 1px solid #dee2e6;
    }
    </style>
""", unsafe_allow_html=True)

# === Sidebar ===
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/891/891462.png", width=80)
st.sidebar.markdown("### 🛒 Supermarket Dashboard")
st.sidebar.markdown("**Kelompok Exclusive**")
st.sidebar.markdown("---")

menu = st.sidebar.radio("Pilih Halaman:", (
    "🏠 Beranda",
    "📉 Korelasi Antar Kolom",
    "🏙️ Visualisasi Penjualan",
    "📈 Pola Transaksi"
))

# === Halaman Beranda ===
if menu == "🏠 Beranda":
    st.title("🛍️ Selamat Datang di Dashboard Supermarket")
    st.markdown("---")

    st.markdown("""
    <div class='info-box'>
        <h4>📌 Deskripsi Proyek</h4>
        Dashboard ini bertujuan untuk menganalisis data penjualan supermarket berdasarkan:
        <ul>
        <li>Kota dan Cabang Penjualan</li>
        <li>Kategori Produk</li>
        <li>Tipe Pelanggan</li>
        <li>Waktu dan Metode Pembayaran</li>
        </ul>
        Dibuat oleh <strong>Kelompok Exclusive</strong> dengan menggunakan <code>Python + Streamlit</code>.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='info-box'>
        <h4>👨‍💻 Anggota Kelompok</h4>
        <ul>
            <li>🧑‍🎓 Rifdah Qurrota Aini Dhiaulhaq — <code>110221257</code></li>
            <li>🧑‍🎓 M Irkham Dwi Ramadhan — <code>110223284</code></li>
            <li>🧑‍🎓 Muhammad Fauzan Adhima — <code>110223116</code></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🗂️ Dataset Penjualan")
    st.dataframe(df, use_container_width=True)

# === Halaman Visualisasi Penjualan ===
elif menu == "🏙️ Visualisasi Penjualan":
    st.title("💳 Visualisasi Rata-rata dan Distribusi Penjualan")
    st.markdown("---")

    gender_avg = df.groupby('Gender')['Total'].mean()
    cust_avg = df.groupby('Customer type')['Total'].mean()

    # Rata-rata Pembelian per Gender
    st.subheader("📌 Berdasarkan Gender")
    fig_gender = px.bar(
        x=gender_avg.index,
        y=gender_avg.values,
        labels={'x': 'Gender', 'y': 'Rata-rata Total Pembelian'},
        color=gender_avg.index,
        color_discrete_sequence=['#74c0fc', '#e599f7'],
        text=gender_avg.values.round(2),
        title="Rata-rata Pembelian per Gender"
    )
    fig_gender.update_traces(textposition='outside')
    fig_gender.update_layout(showlegend=False)
    st.plotly_chart(fig_gender, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Rata-rata Pembelian per Customer Type
    st.subheader("🧾 Berdasarkan Tipe Pelanggan")
    fig_cust = px.bar(
        x=cust_avg.index,
        y=cust_avg.values,
        labels={'x': 'Tipe Pelanggan', 'y': 'Rata-rata Total Pembelian'},
        color=cust_avg.index,
        color_discrete_sequence=['#f783ac', '#ffa94d'],
        text=cust_avg.values.round(2),
        title="Rata-rata Pembelian per Tipe Pelanggan",
    )
    fig_cust.update_traces(textposition='outside')
    fig_cust.update_layout(showlegend=False)
    st.plotly_chart(fig_cust, use_container_width=True)

    # Distribusi Produk
    st.subheader("📦 Distribusi Penjualan per Produk")
    product_counts = df['Product line'].value_counts().reset_index()
    product_counts.columns = ['Produk', 'Jumlah']
    fig = px.bar(product_counts, x='Jumlah', y='Produk', orientation='h',
                 color='Jumlah', color_continuous_scale='Plasma')
    st.plotly_chart(fig, use_container_width=True)

    # Distribusi Transaksi per Kota
    st.subheader("📍 Distribusi Jumlah Transaksi per Kota")
    city_counts = df['City'].value_counts().reset_index()
    city_counts.columns = ['City', 'Jumlah']
    fig = px.pie(city_counts, names='City', values='Jumlah',
                 color_discrete_sequence=px.colors.sequential.Viridis,
                 hole=0.4)
    fig.update_traces(textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)

    # Stacked Bar Produk per Cabang
    st.subheader("🏙️ Persentase Produk Terjual per Cabang")
    pivot_df = df.pivot_table(
        index='City',
        columns='Product line',
        values='Quantity',
        aggfunc='sum'
    )
    percentage_df = pivot_df.div(pivot_df.sum(axis=1), axis=0) * 100
    fig, ax = plt.subplots(figsize=(10, 6))
    left = [0] * len(pivot_df)

    for product in pivot_df.columns:
        values = pivot_df[product]
        ax.barh(pivot_df.index, values, left=left, label=product)
        for i, (value, l) in enumerate(zip(values, left)):
            if value > 0:
                percent = percentage_df.loc[pivot_df.index[i], product]
                ax.text(l + value / 2, i, f"{percent:.1f}%", ha='center', va='center', fontsize=8, color='white')
        left = [l + v for l, v in zip(left, values)]

    ax.set_title('Persentase Produk Terjual per Cabang berdasarkan Product Line')
    ax.set_xlabel('Jumlah Produk Terjual')
    ax.set_ylabel('Cabang')
    ax.legend(title='Product Line', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    st.pyplot(fig)

# === Halaman Pola Transaksi ===
elif menu == "📈 Pola Transaksi":
    df['Time'] = pd.to_datetime(df['Time'])
    df['Hour'] = df['Time'].dt.hour
    df['Date'] = pd.to_datetime(df['Date'])
    df['Day'] = df['Date'].dt.day_name()
    df['Month'] = df['Date'].dt.strftime('%B')

    bulan_tersedia = df['Month'].unique().tolist()
    bulan_tersedia.sort()
    bulan_dipilih = st.selectbox("📅 Pilih Bulan", bulan_tersedia)

    df_bulan = df[df['Month'] == bulan_dipilih]

    st.subheader(f"⏰ Jumlah Transaksi per Jam ({bulan_dipilih})")
    jam_range = range(10, 21)
    jam_agg = df_bulan[df_bulan['Hour'].isin(jam_range)].groupby('Hour').size().reindex(jam_range, fill_value=0)

    fig_jam, ax1 = plt.subplots(figsize=(10, 4))
    ax1.plot(jam_agg.index, jam_agg.values, marker='o', linestyle='-', color='steelblue')
    ax1.set_title("Jumlah Transaksi per Jam")
    ax1.set_xlabel("Jam")
    ax1.set_ylabel("Jumlah Transaksi")
    ax1.set_xticks(list(jam_range))
    ax1.grid(True)
    for i, v in enumerate(jam_agg.values):
        ax1.text(jam_agg.index[i], v + 0.5, str(v), ha='center', va='bottom', fontsize=8)
    st.pyplot(fig_jam)

    st.subheader(f"📅 Jumlah Transaksi per Hari ({bulan_dipilih})")
    hari_terlaris = df_bulan['Day'].value_counts().reindex([
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
    ], fill_value=0)

    fig_hari, ax2 = plt.subplots(figsize=(10, 4))
    ax2.bar(hari_terlaris.index, hari_terlaris.values, color='salmon')
    ax2.set_title("Jumlah Transaksi per Hari")
    ax2.set_xlabel("Hari")
    ax2.set_ylabel("Jumlah Transaksi")
    for i, v in enumerate(hari_terlaris.values):
        ax2.text(i, v + 0.5, str(v), ha='center', va='bottom', fontsize=8)
    st.pyplot(fig_hari)
