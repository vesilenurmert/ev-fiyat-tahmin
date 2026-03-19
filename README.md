# Ev Fiyat Tahmin Modeli

Python ve Scikit-learn kullanarak basit bir regresyon modeli ile ev fiyatlarını tahmin eden proje.

## Özellikler
- Kullanıcıdan **metrekare** ve **oda sayısı** bilgilerini alır
- Girilen bilgilere göre **tahmini fiyat**ı hesaplar
- Eğitim verisi örnek bir veri seti ile hazırlanmıştır
- Modelin performansı `mean_absolute_error` metriği ile değerlendirilebilir

## Kurulum
1. Python 3 yüklü olduğundan emin olun
2. Gerekli kütüphaneleri kurun:
 ```bash
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
```
4. `main.py` dosyasını çalıştırın:
 ```bash
python3 main.py
```
## Kullanım
Program çalışınca kullanıcıdan:
- Metrekare
- Oda sayısı  

Bilgileri istenir ve tahmini fiyat ekrana yazdırılır.


