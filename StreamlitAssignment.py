import streamlit as st
import pandas as pd
import plotly.express as px
import chart_studio.plotly as py

st.title("Analysis of the Unemployment Rate in Saudi Arabia by Lara Baltaji")

df = pd.read_csv("Unemployment Rates by Education in Saudi Arabia.csv")
st.write("The following dataset was taken from **_Kaggle_**, an online data science platform that provides free-to-download datasets, data science courses, codes and much more. It shows **the unemployment rates per education level, nationality and gender in Saudi Arabia**. The data was collected from 18 different files from the first quarter of 2017 till the second quarter of 2021. The main source is **_GASTAT_**.")
st.write("The dataset's dimensions are as follows: **504 rows x 5 columns**")
st.write(df)
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='Unemployment Rates in Saudi Arabia.csv',
    mime='text/csv',
)

st.write("In order to better understand our data, we plotted a couple of data visualizations of different chart types.")

with st.sidebar:
    st.write("**We have created a couple of data visualizations in order to better understand  our data.**")
    

select = st.sidebar.selectbox('Select the chart type', ['Bar', 'Stacked Bar','Line','Box Plot'])
with st.sidebar:
    st.write("**_Scroll down to view the charts._**")

if select == 'Bar':
    #1 Plotting a bar graph that shows the unemployment rate by gender
    df_by_gender= df.groupby(["Gender"], as_index = False)["Unemployment Rate"].mean()
    st.header("Bar Graph Showing the Average of Unemployment Rate by Gender ")
    fig = px.bar(df_by_gender, x="Gender", y="Unemployment Rate", color = "Gender", color_discrete_sequence=["deeppink", "darkblue"])
    fig.update_layout(showlegend=False) 
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("See explanation"):
        st.write("The bar chart shows a huge unemployment gender gap in Saudi Arabia where the unemployment rate for women was more than four times that of men between 2017 Q1 and 2021 Q2. This is probably due to the great gender segregation and inquality in Saudi Arabia which was present in the duration between the first quarter of 2017 and the second quarter of 2021.")

    
    if st.checkbox('Show the grouped data by gender'):
        st.subheader('Grouped Data by Gender')
        st.write(df_by_gender)
    
    #2 Plotting a bar graph that shows the unemployment rate by nationality
    df_by_nationality= df.groupby(["Nationality"], as_index = False)["Unemployment Rate"].mean()
    st.header("Bar Graph Showing the Average of Unemployment Rate by Nationality")
    fig = px.bar(df_by_nationality, x="Nationality", y="Unemployment Rate", color = "Nationality", color_discrete_sequence=["red", "green"])
    fig.update_layout(showlegend=False) 
    st.plotly_chart(fig, use_container_width=True)
    with st.expander("See explanation"):
        st.write("This bar chart shows a huge unemployment gap between Saudis and non-Saudis. This is probably due to the fact that the majority of non-Saudis go to Saudi Arabia to work.")
    
    if st.checkbox('Show the grouped data by nationality'):
        st.subheader('Grouped Data by Nationality')
        st.write(df_by_nationality)
    
    #3 Plotting a bar graph that shows the unemployment rate by degree level
    df_by_degree= df.groupby(["Degree Level"], as_index = False)["Unemployment Rate"].mean()
    st.header("Bar Graph Showing the Average of Unemployment Rate by Degree Level ")
    fig = px.bar(df_by_degree, x="Degree Level", y="Unemployment Rate", color = "Degree Level")
    fig.update_xaxes(categoryorder = 'array', categoryarray = ["Primary","Intermediate", "Secondary", "Bachelor", "Diploma", "Master", "Doctorate"])
    fig.update_layout(showlegend=False) 
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("See explanation"):
        st.write("This maximum unemployment rate was for citizens with a secondary degree level and the minimum was for citizens with a doctorate. Primary and Intermediate level citizens, which consistent a small portion of the population, have probably dropped out of school to work. This graph shows that in Saudi Arabia, having a Bachelor's Degree does not necessarily mean that one will find a job easily. An additional Diploma or a Master's Degree can increase the chances of finding a job.")
    
    if st.checkbox('Show the grouped data by degree level'):
        st.subheader('Grouped Data by Degree Level')
        st.write(df_by_degree)

    #4 Plotting a bar graph that shows the unemployment rate by degree level for every year quarter
    st.header("Interactive Bar Graph Showing the Change in the Sum of Unemployment Rate by Degree Level Over Time")
    fig = px.bar(df, x = 'Degree Level', y = 'Unemployment Rate', animation_frame= 'Year Quarter', color = 'Degree Level', range_y=[0,80])
    fig.update_xaxes(categoryorder = 'array', categoryarray = ["Primary","Intermediate", "Secondary", "Bachelor", "Diploma", "Master", "Doctorate"])
    fig.update_layout(showlegend=False) 
    st.plotly_chart(fig, use_container_width=True)

