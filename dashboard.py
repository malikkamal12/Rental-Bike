import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data
# Assuming df is your DataFrame containing the bike rental data
# Replace this line with your data loading code
df = pd.read_csv("Bike-sharing-dataset/day.csv")

# Function to create the bar plot
def plot_bar(data, x_label, y_label, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=data.index, y=data.values, palette='viridis', ax=ax)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # Adding labels to the bars
    for i, value in enumerate(data.values):
        ax.text(i, value, str(round(value, 2)), ha='center', va='bottom')

    st.pyplot(fig)


def show_dashboard():
    st.header("Welcome to the Bike Rental Dashboard")
    st.write("This dashboard allows you to explore bike rental data.")
    st.write("Please select a page from the sidebar.")

    # Add dataset overview
    st.subheader("Dataset Overview:")
    st.write("This dataset consists of information about bike sharing rentals recorded over a period of two years. It includes various features such as date, weather conditions, and rental counts.")

    st.subheader("Data Structure:")
    st.write("- `instant`: Sequential unique identifier for each row.")
    st.write("- `dteday`: Date of the recorded data.")
    st.write("- `season`: Season 1; springer 2; summer 3; fall 4; winter")
    st.write("- `yr`: year (0: 2011, 1:2012)")
    st.write("- `mnth`: month (1 to 12)")
    st.write("- `hr`: hour (0 to 23)")
    st.write("- `holiday`: Binary feature indicating whether it's a holiday or not.")
    st.write("- `weekday`: Day of the week (0: Sunday, 1: Monday, ..., 6: Saturday).")
    st.write("- `workingday`: Binary feature indicating whether it's a working day or not.")
    st.write("- `weathersit`: Weather situation :")
    st.write("  - 1: Clear, Few clouds, Partly cloudy, Partly cloudy")
    st.write("  - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist")
    st.write("  - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds")
    st.write("  - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog")
    st.write("- `temp`: Normalized temperature in Celsius. The values are divided by 41 (max)")
    st.write("- `atemp`: Normalized feeling temperature in Celsius. The values are divided by 50 (max)")
    st.write("- `hum`: Normalized humidity. The values are divided by 100 (max)")
    st.write("- `windspeed`: Normalized wind speed. The values are divided by 67 (max)")
    st.write("- `casual`: count of casual users")
    st.write("- `registered`: count of registered users")
    st.write("- `cnt`: Total count of bike rentals (casual + registered).")


# Function to create the bar plot for average counts by season
def plot_season_counts(data, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=data.index, y=data.values, palette='viridis', ax=ax)
    ax.set_title(title)
    ax.set_xlabel('Season')
    ax.set_ylabel('Average Counts')

    # Adding labels to the bars
    for i, count in enumerate(data.values):
        ax.text(i, count, str(round(count, 2)), ha='center', va='bottom')

    st.pyplot(fig)

    

# Function to display the page for average counts by season
def show_season_counts():
    st.title('Average Counts of Users by Season')

    # Penjelasan musim
    st.write("Season:")
    st.write("1: Spring")
    st.write("2: Summer")
    st.write("3: Fall")
    st.write("4: Winter")
    
    user_type = st.sidebar.selectbox("Select User Type", ["Casual", "Registered"])

    if user_type == "Casual":
        data = df.groupby('season')['casual'].mean()
        plot_title = 'Average Counts of Casual Users by Season'

        # Create a bar plot for selected user type by season
        plot_season_counts(data, plot_title)

        # Penjelasan untuk pengguna biasa (casual user)
        st.subheader('Analisis Data untuk Pengguna Biasa (Casual User):')
        st.write("1.) **Perbandingan Jumlah Pengguna:**")
        st.write("Terdapat perbedaan signifikan antara jumlah pengguna yang terdaftar dan pengguna biasa, dengan pengguna terdaftar lebih dominan dalam jumlah.")
        st.write("2.) **Pola Aktivitas Penyewaan Berdasarkan Musim:**")
        st.write("Puncak aktivitas penyewaan sepeda terjadi pada musim gugur (season fall), diikuti oleh musim panas (season summer), musim dingin (season winter), dan terakhir musim semi (season spring).")
        st.write("Musim gugur menjadi yang paling diminati, diikuti oleh musim panas, musim dingin, dan musim semi.")
        st.write("3.) **Kesimpulan untuk Pengguna Biasa:**")
        st.write("Musim gugur (season fall) adalah waktu yang paling menguntungkan untuk bisnis penyewaan sepeda bagi pengguna biasa.")
        st.write("Meskipun musim panas juga menunjukkan tingkat penyewaan yang tinggi, musim gugur tetap menjadi pilihan utama bagi para penyewa sepeda.")
        st.write("Pengguna biasa cenderung aktif dalam menyewa sepeda pada musim-musim tertentu, dengan tingkat aktivitas tertinggi pada musim gugur.")

    elif user_type == "Registered":
        data = df.groupby('season')['registered'].mean()
        plot_title = 'Average Counts of Registered Users by Season'

        # Create a bar plot for selected user type by season
        plot_season_counts(data, plot_title)

        # Penjelasan untuk pengguna terdaftar (registered user)
        st.subheader('Analisis Data untuk Pengguna Terdaftar (Registered User):')
        st.write("1.) **Perbandingan Jumlah Pengguna:**")
        st.write("Terdapat perbedaan jumlah yang signifikan antara pengguna yang terdaftar dan pengguna biasa, dengan pengguna terdaftar lebih banyak daripada pengguna biasa.")
        st.write("2.) **Pola Aktivitas Penyewaan Berdasarkan Musim:**")
        st.write("Puncak aktivitas penyewaan sepeda terjadi pada musim gugur (season fall), diikuti oleh musim panas (season summer), musim dingin (season winter), dan terakhir musim semi (season spring).")
        st.write("Musim gugur menjadi yang paling diminati, diikuti oleh musim panas, musim dingin, dan musim semi.")
        st.write("3.) **Kesimpulan untuk Pengguna Terdaftar:**")
        st.write("Musim gugur (season fall) adalah waktu yang paling menguntungkan untuk bisnis penyewaan sepeda bagi pengguna terdaftar.")
        st.write("Pengguna terdaftar cenderung lebih aktif dalam menyewa sepeda secara reguler dibandingkan dengan pengguna biasa.")
        st.write("Meskipun musim panas juga menunjukkan tingkat penyewaan yang tinggi, musim gugur tetap menjadi pilihan utama bagi para penyewa sepeda terdaftar.")


    
    # Show raw data option
    if st.sidebar.checkbox('Show Raw Data'):
            st.subheader('Raw Data')
            st.write(df)


