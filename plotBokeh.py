from bokeh.plotting import figure,output_file,show
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool
import sqlite3
import mysql.connector 
import pandas as pd
from bokeh.models import NumeralTickFormatter
from bokeh.models import DatetimeTickFormatter
from datetime import datetime

#récuperation des données 

# conn = mysql.connector.connect(host="localhost",user="tpgrp1",password="grp1", database="tpgrp1")
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM bitvalue")
# dataframe = pd.read_sql_query("SELECT * FROM bitvalue ", conn)
# conn.close()

#curseur = con.cursor() #Obj curseur permettant executer les commandes sql
con = sqlite3.connect("/home/znatysharone/cloned/tpgrp1/tpgr1.db")
cur= con.cursor()

# for line in cur.execute("SELECT * FROM bitvalue ;"):
#     print(line)

df = pd.read_sql_query("SELECT * FROM bitvalue ;", con)
# for i in df['date']:
        # df['date'=i/1000
# print(df)

for i in range(len(df)):
        df.iat[i,2]=datetime.fromtimestamp(df.iat[i,2])
        print(df.iat[i,2])

#df['date']= datetime.fromtimestamp(df['date'])

# # # create a ColumnDataSource by passing the dict
source = ColumnDataSource(data=df)

# # create a plot using the ColumnDataSource's two columns
p = figure(title="Bitcoin Values",
        sizing_mode="stretch_width",    
        plot_width=900, 
        plot_height=800, 
        x_axis_label='Times (min) ', 
        y_axis_label='Bitcoin Values (euros) ',
        toolbar_location=None,
        tools=[HoverTool()],   
        tooltips=[("Time   ", "@date" ),
                  ("Bitcoin", "@valeur")]
        )
output_file("index.html")
p.title.align = 'center'
p.title.text_font_size = '15pt'

DTF =  DatetimeTickFormatter()
DTF.hours = ["%H:%M"]
DTF.days = ["%d/%m/%Y"]
DTF.months = ["%d/%m/%Y"]
DTF.years = ["%d/%m/%Y"]
DTF.minutes = ["%m/%d %H:%M"]
p.xaxis[0].formatter = DTF

p.line(x='date',
        y='valeur',
        source=source)

p.circle(x='date', 
        y='valeur', 
        line_color="red", 
        line_width=2,
        source=source)

# add bands to the y-grid
p.ygrid.band_fill_color = "olive"
p.ygrid.band_fill_alpha = 0.1

DTF =  DatetimeTickFormatter()
#DTF.hours = ["%H:%M"]
# # DTF.days = ["%d/%m/%Y"]
# # DTF.months = ["%d/%m/%Y"]
# DTF.years = ["%d/%m/%Y"]
DTF.minutes = ["%m/%d %H:%M"]
# p.yaxis[0].formatter = NumeralTickFormatter(format="$0.00") 
p.xaxis[0].formatter = DTF



p.background_fill_color = ('#cccccc')
p.outline_line_color = (0, 0, 255)
show(p)