elif select == 'Line':
    #5 Plotting a line plot that shows the average unemployment rate
    st.header("Line Graph Showing the Unemployment Rate Between 2017 Q1 and 2021 Q2")
    df_by_year = df.groupby(['Year Quarter'], as_index = False)["Unemployment Rate"].mean()
    fig = px.line(df_by_year, x = "Year Quarter", y = "Unemployment Rate", color_discrete_sequence=["red"])
    fig.update_xaxes(tickangle = 30)
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("See explanation"):
        st.write("The line graph shows a fluctation of the unemployment rates between 2017 Q1 and 2021 Q2, where the average unemployment rate reaches a trough in the first quarter of 2020. Then the rate dramatically increases till it reaches a peak in the second quarter of 2020 (Peak of COVID-19). This peak is expectedly due to the COVID-19 pandemic, and its catastrophic effect on the economy. ")
    
    if st.checkbox('Show the grouped data between 2017 Q1 and 2021 Q2'):
        st.subheader('Grouped Data Between 2017 Q1 and 2021 Q2')
        st.write(df_by_year)

    #6 Plotting a line plot that shows the average unemployment rate by gender
    st.header("Line Graph Showing the Average of Unemployment Rate by Gender Between 2017 Q1 and 2021 Q2")
    df_by_year_gender = df.groupby(['Gender','Year Quarter'], as_index = False)["Unemployment Rate"].mean()
    fig = px.line(df_by_year_gender, x = "Year Quarter", y = "Unemployment Rate", color = "Gender", color_discrete_sequence=["deeppink", "darkblue"])
    fig.update_xaxes(tickangle = 30)
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("See explanation"):
        st.write("The unemployment gap between males and females has been huge since the first quarter of 2017. However, we can notice a considerable decrease for women just before and after the peak of the COVID-19 pandemic, precisely in the first quarter of 2020 and the first quarter of 2021. This sudden decrease is explained by King Salman and Prince Mohammad's new agenda which empowers women in Saudi Arabia in many different aspects. ")
    
    if st.checkbox('Show the grouped data by gender between 2017 Q1 and 2021 Q2'):
        st.subheader('Grouped Data by Gender Between 2017 Q1 and 2021 Q2')
        st.write(df_by_year_gender)

    #7 Plotting a line plot that shows the average unemployment rate by nationality
    st.header("Line Graph Showing the Average of Unemployment Rate by Nationality Between 2017 Q1 and 2021 Q2")
    df_by_year_nationality = df.groupby(['Nationality','Year Quarter'], as_index = False)["Unemployment Rate"].mean()
    fig = px.line(df_by_year_nationality, x = "Year Quarter", y = "Unemployment Rate", color = "Nationality", color_discrete_sequence=["red", "green"], category_orders={"Nationality": ['Saudi', 'NonSaudi']})
    fig.update_xaxes(tickangle = 30)
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("See explanation"):
        st.write("The unemployment gap between Saudi and non-Saudi citizens has also been huge since the first quarter of 2017. We can notice that the rate has increased for both between first and second quarter of 2020, just by the start of the COVID-19 pandemic. This increase, however, was much steeper for non-Saudis who have lost their jobs and faced strict restrictions because of the socio-economic impact of the coronavirus.")
    
    if st.checkbox('Show the grouped data by nationality between 2017 Q1 and 2021 Q2'):
        st.subheader('Grouped Data by Nationality Between 2017 Q1 and 2021 Q2')
        st.write(df_by_year_nationality)
    
    #8 Plotting a line plot that shows the average unemployment rate by degree level
    st.header("Line Graph Showing the Average of Unemployment Rate by Degree Level Between 2017 Q1 and 2021 Q2")
    df_by_year_degree = df.groupby(['Degree Level','Year Quarter'], as_index = False)["Unemployment Rate"].mean()
    fig = px.line(df_by_year_degree, x = "Year Quarter", y = "Unemployment Rate", color = "Degree Level", category_orders={"Degree Level": ["Primary","Intermediate", "Secondary", "Bachelor", "Diploma", "Master", "Doctorate"]})
    fig.update_xaxes(tickangle = 30)
    st.plotly_chart(fig, use_container_width=True)
    if st.checkbox('Show the grouped data by degree level between 2017 Q1 and 2021 Q2'):
        st.subheader('Grouped Data by Degree Level Between 2017 Q1 and 2021 Q2')
        st.write(df_by_year_degree)
