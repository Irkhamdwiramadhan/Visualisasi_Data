import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load Dataset ---
df = pd.read_csv("supermarket_sales - Sheet1 (1).csv")

st.set_page_config(
    page_title="Dashboard Analisis Data Supermarket",
    page_icon="🧺"
)
st.markdown("""
    <style>
    /* ====== BACKGROUND UTAMA ====== */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa, #e8f0fe);
        font-family: 'Segoe UI', sans-serif;
        color: #333;
    }

    /* ====== JUDUL DAN TEKS ====== */
    h1, h2, h3, h4 {
        color: #2c3e50;
        font-weight: 600;
    }

    /* ====== SIDEBAR ====== */
    [data-testid="stSidebar"] {
        background-color: #3f5d7d !important;  /* Lebih gelap */
        color: white !important;
        border: none;
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    .stRadio label {
        color: white !important;
    }

    /* ====== NAVBAR ====== */
    header, .css-18ni7ap {
        background-color: #dce3ec !important;  /* Lebih terang dari sidebar, lebih gelap dari background */
        color: #333 !important;
        border-bottom: 1px solid #ccc;
    }

    /* ====== TOMBOL UTAMA ====== */
    button[kind="primary"] {
        background-color: #2e7d32;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1.2rem;
    }

    button[kind="primary"]:hover {
        background-color: #1b5e20;
    }

    /* ====== TABEL / KARTU DATA ====== */
    .css-1d391kg {
        background: #ffffff;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }

    /* ====== HILANGKAN FOOTER STREAMLIT ====== */
    footer, .css-164nlkn {
        display: none !important;
    }

    /* ====== SPASI UMUM KONTEN ====== */
    .block-container {
        padding: 2rem 3rem;
    }
    </style>
""", unsafe_allow_html=True)






color_discrete_sequence=px.colors.qualitative.Pastel




# --- Sidebar ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/891/891462.png", width=80)
st.sidebar.markdown("### 🛒 Supermarket Dashboard")
st.sidebar.markdown("**Kelompok Exclusive**")

st.sidebar.markdown("---")

# Radio dengan label dan emoji disamakan dengan bagian if
menu = st.sidebar.radio("Pilih Halaman:", (
    "🏠 Beranda",
    "📉 Korelasi Antar Kolom",
    "🏙️ Visualisasi Penjualan",
    "📈 Pola Transaksi"
   
))

