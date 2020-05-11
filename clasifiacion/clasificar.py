import numpy as np
import matplotlib.pyplot as plt
import scipy
from sklearn.cluster import KMeans as km
import psycopg2
import pandas as pd


def calculo_k_means(X):
   clustering=km(n_clusters=3, n_init=20)
   clustering.fit(X.reshape(-1, 1) )
   color_theme=np.array(['darkgray', 'lightsalmon','powderblue'])
   t=np.linspace(0,len(X)-1,len(X) )
   plt.scatter(x=t,y=X , c=color_theme[clustering.labels_])
   plt.savefig("clasificación.png")


def getVoluntariados(pUsuario):
    try:
       connection = psycopg2.connect(user='beonguser',
                                      password='beong2020',
                                      host='beong-db.cq9blh97b4vq.us-east-1.rds.amazonaws.com',
                                      port='5432',
                                      database="beongDB")
       cursor = connection.cursor()
       usuarios_qr = "select * from usuarios_voluntario"
       gustos_qr = "select * from intereses_gusto"
       idiomas_qr = "select * from intereses_idioma"
       idiomas_usuarios_qr = "select * from usuarios_voluntario_idiomas"
       gustos_usuarios_qr = "select * from usuarios_voluntario_gustos"
       voluntariado_idiomas_qr = "select * from voluntariados_voluntariado_idiomasRequeridos"

       voluntariado_idiomas_usuarios_qr ='select us_id.voluntario_id, us_id.voluntariado_id from (select * from "voluntariados_voluntariado_idiomasRequeridos" INNER JOIN "usuarios_voluntario_idiomas" ON "usuarios_voluntario_idiomas".idioma_id="voluntariados_voluntariado_idiomasRequeridos".idioma_id)  as us_id' # where us_id.voluntario_id='+ pUsuario
       voluntariado_gustos_usuarios_qr ='select us_id.voluntario_id, us_id.voluntariado_id from (select * from "voluntariados_voluntariado_gustosRequeridos" INNER JOIN "usuarios_voluntario_gustos" ON "usuarios_voluntario_gustos".gusto_id="voluntariados_voluntariado_gustosRequeridos".gusto_id)  as us_id' # where us_id.voluntario_id='+ pUsuario
       voluntariados_qr = "select * from voluntariados_voluntariado"
       voluntariado_gustos_qr = 'SELECT * FROM "voluntariados_voluntariado_gustosRequeridos"'
       gustos_pusuario= "select * from usuarios_voluntario_idioma WHERE "


       cursor.execute(gustos_qr)
       gustos = cursor.fetchall()

       cursor.execute(gustos_usuarios_qr)
       gustos_usuarios = cursor.fetchall()

       cursor.execute(idiomas_qr)
       idiomas= cursor.fetchall()

       cursor.execute(idiomas_usuarios_qr)
       idiomas_usuarios = cursor.fetchall()
       #print(idiomas_usuarios)

       cursor.execute(voluntariado_gustos_usuarios_qr)
       voluntariado_gustos_usuarios =np.array(cursor.fetchall())

       cursor.execute(voluntariado_idiomas_usuarios_qr)
       voluntariado_idiomas_usuarios = np.array(cursor.fetchall())

       cursor.execute(voluntariados_qr)
       voluntariados = np.array(cursor.fetchall())

       nombre_gustos =[]

       #Almacena el id del de los gusto con el la posicon en el arreglo de nombres (id, pos)
       gustos_real=[]

       for row in gustos:
           if row[1] not in nombre_gustos:
                nombre_gustos.append(row[1])
                gustos_real.append([row[0],len(nombre_gustos) -1])
           else:
                gustos_real.append([row[0],nombre_gustos.index(row[1])])

      # print(gustos_real)
       nombre_idiomas = []
       idiomas_real = []
       for row in idiomas:
           if row[1] not in nombre_idiomas:
                nombre_idiomas.append(row[1])
                idiomas_real.append([row[0],len(nombre_idiomas) -1])
           else:
                idiomas_real.append([row[0],nombre_idiomas.index(row[1])])


       trabajar_tem = []
       for row in gustos_usuarios:
            pos=-1
            for i in gustos_real:
                if i[0]==row[2]:
                    pos=i[0]
                    break
            trabajar_tem.append([row[1],pos])
      # trabajar=pd.DataFrame(trabajar_tem)
       trabajar = np.array(trabajar_tem)

       trabajar_idi = []
       for row in idiomas_usuarios:
           pos = -1
           for i in idiomas_real:
               if i[0] == row[2]:
                   pos = i[0]
                   break
           trabajar_idi.append([row[1], pos])
       trabajar_fidi = pd.DataFrame(trabajar_idi)
       #print(trabajar_fidi)
       #print(pd.concat([trabajar, trabajar_fidi[1]], axis=1, sort=False))

       # Voluntariados para el voluntario dado. Ingnorando cantidad
       #print(trabajar[:,0]==usuario)

       #----------------------------------------------
       #calculo_k_means(trabajar[:,1])
       #----------------------------------------------


        ##buscamos los voluntariados que cumple con los idiomas.
       voluntarios_idiomas_pUsuarios=voluntariado_idiomas_usuarios[voluntariado_idiomas_usuarios[:,0]==pUsuario]
       voluntarios_gustos_pUsuarios = (voluntariado_gustos_usuarios[voluntariado_gustos_usuarios[:,0] == pUsuario])[:,1]

       voluntariados_finales = []
       for vol_id in voluntarios_idiomas_pUsuarios[:,1]:
           if vol_id in voluntarios_gustos_pUsuarios:
               voluntariados_finales.append(voluntariados[voluntariados[:,0]==int(vol_id)].tolist())

       return voluntariados_finales

    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)


