import pandas as pd
import matplotlib.pyplot as plt

# Excel dosyası okutalım
df = pd.read_excel("satis_temsilci.xlsx")

# Satış temsilcilerini gruplayarak toplam adetleri hesaplayalım
toplam_satis = df.groupby('Satış Temsilci')['Adet'].sum().reset_index()

# Pasta grafiği oluşturyoruz
plt.figure(figsize=(10, 6))
plt.pie(toplam_satis['Adet'], labels=toplam_satis['Satış Temsilci'], autopct=lambda p: f'{int(p * sum(toplam_satis["Adet"])/100)} Adet', startangle=140)
plt.axis('equal')  # Daire şeklinde görüntülemek için

# Başlığı biraz yukarıdan görüntülemek için
plt.title('Satış Temsilcilerine Göre Toplam Adet Dağılımı', y=1.1)

plt.show()