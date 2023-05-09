import sqlite3

def main():
    crear_alumno(1,"juan","Perez")
    crear_alumno(2,"Lucia","Rojas")
    crear_alumno(3,"Alvaro","Soto")
    crear_alumno(4,"Lucian","Wenupan")
    crear_alumno(5,"Pedro","Gutierrez")
    crear_alumno(6,"Andres","Lavin")
    crear_alumno(7,"Roberto","Villa")
    crear_alumno(8,"Ignacio","Mayorca")

def main2():
    buscar_por_nombre("juan")

def crear_alumno(id,nombre,apellido):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()
    
    query = '''INSERT INTO alumnos(id,nombre,apellido) VALUES(?,?,?)'''
    cursor.execute(query,(id,nombre,apellido))

    conn.commit()

    cursor.close()
    conn.close()

def buscar_por_nombre(nombre):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM alumnos WHERE nombre='{nombre}'"
    rows = cursor.execute(query)
    for row in rows:
        print(row)
    
    cursor.close()
    conn.close()
    


if __name__ == '__main__':
    main2()
