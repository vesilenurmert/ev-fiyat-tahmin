
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

#veri
data = {
    "metrekare": [50, 60, 80, 100, 120],
    "oda_sayisi": [1, 2, 2, 3, 3],
    "fiyat": [150000, 180000, 250000, 300000, 350000]
}

df = pd.DataFrame(data)

#X ve y
X = df[["metrekare", "oda_sayisi"]]
y = df["fiyat"]

#bölme
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#model
model = LinearRegression()
model.fit(X_train, y_train)

#tahmin ve hata
y_pred = model.predict(X_test)
print("Hata:", mean_absolute_error(y_test, y_pred))

#grafik
plt.scatter(y_test, y_pred)
plt.xlabel("Gerçek Fiyat")
plt.ylabel("Tahmin Edilen Fiyat")
plt.title("Gerçek vs Tahmin Fiyat")
plt.show()

#kullanıcıdan veri alma
m2 = int(input("Metrekare: "))
oda = int(input("Oda sayısı: "))

tahmin = model.predict([[m2, oda]])
print("Tahmini fiyat:", tahmin[0])