import streamlit as st
import pandas as pd
import pickle

data =pickle.load(open(r'C:\To lenovo\Baramej_Courses\projects\python\017 Car Price Prediction Challenge/Cars_Predictions.sav','rb'))

#Streamlit Page
st.title('Car Price Prediction')
st.sidebar.header('Feature Selection')
st.sidebar.info('Easy Application For Car Price Predicting')
st.image(r'C:\To lenovo\Baramej_Courses\projects\python\017 Car Price Prediction Challenge\OIP.jpg', width=700)

m1 = ['LEXUS', 'CHEVROLET', 'HONDA', 'FORD', 'HYUNDAI', 'TOYOTA',
       'MERCEDES-BENZ', 'OPEL', 'PORSCHE', 'BMW', 'JEEP', 'VOLKSWAGEN',
       'AUDI', 'RENAULT', 'NISSAN', 'SUBARU', 'DAEWOO', 'KIA',
       'MITSUBISHI', 'SSANGYONG', 'MAZDA', 'GMC', 'FIAT', 'INFINITI',
       'ALFA ROMEO', 'SUZUKI', 'ACURA', 'LINCOLN', 'VAZ', 'GAZ',
       'CITROEN', 'LAND ROVER', 'MINI', 'DODGE', 'CHRYSLER', 'JAGUAR',
       'ISUZU', 'SKODA', 'DAIHATSU', 'BUICK', 'TESLA', 'CADILLAC',
       'PEUGEOT', 'BENTLEY', 'VOLVO', 'სხვა', 'HAVAL', 'HUMMER', 'SCION',
       'UAZ', 'MERCURY', 'ZAZ', 'ROVER', 'SEAT', 'LANCIA', 'MOSKVICH',
       'MASERATI', 'FERRARI', 'SAAB', 'LAMBORGHINI', 'ROLLS-ROYCE',
       'PONTIAC', 'SATURN', 'ASTON MARTIN', 'GREATWALL']


m2 = [16, 12, 17, 43, 27, 45, 35, 31,  6, 41,  9,  3, 21, 30, 40, 26, 14,
       11, 42, 24, 32,  2,  8, 29, 10, 20,  0, 44, 19, 39,  7, 25,  4, 33,
       47, 15, 23,  5, 38, 18, 34, 22, 28, 36, 46,  1, 37, 13]

manu_maping = dict(zip(m1, m2))

manu1= st.selectbox("Manufacturer", m1)
manu2 = manu_maping[manu1]

#---------------------------------------------------------
mm1 = ['RX 450', 'Equinox', 'FIT', ..., 'E 230 124', 'RX 450 F SPORT',
       'Prius C aqua']
mm2 = [890, 458, 477, 485, 833]
Model_mapping = dict(zip(mm1, mm2))
Model1 = st.selectbox('Model', mm1)
Model = Model_mapping[Model1]
#---------------------------------------------------------
c1 = ['Jeep', 'Hatchback', 'Sedan', 'Microbus', 'Goods wagon',
       'Universal', 'Coupe', 'Minivan', 'Cabriolet', 'Limousine',
       'Pickup']
c2 = [3, 4, 8, 9, 6, 0, 1, 5, 2, 7]
Category_mapping = dict(zip(c1, c2))
Category1 = st.selectbox('Category', c1)
Category = Category_mapping[Category1]
#---------------------------------------------------------
l1 = ['yes', 'no']
l2 = [1, 2]
leather_mapping = dict(zip(l1, l2))
leather1 = st.selectbox('Leather Interior', l1)
leather = leather_mapping[leather1]
#---------------------------------------------------------
f1 = ['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG','Hydrogen']
f2 = [2, 5, 1, 6, 4, 0, 3]
Fuel_mapping = dict(zip(f1, f2))
Fuel1 = st.selectbox('Fuel Type', f1)
Fuel = Fuel_mapping[Fuel1]
#---------------------------------------------------------
g1 = ['Automatic', 'Tiptronic', 'Variator', 'Manual']
g2 = [3, 0, 2, 1]
Gear_mapping = dict(zip(g1, g2))
Gear1 = st.selectbox('Gear Box Type', g1)
Gear = Gear_mapping[Gear1]
#---------------------------------------------------------
d1 = ['4x4', 'Front', 'Rear']
d2 = [0, 1, 2]
Drive_mapping = dict(zip(d1, d2))
Drive1 = st.selectbox('Drive wheels', d1)
Drive = Drive_mapping[Drive1]
#---------------------------------------------------------
w1 = ['Left wheel', 'Right-hand drive']
w2 = [0, 1]
Weel_mapping = dict(zip(w1, w2))
Weel1 = st.selectbox('Wheels', w1)
Weel = Weel_mapping[Weel1]
#---------------------------------------------------------
cc1 = ['Silver', 'Black', 'White', 'Grey', 'Blue', 'Green', 'Red',
       'Sky blue', 'Orange', 'Yellow', 'Brown', 'Golden', 'Beige',
       'Carnelian red', 'Purple', 'Pink']
cc2 = [12, 1, 14,  7,  2, 13, 11,  8, 6, 15,  3,  5,  0, 4, 10,  9]
color_mapping = dict(zip(cc1, cc2))
color1 = st.selectbox('Color', cc1)
color = color_mapping[color1]
#---------------------------------------------------------

Engine = st.selectbox('Engine volume',[1.3, 2.5, 2. , 1.8, 2.4, 1.6, 2.2, 1.5, 1.4, 2.3, 1.2, 1.7, 2.9,
       1.9, 3.5, 2.1, 2.7, 1. , 0.8, 3. , 3.3, 2.8, 3.2, 1.1])
#---------------------------------------------------------
Airbags = st.selectbox('Air Bag',[2,  0,  4, 12,  8, 10,  6,  1, 16,  7,  9,  5, 11,  3, 14, 15, 13])
#---------------------------------------------------------

Age  = st.number_input('Age')
#---------------------------------------------------------
Cylinders = st.selectbox('Cylinders',[1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 12, 14, 16])
#---------------------------------------------------------
Mileage  = st.number_input('Milage')
#---------------------------------------------------------
Levy = st.number_input('Levy')
#---------------------------------------------------------
# df = pd.DataFrame({'Manufacturer':manu2, 'Model': Model, 'Category': Category, 'Leather interior':leather, 'Fuel type':Fuel,
#               'Mileage': Mileage, 'Gear box type': Gear,'Cylinders': Cylinders, 'Drive wheels': Drive, 'Wheel': Weel, 'Color':color,
#               'Levy': Levy,'Engine volume': Engine, 'Airbags': Airbags, 'Age': Age}, index = [0])


df = pd.DataFrame({'Manufacturer': manu2, 'Model': Model, 'Category': Category, 'Leather interior':leather, 'Fuel type':Fuel,
       'Gear box type':Gear, 'Drive wheels':Drive, 'Wheel':Weel, 'Color':color, 'Levy':Levy,
       'Engine volume':Engine, 'Mileage':Mileage, 'Cylinders': Cylinders, 'Airbags':Airbags, 'Age':Age}, index = [0])

p = st.sidebar.button('Predict Price')
if p:
    pred  = data.predict(df)
    st.sidebar.write('Predicted Price is : ', pred, 'USD')

