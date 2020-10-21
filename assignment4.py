import streamlit as st
import pandas as pd
import altair as alt

st.title("Gender equality")


st.header("Gender equality")

df = pd.read_csv("genderTransformed.csv", sep=',', header=0)


# a lot of missing data so will start from 1990
is_selected =  df['Year']>=1990
df = df[is_selected]

'''
The chart will show how that gender gap indicator has changed throught the years for the chosen country.

'''
   
df = df.sort_values(by=['Country Name'])
countries = df['Country Name'].unique()


country3 = st.selectbox('Choose country',countries)
indicators = ['Gender Gap Labor force participation % (15+age)','Gender Gap Part time employment %','Gender Gap Self-employed %','Gender Gap Unemployment %','Gender Gap Vulnerable employment %','Gender Gap Wage and salaried workers %']
indicator = st.selectbox('Choose Indicator',indicators)



if st.button("Show chart 1"):
    is_selected =  df['Country Name']==country3
    df_selected = df[is_selected]
    df1 = df_selected[['Year', indicator]]
    
    y = indicator.split("%")
    chart3 = alt.Chart(df1).mark_area().encode(
    alt.X('Year:N'),
	alt.Y(indicator+":Q"),
    ).properties(
        title={
            "text": [indicator + " for "+ country3], 
            "subtitle": ["Diferece male - female for this indicator"]
    }
    )
    chart3.encoding.y.title = y[0]
    st.altair_chart(chart3)
    
   
"""
The chart shows the difference between males and females for each indicator, given a country and specific year.
"""

country2 = st.selectbox('Country Name',countries)
df = df.sort_values(by=['Year'])
year = df['Year'].unique()
year2 = st.selectbox('Year',year)
    
if st.button("Show chart 2"):
    is_selected =  df['Country Name']==country2
    df_selected = df[is_selected]
    is_selected2 =  df_selected['Year']==year2
    df_selected2 = df_selected[is_selected2]
    df_selected2 = df_selected2.drop(['Country Name'], axis = 1) 
    df_selected2 = df_selected2.drop(['Country Code'], axis = 1) 
    df_selected2 = df_selected2.drop(['Year'], axis = 1) 
    df_selected2 = df_selected2.transpose()
    df_selected2.columns = ['Gap Gender Indicator']
    df_selected2.reset_index(inplace=True)

    chart = alt.Chart(df_selected2).mark_bar().encode(
	alt.X('index:N',sort='-y'),
	alt.Y('Gap Gender Indicator:Q'),
    alt.Color('index:N')
    ).properties(
        width=500,
        height=500,
         title={
            "text": ['Gender Gap indicators for '+country2], 
            "subtitle": ["Each indicator as diferece male - female for this indicator"]
    }
    )
    st.altair_chart(chart)
