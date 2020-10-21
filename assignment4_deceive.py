import streamlit as st
import pandas as pd
import altair as alt

st.title("Gender equality")


st.header("Gender equality")

df = pd.read_csv("genderTransformed.csv", sep=',', header=0)


# a lot of missing data so will start from 1990
is_selected =  df['Year']>=1990
df = df[is_selected]

 
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
    
    # lets try to deceive by increasing the domain of Y axis, so the gap looks smaller and changes smoother throught the years
    chart3_deceive = alt.Chart(df1).mark_area().encode(
    alt.X('Year:N'),
	alt.Y(indicator+":Q",scale=alt.Scale(domain=(-100, 100))),
    ).properties(
        title={
            "text": [indicator + " for "+ country3]
    }
    )
    chart3_deceive.encoding.y.title = y[0]
    st.altair_chart(chart3_deceive)



country = st.selectbox('Country',countries)
if st.button("Show chart 3"):
    is_selected =  df['Country Name']==country
    df_selected = df[is_selected]

    base = alt.Chart(df_selected.reset_index()).encode(x='Year').properties(
        title='Gender Equality indicators for '+country
    )
    
    chart = alt.layer(
        base.mark_line(color='red').encode(y='Gender Gap Part time employment %'),
        base.mark_line(color='orange').encode(y='Gender Gap Self-employed %'),
        base.mark_line(color='green').encode(y='Gender Gap Unemployment %'),
        base.mark_line(color='purple').encode(y='Gender Gap Vulnerable employment %'),
        base.mark_line(color='pink').encode(y='Gender Gap Wage and salaried workers %')
    )
    chart.layer[0].encoding.y.title = 'Gender Gap'
    st.write(chart)
    

    

 



