import numpy as np
import matplotlib.pyplot as plt

# ID
print ("Nama : Muhammad Fahmi Ramadhan")
print ("NRP  : 5009211007")


# Fungsi untuk menghaluskan data suhu dengan filter rata-rata sederhana
def simple_moving_average(data, window_size):
    smoothed_data = np.convolve(data, np.ones(window_size)/window_size, mode='valid')
    return smoothed_data

# Membuat data suhu acak untuk simulasi
np.random.seed(0)
num_samples = 250
mean_temp = 25
temp_variation = 5
temperature_data = mean_temp + temp_variation * np.random.randn(num_samples)

# Parameter filter rata-rata
window_size = 10  # Ukuran jendela filter

# Menghaluskan data suhu menggunakan filter rata-rata
smoothed_data = simple_moving_average(temperature_data, window_size)

# Plot data suhu asli dan hasil smoothing
plt.figure(figsize=(12, 6))
plt.plot(temperature_data, marker='o', linestyle='-', color='b', label='Suhu Asli')
plt.plot(smoothed_data, marker='x', linestyle='-', color='r', label='Suhu Setelah Filtering')
plt.xlabel('Waktu (Sekon)')
plt.ylabel('Suhu (°C)')
plt.title('Data Suhu dengan Filtering Rata-rata')
plt.grid(True)
plt.legend()
plt.show()