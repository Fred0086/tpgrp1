from bokeh.plotting import figure,output_file,show
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool
import sqlite3
import mysql.connector 
import pandas as pd
from bokeh.models import NumeralTickFormatter
from bokeh.models import DatetimeTickFormatter
from bokeh.io import curdoc

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
# #print(dataframe)

# # create a ColumnDataSource by passing the dict
source = ColumnDataSource(data=df)
#y2 = pd.DataFrame(df,columns=['valeur'])*1.9
#print(y2)

# # create a plot using the ColumnDataSource's two columns
p = figure(title="Bitcoin Values",
        sizing_mode="stretch_both",    
        plot_width=900, 
        plot_height=800, 
        x_axis_label='Times (min) ', 
        y_axis_label='Bitcoin Values (euros) ',
        toolbar_location=None,
        tools=[HoverTool()],   
        tooltips=[("Time   ", "@id" ),
                  ("Bitcoin", "@valeur")]
        )
output_file("index.html")

curdoc().theme = 'night_sky'

p.title.align = 'center'
p.title.text_font_size = '15pt'
p.line(x='id',
        y='valeur',
        source=source)
p.circle(x='id', 
        y='valeur', 
        line_color="red", 
        line_width=2,
        source=source)


p.yaxis[0].formatter = NumeralTickFormatter(format="$0.00") 
p.xaxis[0].formatter = DatetimeTickFormatter(months="%b %Y")


p.background_fill_color = ('#2F2F2F')
p.outline_line_color = (0, 0, 255)
show(p)
