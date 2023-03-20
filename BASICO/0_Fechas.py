#Dates?

from datetime import datetime
now = datetime.now()
def obtenerhora(now):
    hora=now.hour
    minuto=now.minute
    mes= now.month
    dia= now.day
    segundo = now.second
    timestamp = now.timestamp()

    dia_hoy=dict({"Mes":mes,
                "Dia":dia,
                "Hora":hora,
                "Minuto":minuto,
                "Segundo":segundo,
                "Timestamp":timestamp})
    
    print(dia_hoy.keys())
    print(dia_hoy.values())

#obtenerhora(now)

year_2023 = datetime(2023,1,1,3)
#print(year_2023)


from datetime import time  #fechas horas extraer campos de manera eficiente

#tiempo = date.fromisocalendar(2023,1,6)
tiempo_actual = time(00,30,10)
obtenerhoras=tiempo_actual.hour
obtenermin=tiempo_actual.minute
obtenersec=tiempo_actual.second
print(obtenerhoras)
print(obtenermin)
print(obtenersec)

from datetime import date

dia_actual = date.today()#(2023,4,29)
obteneryear=dia_actual.year
obtenermes=dia_actual.month
obtenerdia=dia_actual.day
print(f"{obtenerdia}/{obtenermes}/{obteneryear}")

dia_actual = date(2023,4,29)
print(f"{dia_actual.day}/{dia_actual.month}/{dia_actual.year}")

dia_actual = date(2023,4+1,29)
print(f"{dia_actual.day}/{dia_actual.month}/{dia_actual.year}")

year_2023 = datetime(2023,1,1)
print(year_2023 - now)
print(year_2023.date() - dia_actual)

print(year_2023.time())
print(tiempo_actual)

from datetime import timedelta

time_delta = timedelta

star_time_delta= time_delta(30,100,100,weeks=1)
end_time_delta= time_delta(60,100,100,weeks=1)
print(star_time_delta)
print(end_time_delta)
print(end_time_delta - star_time_delta)
print(end_time_delta + star_time_delta)


