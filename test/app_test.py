from app_logic import *

app = NetflixPicks()
'''app.select_options(app.question[0])
print(app.button1)
print(app.button2)
print(app.button3)
print(app.button4)
app.select_options(app.question[1])
print(app.button1)
print(app.button2)
print(app.button3)
print(app.button4)
app.select_options(app.question[2])
print(app.button1)
print(app.button2)
print(app.button3)
print(app.button4)'''
app.comunication[app.selected]=app.selection[1]
app.comunication[app.question[0]]=['comedy','war']
app.comunication[app.question[1]]=['G','NC-17','PG','PG-13','R','TV-14','TV-G','TV-MA','TV-PG','TV-Y7']
app.comunication[app.question[2]]=['MX', 'XX','US']
resultados = app.result()
print(resultados)
app.comunication[app.selected]=app.selection[0]
resultados = app.result()
print(resultados)