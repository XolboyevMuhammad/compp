# import streamlit as st
# import pandas as pd
# import pickle
# import numpy as np

# # Modelni yuklash
# model = pickle.load(open('computer_price_model.pkl', 'rb'))

# # Nominal o'zgaruvchilar uchun label encoding
# brand_mapping = {'Dell': 0, 'HP': 1, 'Lenovo': 2, 'Asus': 3, 'Acer': 4, 'Apple': 5}
# processor_mapping = {'Intel': 0, 'AMD': 1, 'Apple M1': 2, 'Intel Core i5': 3, 'Intel Core i7': 4}
# storage_type_mapping = {'SSD': 0, 'HDD': 1}
# graphics_card_mapping = {'Intel Integrated': 0, 'NVIDIA': 1, 'AMD Radeon': 2, 'None': 3}

# # Streamlit ilovasi
# st.title("Kompyuter Narxini Bashorat Qilish")

# # Foydalanuvchi uchun formalar
# brand = st.selectbox('Brendni tanlang', ['Dell', 'HP', 'Lenovo', 'Asus', 'Acer', 'Apple'])
# processor = st.selectbox('Protsessorni tanlang', ['Intel', 'AMD', 'Apple M1', 'Intel Core i5', 'Intel Core i7'])
# ram = st.slider('RAM hajmini tanlang (GB)', 4, 64, 8)
# storage = st.slider('Saqlash hajmini tanlang (GB)', 256, 2048, 512)
# storage_type = st.selectbox('Saqlash turi', ['SSD', 'HDD'])
# graphics_card = st.selectbox('Grafik kartani tanlang', ['Intel Integrated', 'NVIDIA', 'AMD Radeon', 'None'])
# screen_size = st.selectbox('Ekran o‘lchamini tanlang (dyuym)', [13, 15, 17])

# # Foydalanuvchi ma'lumotlarini raqamli formatga o'tkazish
# brand_encoded = brand_mapping[brand]
# processor_encoded = processor_mapping[processor]
# storage_type_encoded = storage_type_mapping[storage_type]
# graphics_card_encoded = graphics_card_mapping[graphics_card]

# # Input ma'lumotlarini modelga yuborish
# input_data = np.array([[brand_encoded, processor_encoded, ram, storage, storage_type_encoded, graphics_card_encoded, screen_size]])

# # Narxni bashorat qilish
# if st.button('Narxni bashorat qilish'):
#     predicted_price = model.predict(input_data)
#     st.write(f"Taxminiy narx: ${predicted_price[0]:.2f}")

import streamlit as st
import pandas as pd
import pickle
import numpy as np
import gzip

# Gzip yordamida modelni yuklash
with gzip.open('computer_price_model.pkl.gz', 'rb') as f:
    model = pickle.load(f)

# Nominal o'zgaruvchilar uchun label encoding  
brand_mapping = {'Dell': 0, 'HP': 1, 'Lenovo': 2, 'Asus': 3, 'Acer': 4, 'Apple': 5}
processor_mapping = {'Intel': 0, 'AMD': 1, 'Apple M1': 2, 'Intel Core i5': 3, 'Intel Core i7': 4}
storage_type_mapping = {'SSD': 0, 'HDD': 1}
graphics_card_mapping = {'Intel Integrated': 0, 'NVIDIA': 1, 'AMD Radeon': 2, 'None': 3}

# Streamlit ilovasi
st.title("Kompyuter Narxini Bashorat Qilish")

# Foydalanuvchi uchun formalar
brand = st.selectbox('Brendni tanlang', ['Dell', 'HP', 'Lenovo', 'Asus', 'Acer', 'Apple'])
processor = st.selectbox('Protsessorni tanlang', ['Intel', 'AMD', 'Apple M1', 'Intel Core i5', 'Intel Core i7'])
ram = st.slider('RAM hajmini tanlang (GB)', 4, 64, 8)
storage = st.slider('Saqlash hajmini tanlang (GB)', 256, 2048, 512)
storage_type = st.selectbox('Saqlash turi', ['SSD', 'HDD'])
graphics_card = st.selectbox('Grafik kartani tanlang', ['Intel Integrated', 'NVIDIA', 'AMD Radeon', 'None'])
screen_size = st.selectbox('Ekran o‘lchamini tanlang (dyuym)', [13, 15, 17])

# Foydalanuvchi ma'lumotlarini raqamli formatga o'tkazish
brand_encoded = brand_mapping[brand]
processor_encoded = processor_mapping[processor]
storage_type_encoded = storage_type_mapping[storage_type]
graphics_card_encoded = graphics_card_mapping[graphics_card]

# Input ma'lumotlarini modelga yuborish
input_data = np.array([[brand_encoded, processor_encoded, ram, storage, storage_type_encoded, graphics_card_encoded, screen_size]])

# Narxni bashorat qilish
if st.button('Narxni bashorat qilish'):
    predicted_price = model.predict(input_data)
    st.write(f"Taxminiy narx: ${predicted_price[0]:.2f}")
