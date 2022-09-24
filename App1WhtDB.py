#Importamos las 2 librerias a usar
import psycopg2
import os
#Declaramos la variable de las opciones del menu
op = 0
#Funcion para escribir datos en la db
def wrtDB():
    print("Introduzca un nombre:")
    name = input()
    print("Introduzca una edad:")
    age = input()
    conn = psycopg2.connect(dbname="app1", user="postgres", password="Noviembre226", host="localhost", port="5432")
    cur = conn.cursor()
    query = '''INSERT INTO personas(nombre, edad) VALUES (%s, %s)'''
    cur.execute(query, (name, age))
    conn.commit()
    conn.close()
    print("_________________________\n1.Volver a menu\n2.Salir\n_________________________")
    op = input()
    if op=="1":
        os.system("cls")
        main()
#Funcion para leer los datos de la db
def rdDB():
    conn = psycopg2.connect(dbname="app1", user="postgres", password="Noviembre226", host="localhost", port="5432")
    cur = conn.cursor()
    query = '''SELECT nombre, edad FROM personas'''
    cur.execute(query)
    row = cur.fetchall()
    print(row)
    conn.commit()
    conn.close()
    print("_________________________\n1.Volver a menu\n2.Salir\n_________________________")
    op = input()
    if op=="1":
        os.system("cls")
        main()
#Funcion principal de la app
def main():
    print("Elige la opcion a realizar: \n1.Ingresar datos a la DB\n2.Leer datos de la DB\n3.Salir\n_________________________")
    op = input()
    print("_________________________")
    if op=="1":
        wrtDB()
    elif op=="2":
        rdDB()
    else:
        print("Good Bye")
#Iniciamos la app
main()