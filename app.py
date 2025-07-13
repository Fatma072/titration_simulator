import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulator Titrasi")

st.title("🔬 Simulator Titrasi Asam-Basa")

# Input parameter
vol_asam = st.number_input("Volume Asam (mL)", min_value=1.0, value=25.0)
conc_asam = st.number_input("Konsentrasi Asam (M)", min_value=0.01, value=0.1)
conc_basa = st.number_input("Konsentrasi Basa (M)", min_value=0.01, value=0.1)

# Titik-titik volume basa ditambahkan
vol_basa = np.linspace(0, 2 * vol_asam, 100)
mol_asam = vol_asam * conc_asam / 1000
mol_basa = vol_basa * conc_basa / 1000

# Hitung pH (contoh sederhana untuk asam kuat vs basa kuat)
pH = np.where(
    mol_basa < mol_asam,
    -np.log10((mol_asam - mol_basa) / (vol_asam + vol_basa) * 1000),
    np.where(
        mol_basa == mol_asam,
        7,
        14 + np.log10((mol_basa - mol_asam) / (vol_asam + vol_basa) * 1000)
    )
)

# Tampilkan grafik
fig, ax = plt.subplots()
ax.plot(vol_basa, pH, color='blue')
ax.set_xlabel("Volume Basa Ditambahkan (mL)")
ax.set_ylabel("pH")
ax.set_title("Kurva Titrasi")
ax.grid(True)

st.pyplot(fig)
