# HS100 TP-Link

## Scripts útiles

Un puñado de scripts para prender y apagar un dispositivo HS100 de la marca TP-Link.

Se utilizó como entorno de ejecución Python 3.7.5

Antes de comenzar deben configurar los scripts cambiando la direccion de IP por
la que figure en su WAN

Se usó Nmap para encontrar el rango del dispositivo.

```
nmap -sP 192.168.0.1-100
```

---

app_hs100 v1.2

Aplicacion en desarrollo en Python3 con Ttkinder(GUI) para el dispisitivo HS100
de TP-Link

## Funcionalidades
* Apagar y Prender el dispositivo.

## Colaboradores:

* [Garcia J Hernan](https://github.com/C0Y4)
* [Valentin Baez](https://github.com/ValentinBaez)
* [asoster](https://github.com/asoster)


## Instalación

Es necesario instalar un entorno virtual para ejecutar correctamente el módulo
de Python.

```
python -m virtualenv venv
```

Este proceso es necesario ejecutarlo en una sola oportunidad.

Luego debemos activar el entorno con el comando:

```
source venv/bin/activate
```

Finalmente, necesitamos instalar las dependencias del proyecto:

```
pip install -r requeriments.txt
```

## Configuración

Dentro del archivo de configuracion `config.yaml` deberá cambiar las siguientes
opciones:

```
ip: IP_DEL_EQUIPO
port: NRO_DE_PUERTO
```

### Uso en pruebas

Lanzamos con python un servidor web:
```
python -m http.server --bind 127.0.0.1 9999
```

En otra terminal, probamos enviar datos con:
```
python -m hs100 start config.yaml

python -m hs100 stop config.yaml
```

Veremos los datos recibidos en la terminal del servidor web de pruebas.

### Uso en producción

Debemos tener configurada la opción `debug`:
```
debug: false
```
