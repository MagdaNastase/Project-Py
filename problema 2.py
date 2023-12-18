import pandas as pd
import matplotlib.pyplot as plt

# Citirea datelor din fisierul CSV
df = pd.read_csv('C:\\Users\\nasta\\OneDrive - Universitatea Politehnica Bucuresti\\Desktop\\PYTHON\\data.csv')


# Plotează toate valorile
plt.figure(figsize=(10, 5))
df.plot(title='Toate valorile')
plt.show()

# Plotează primele 7 valori
plt.figure(figsize=(10, 5))
df.head(7).plot(title='Primele 7 valori')
plt.show()

# Plotează ultimele 14 valori pentru coloanele Durata și Puls
plt.figure(figsize=(10, 5))
df[['Durata', 'Puls']].tail(14).plot(title='Ultimele 14 valori pentru Durata și Puls')
plt.show()
