import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#streamlit run app_de.py


st.title('Анализ изменения средней зарплаты Data Engeneers')

st.subheader('Полный датасет')
df = st.cache_data(pd.read_csv)('DataScience_salaries_2024.csv')
st.dataframe(df)

st.subheader('Определим самую часто встречающуюся профессию в датасете')
selected = df['job_title'].value_counts()
st.dataframe(selected)

st.subheader('Средняя зп Дата Инженеров 2020 - 2024 гг.')
table = pd.DataFrame(df[df['job_title']=='Data Engineer'].groupby('work_year')['salary_in_usd'].mean())
table.reset_index(inplace = True)
table['year'] = np.nan
for i in range(len(table['year'])):
    table['year'][i] = str(table['work_year'][i])
table.drop(['work_year'], axis = 'columns', inplace = True)
st.table(table)

st.subheader('Данные таблицы на графике')
fig, ax = plt.subplots()
ax.plot(table['year'], table['salary_in_usd'], marker = '.')
ax.set_title('Средняя зп Дата Инженеров 2020-2024 гг.')
plt.grid()
st.pyplot(fig)

st.markdown('Просто кнопочка:')
st.button("Click here")