# Streamlit app
# Streamlit app
def main():
    st.sidebar.title('Navigation')
    page = st.sidebar.selectbox("Select a page", ["Dashboard", "Impact of Weather Conditions", "Average Counts of User"])

    if page == "Dashboard":
        show_dashboard()
    elif page == "Impact of Weather Conditions":
        st.title('Impact of Weather Conditions on Bike Rental Counts')

    # Penjelasan kondisi cuaca
        st.write("Weather conditions:")
        st.write("- 1: Clear, Few clouds, Partly cloudy, Partly cloudy")
        st.write("- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist")
        st.write("- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds")

        # Group by weather condition and calculate the average bike rental counts
        weather_counts = df.groupby('weathersit')['cnt'].mean()

        # Display the bar plot
        plot_bar(weather_counts, 'Weather Condition', 'Average Bike Rental Counts', 'Average Rental Counts by Weather Condition')

        # Berdasarkan analisis data yang dilakukan, dapat disimpulkan beberapa poin utama:
        st.subheader('Berdasarkan analisis data yang dilakukan, dapat disimpulkan beberapa poin utama:')
        st.write("1.) **Polanya Penyewaan Sepeda**:")
        st.write("- Pola penyewaan sepeda paling tinggi terjadi pada saat cuaca nomor 1, yang ditandai dengan kondisi 'Clear, Few clouds, Partly cloudy, Partly cloudy'.")
        st.write("- Cuaca nomor 2, dengan kondisi 'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist', menempati urutan kedua dalam jumlah penyewaan sepeda.")
        st.write("- Cuaca nomor 3, yang mencakup kondisi 'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds', memiliki tingkat penyewaan yang lebih rendah dibandingkan dengan yang lainnya.")

        st.write("2.) **Prioritas Penyewaan Sepeda**:")
        st.write("- Urutan prioritas penyewaan sepeda berdasarkan kondisi cuaca adalah cuaca nomor 1, diikuti oleh nomor 2, dan terakhir nomor 3.")
        st.write("- Kondisi cuaca yang paling menguntungkan untuk penyewaan sepeda adalah saat cuaca cerah dengan sedikit awan (cuaca nomor 1), diikuti oleh kondisi kabut dengan awan pecah-pecah (cuaca nomor 2).")

        st.write("3.) **Kesimpulan dan Rekomendasi**:")
        st.write("- Untuk mengoptimalkan bisnis penyewaan sepeda, fokus dapat diberikan pada saat-saat cuaca yang paling diminati oleh pelanggan, yaitu cuaca nomor 1 dan 2.")
        st.write("- Langkah-langkah strategis dapat diambil untuk meningkatkan pelayanan atau promosi khusus pada hari-hari dengan cuaca yang sesuai dengan preferensi pelanggan, yang pada akhirnya dapat meningkatkan jumlah penyewaan sepeda.")

        # Show raw data option
        if st.sidebar.checkbox('Show Raw Data', key="weather_raw_data"):
            st.subheader('Raw Data')
            st.write(df)

            
    elif page == "Average Counts of User":
        show_season_counts()

if __name__ == "__main__":
    main()