# --- Tampilan Halaman ---
if menu == "🏠 Beranda":
    # CSS agar tampilan lebih lebar hanya di beranda
    st.markdown(
        """
        <style>
        .main .block-container {
            max-width: 100% !important;
            padding-left: 3rem;
            padding-right: 3rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("🛍️ Selamat Datang di Dashboard Supermarket")
    st.write("---")

    st.markdown("""
    ### 📌 Deskripsi Proyek  
    Dashboard ini merupakan bagian dari proyek analisis data yang bertujuan untuk memahami pola penjualan di sebuah supermarket berdasarkan berbagai variabel seperti:
    - Kota dan cabang penjualan
    - Kategori produk
    - Tipe pelanggan
    - Waktu dan metode pembayaran

    Proyek ini dikerjakan oleh **tiga anggota tim** sebagai latihan penerapan analisis data dan visualisasi interaktif menggunakan **Python + Streamlit**.
    """)

    st.markdown("""
    ### 👨‍💻 Anggota Kelompok  
    **Kelompok Exclusive – Visualisasi Data**
    - 🧑‍🎓 Rifdah Qurrota Aini Dhiaulhaq — `110221257`
    - 🧑‍🎓 M Irkham Dwi Ramadhan — `110223284`
    - 🧑‍🎓 Muhammad Fauzan Adhima — `110223116`
    """)

    st.write("---")
    st.markdown("### 🗂️ Dataset Penjualan")
    st.dataframe(df)

elif menu == "🏙️ Visualisasi Penjualan":
   

    st.title("💳 Rata-rata Pembelian")
    st.write("---")
    # Hitung rata-rata
    gender_avg = df.groupby('Gender')['Total'].mean()
    cust_avg = df.groupby('Customer type')['Total'].mean()

    # === Visualisasi Gender (Full Width) ===
    st.subheader("📌 Berdasarkan Gender")
    fig_gender = px.bar(
        x=gender_avg.index,
        y=gender_avg.values,
        labels={'x': 'Gender', 'y': 'Rata-rata Total Pembelian'},
        color=gender_avg.index,
        color_discrete_sequence=['skyblue', 'lightgreen'],
        text=gender_avg.values.round(2),
        title="Rata-rata Pembelian per Gender"
    )
    fig_gender.update_traces(textposition='outside')
    fig_gender.update_layout(showlegend=False)
    st.plotly_chart(fig_gender, use_container_width=True)

    # Spasi Vertikal
    st.markdown("<br><br>", unsafe_allow_html=True)

    # === Visualisasi Customer Type (Full Width) ===
    st.subheader("🧾 Berdasarkan Tipe Pelanggan")
    fig_cust = px.bar(
        x=cust_avg.index,
        y=cust_avg.values,
        labels={'x': 'Tipe Pelanggan', 'y': 'Rata-rata Total Pembelian'},
        color=cust_avg.index,
        color_discrete_sequence=['pink', 'orange'],
        text=cust_avg.values.round(2),
        title="Rata-rata Pembelian per Tipe Pelanggan",
    )
    fig_cust.update_traces(textposition='outside')
    fig_cust.update_layout(showlegend=False)
    st.plotly_chart(fig_cust, use_container_width=True)
    st.write("rata-rata pembelian pelanggan perempuan lebih tinggi dibanding laki-laki. Ini menunjukkan bahwa perempuan cenderung belanja lebih banyak. Selain itu, pelanggan yang sudah menjadi member juga belanja lebih banyak dibanding pelanggan biasa. Artinya, program member bisa mendorong peningkatan pembelian. Informasi ini bisa digunakan untuk membuat strategi promosi yang lebih tepat, misalnya fokus ke pelanggan perempuan dan mendorong lebih banyak orang menjadi member.")
    



    st.subheader("📦 Distribusi Penjualan per Produk")
    product_counts = df['Product line'].value_counts().reset_index()
    product_counts.columns = ['Produk', 'Jumlah']
    fig = px.bar(product_counts, x='Jumlah', y='Produk', orientation='h',
                 color='Jumlah', color_continuous_scale='Plasma')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📍 Distribusi Jumlah Transaksi per Kota")
    city_counts = df['City'].value_counts().reset_index()
    city_counts.columns = ['City', 'Jumlah']

    fig = px.pie(city_counts, names='City', values='Jumlah',
                 color_discrete_sequence=px.colors.sequential.Viridis,
                 hole=0.4)
    fig.update_traces(textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)
    st.write("Visualisasi ini menunjukkan jumlah transaksi untuk setiap kategori produk. Kategori Fashion accessories menempati posisi teratas dengan jumlah transaksi terbanyak (178), diikuti oleh Food and beverages (174), dan Electronic accessories (170). Sementara itu, kategori dengan jumlah transaksi paling rendah adalah Health and beauty (152). Perbedaan jumlah transaksi antar kategori tidak terlalu besar, yang berarti semua lini produk memiliki performa yang cukup baik. Namun, dari sini kita bisa melihat bahwa produk fashion dan makanan menjadi pilihan utama pelanggan. Hal ini bisa dimanfaatkan untuk fokus pada promosi atau stok lebih besar di kategori tersebut. Sebaliknya, lini seperti Health and Beauty yang lebih rendah performanya bisa dianalisis lebih lanjut — apakah karena kurangnya minat, strategi promosi yang kurang tepat, atau faktor lain.")

    st.subheader("🏙️ Persentase Produk Terjual per Cabang")

    # Pivot untuk total quantity per branch dan product line
    pivot_df = df.pivot_table(
        index='City',
        columns='Product line',
        values='Quantity',
        aggfunc='sum'
    )

    # Hitung persentase tiap produk terhadap total cabang
    percentage_df = pivot_df.div(pivot_df.sum(axis=1), axis=0) * 100

    # Plot stacked bar horizontal
    fig, ax = plt.subplots(figsize=(10, 6))
    left = [0] * len(pivot_df)

    for product in pivot_df.columns:
        values = pivot_df[product]
        ax.barh(pivot_df.index, values, left=left, label=product)

        # Label persentase
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

    # Tampilkan di dashboard
    st.pyplot(fig)
    st.write("Perusahaan sebaiknya mempertimbangkan untuk menyesuaikan stok dan strategi promosi di tiap cabang berdasarkan pola pembelian yang berbeda. Misalnya, di cabang Naypyitaw, produk makanan dan minuman sangat diminati, jadi stoknya bisa ditambah dan promosi difokuskan pada produk tersebut. Sementara di Yangon, produk rumah tangga lebih laku, jadi fokus bisa diarahkan ke sana. Di Mandalay, penjualan cukup seimbang, tapi bisa lebih ditingkatkan dengan promosi produk kesehatan dan olahraga yang cukup menonjol.")

elif menu == "📈 Pola Transaksi":
    st.title("Pola Transaksi")
    # --- Parsing kolom waktu ---
    df['Time'] = pd.to_datetime(df['Time'])
    df['Hour'] = df['Time'].dt.hour
    df['Date'] = pd.to_datetime(df['Date'])
    df['Day'] = df['Date'].dt.day_name()
    df['Month'] = df['Date'].dt.strftime('%B')  # Tambah nama bulan (e.g., January)

    # --- Filter bulan ---
    bulan_tersedia = df['Month'].unique().tolist()
    bulan_tersedia.sort()  # Urutkan alfabet
    bulan_dipilih = st.selectbox("📅 Pilih Bulan", bulan_tersedia)

    # Filter dataframe berdasarkan bulan yang dipilih
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
    ax2.plot(hari_terlaris.index, hari_terlaris.values, marker='o', linestyle='-', color='salmon')
    ax2.set_title("Distribusi Transaksi per Hari")
    ax2.set_xlabel("Hari")
    ax2.set_ylabel("Jumlah Transaksi")
    ax2.set_xticklabels(hari_terlaris.index, rotation=45)
    ax2.grid(True)
    for i, v in enumerate(hari_terlaris.values):
        ax2.text(i, v + 0.5, str(v), ha='center', va='bottom', fontsize=8)
    st.pyplot(fig_hari)

    st.subheader(f"🔥 Heatmap Transaksi Berdasarkan Hari dan Jam ({bulan_dipilih})")
    df_bulan['Hour'] = df_bulan['Time'].dt.hour
    df_bulan['Day'] = df_bulan['Date'].dt.day_name()

    pivot = df_bulan.pivot_table(index='Day', columns='Hour', values='Invoice ID', aggfunc='count')
    ordered_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    pivot = pivot.reindex(ordered_days)

    fig_heatmap, ax = plt.subplots(figsize=(12, 5))
    sns.heatmap(pivot, cmap='YlOrRd', linewidths=0.5, annot=True, fmt='g', ax=ax)
    ax.set_title('Heatmap Transaksi: Hari vs Jam')
    ax.set_xlabel('Jam')
    ax.set_ylabel('Hari')
    st.pyplot(fig_heatmap)


elif menu == "📉 Korelasi Antar Kolom":
    st.title("📉 Scatter Plot Interaktif")

    # Pilih kolom numerik
    numerical_columns = df.select_dtypes(include='number').columns.tolist()

    # Dropdown untuk memilih X dan Y axis
    x_col = st.selectbox("Pilih Kolom untuk Sumbu X", options=numerical_columns)
    y_col = st.selectbox("Pilih Kolom untuk Sumbu Y", options=numerical_columns)

    # Plot scatter
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax)
    ax.set_title(f'Scatter Plot: {x_col} vs {y_col}')
    ax.grid(True)

    # Tampilkan plot
    st.pyplot(fig)
    st.write("Faktor utama yang memengaruhi total transaksi dan keuntungan adalah kuantitas dan harga satuan, karena keduanya berkontribusi langsung ke dalam rumus total, pajak, dan pendapatan kotor.Rating pelanggan tidak memiliki hubungan langsung dengan nilai transaksi, harga, atau jumlah pembelian. Ini menunjukkan bahwa kepuasan pelanggan tidak hanya bergantung pada harga atau jumlah barang, tetapi bisa dipengaruhi oleh faktor lain seperti pelayanan, kualitas produk, atau pengalaman belanja.")

    