elif select == 'Stacked Bar':
    #9 Plotting a stacked bar plot that shows the unemployment rate by degree level and gender
    st.header("Bar Graph Showing the Average of Unemployment Rate by Degree Level  and Gender")
    df_by_degree_gender= df.groupby(['Gender','Degree Level'], as_index = False)["Unemployment Rate"].mean()
    fig = px.bar(df_by_degree_gender, x="Degree Level", y="Unemployment Rate", color="Gender", color_discrete_sequence=["deeppink", "darkblue"])
    fig.update_xaxes(categoryorder = 'array', categoryarray = ["Primary","Intermediate", "Secondary", "Bachelor", "Diploma", "Master", "Doctorate"])
    st.plotly_chart(fig, use_container_width=True)
    if st.checkbox('Show the grouped data by degree level and gender'):
        st.subheader('Grouped Data by Degree Level and Gender')
        st.write(df_by_degree_gender)

    #10 Plotting a stacked bar graph that shows the unemployment rate by degree Level over time
    st.header("Bar Graph Showing the Average of Unemployment Rate by Degree Level Between 2017 Q1 and 2021 Q2")
    df_by_degree_year= df.groupby(['Degree Level', 'Year Quarter'], as_index = False)["Unemployment Rate"].mean()
    fig = px.bar(df_by_degree_year, x="Year Quarter", y="Unemployment Rate", color="Degree Level", category_orders={"Degree Level": ["Primary","Intermediate", "Secondary", "Bachelor", "Diploma", "Master", "Doctorate"]})
    fig.update_xaxes(tickangle = 30)
    st.plotly_chart(fig, use_container_width=True)
    if st.checkbox('Show the grouped data by degree level between 2017 Q1 and 2021 Q2'):
        st.subheader('Grouped Data by Degree Level Between 2017 Q1 and 2021 Q2')
        st.write(df_by_degree_year)

else:
    #11 Plotting a box plot for the unemployment rate
    st.header("Box Plot of the Unemployment Rate")
    fig = px.box(df, y = "Unemployment Rate")
    st.plotly_chart(fig, use_container_width=True)

    #12 Plotting a box plot for the unemployment rate by nationality
    st.header("Box Plot of the Unemployment Rate by Nationality")
    fig = px.box(df, x="Nationality", y = "Unemployment Rate",color = 'Nationality', notched = True, color_discrete_sequence=["red", "green"])
    fig.update_layout(showlegend=False) 
    st.plotly_chart(fig, use_container_width=True)

    #13 Plotting a box plot for the unemployment rate by gender
    st.header("Box Plot of the Unemployment Rate by Gender")
    fig = px.box(df, x="Gender", y = "Unemployment Rate", color = "Gender", color_discrete_sequence=["deeppink", "darkblue"], notched = True)
    fig.update_layout(showlegend=False) 
    st.plotly_chart(fig, use_container_width=True)

    #14 Plotting a box plot for the unemployment rate by nationality and gender
    st.header("Box Plot of the Unemployment Rate by Nationality and Gender")
    fig = px.box(df, x="Nationality", y = "Unemployment Rate", color = "Gender", color_discrete_sequence=["deeppink", "darkblue"], notched = True)
    st.plotly_chart(fig, use_container_width=True)
