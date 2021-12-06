import json
import pandas as pd
import zipfile
from tqdm.auto import tqdm

with zipfile.ZipFile('declaraciones.json.zip','r') as z:
  for filename in z.namelist():
    with z.open(filename) as f:
      data = f.read()
      d= json.loads(data)

rango = len(d)

vehiculos = pd.DataFrame()
adeudos = pd.DataFrame()
exp_laboral = pd.DataFrame()


print('Iniciando...')

"""for i in tqdm(range(rango)):
  data = pd.json_normalize(d[i]['declaracion']['situacionPatrimonial']['vehiculos']['vehiculo'])
  data['_id'] = d[i]['_id']['$oid']
  data['id'] = d[i]['id']
  vehiculos = vehiculos.append(data)
vehiculos.to_csv('Vehiculos.csv')"""

for i in tqdm(range(rango)):
  data = pd.json_normalize(d[0]['declaracion']['situacionPatrimonial']['adeudos']['adeudo'])
  data['_id'] = d[i]['_id']['$oid']
  data['id'] = d[i]['id']
  adeudos = adeudos.append(data)
adeudos.to_csv('Adeudos.csv')

for i in tqdm(range(rango)):
  data = pd.json_normalize(d[i]['declaracion']['situacionPatrimonial']['experienciaLaboral']['experiencia'])
  data['_id'] = d[i]['_id']['$oid']
  data['id'] = d[i]['id']
  exp_laboral = exp_laboral.append(data)
exp_laboral.to_csv('Experiencia_Laboral.csv')


ingresos_anuales_netos = pd.DataFrame()
estudios = pd.DataFrame()
bienes_inmuebles = pd.DataFrame()

for i in tqdm(range(rango)):
  data = pd.json_normalize(d[i]['declaracion']['situacionPatrimonial']['ingresos'])
  data['_id'] = d[i]['_id']['$oid']
  data['id'] = d[i]['id']
  ingresos_anuales_netos = ingresos_anuales_netos.append(data)
ingresos_anuales_netos.to_csv('Ingresos_Anuales.csv')

for i in tqdm(range(rango)):
  data = pd.json_normalize(d[i]['declaracion']['situacionPatrimonial']['datosCurricularesDeclarante']['escolaridad'])
  data['_id'] = d[i]['_id']['$oid']
  data['id'] = d[i]['id']
  estudios = estudios.append(data)
estudios.to_csv('Estudios.csv')

for i in tqdm(range(rango)):
  data = pd.json_normalize(d[i]['declaracion']['situacionPatrimonial']['bienesInmuebles']['bienInmueble'])
  data['_id'] = d[i]['_id']['$oid']
  data['id'] = d[i]['id']
  bienes_inmuebles = bienes_inmuebles.append(data)
bienes_inmuebles.to_csv('Bienes_Inmuebles.csv')
