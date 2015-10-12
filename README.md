# InMoovBrain (Español)
Una manera fácil de controlar tu InMoov

## Descripción

**InMoovBrain** es un aplicación hecha en Python para controlar el robot InMoov imprimible en impresoras 3D diseñado por Gael Langevin ([http://inmoov.fr](http://www.inmoov.fr)). Se conecta al Arduino para controlar los servos y sensores conectados al mismo y dispone de un interfaz Web que permite controlar las funcionalidades del robot. Para la comunicación del servidor con el Arduino se utiliza la librería MRLComm utilizada en el proyecto [MyRobotLab](http://www.myrobotlab.org) con algunas modificaciones.

## Características
* Control de todos los servos del InMoov
* Lbrería MRLCommExt para Arduino Mega compatible con MRLComm
* AutoDetach. Apaga los servos trás un periodo de inactividad
* ChatBot. Permite controlar el robot con lenguaje natural (funciones para controlar el movimiento del robot, Wikipedia, tiempo y respuestas a frases comúnes)
* Interfaz Web para su manejo

## Requisitos
Necesitarás lo siguiente para que funcione InMoovBrain:

* [Python 3.4.3](https://www.python.org/downloads/release/python-343/)
* [pyglet 1.2.3](https://bitbucket.org/pyglet/pyglet/wiki/Download)
* [AVbin 10](http://avbin.github.io/AVbin/Download.html)
* openssl para generar un certificado para la conexión SSL
* (opcional) Un IDE para python como [PyCharm](https://www.jetbrains.com/pycharm/download/) (o simplemente cualquier editor de texto)

¡Ah! Por supuesto necesitarás un robot InMoov montado y con todos los servos conectados a los Arduinos según la documentación de la [página oficial de InMoov](http://www.inmoov.fr).

## Instalación
Lo primero es tener Python 3 instalado y funcionando en tu sistema. A continuación instalar pyglet y AVbin. En el archivo _inmoovbrain.py_ se define el puerto y el nombre del host en el cual escuchará el servidor Web mediante las variable _hostPort_ y _hostName_ (por defecto localhost:8443); cambiala para adaptarla a tus necesidades.

Para que el servidor pueda atender peticiones por HTTPS hay que configurar un certificado. Para generar uno debes tener disponer de _openssl_ en tu sistema y ejecutar el siguiente comando:

```
openssl req -new -x509 -keyout localhost.pem -out localhost.pem -days 365 -nodes
```

## Configuración
Al arrancar el progrma se instancia un objeto llamado _myInMoov_ de la clase _InMoow_, Este objeto será el que se utilizará para gestionar tu robot. Antes de ejecutar el servidor Web, se llama al método _setup_ del módulo _main.py_ que debe contener la inicialización de dicho objeto, así como todas las operaciones que quieres que se ejecuten al arranque del servidor. Operaciones como inicialización del puerto serie al que está conectado el Arduino, asignación de pines a servos, definición de rango de funcionamiento de los servos, etc, son operaciones típicas que puedes incluir aqui. A continuación un ejemplo básico de inicialización del puerto serie y definición de los pines donde estarán conectados un par de servos:

```
def setup(myInMoov):
    if not myInMoov.init('/dev/tty.usbmodemfa141', 57600):
        print ("Error initializing serial port")
        return False
    myInMoov.head.neck.servoPin=12
    myInMoov.head.rotate.servoPin=13
    return True
```


## Arranque
Para arrancar el servidor basta con ejecutar el archivo _inmoovbrain.py_ ya sea desde línea de comandos o desde tu IDE favorito. 

```
MBPUgo:InMoovBrainServer Ugo$ python3 inmoovbrain.py
Running setup...
Starting server...
Server Starts - localhost:8443
```

Y ahora sólo queda conectarse a la consola Web para empezar a controlar tu InMoov. Abre en tu navegador la dirección [http://localhost:8443/console/inmoovconsole?lang=es-ES](http://localhost:8443/console/inmoovconsole?lang=es-ES) y a jugar!. 


## ¡No consigo hacer que esto funcione! 
Estamos ya trabajando en una aplicación standalone para que no tengas que configurar nada en tu sistema. Mientras tanto, si no consigues que esto funcione (o simplemente no tienes ganas de ponerte a instalar y configurar Python y todo lo demás) contacta conmigo indicando tu sistema operativo y te envio una versión standalone compilada para el mismo (y así haces de BetaTester de la aplicación!)

_________________
# InMoovBrain (English)
An easy way to control your InMoov

## Descripción

**InMoovBrain** is a Python application to control the printer 3D printable InMoov robot designed by Gael Langevin ([http://inmoov.fr](http://www.inmoov.fr)). It talks to the Arduinos to send command and control the servos and sensors connected to it. It uses the MRLComm library used in the project [MyRobotLab](http://www.myrobotlab.org) with some custom modifications.

## Features
* Control all th servos of your InMoov
* MRLCommExt library for Arduino Mega compatible with MRLComm
* AutoDetach. Shut down servos automatically after a period of inactivity
* ChatBot. Let you control your InMoov with voice commands and chat with it (basic commands to control the InMoov, Wikipedia and weather) (*) The 'grammar' file (_chatbot.xml_) is for Spanish, you have to translate it to your language
* Web user interface to control your InMoov

## Requirement
You would need to setup the following thing to work with InMoovBrain:

* [Python 3.4.3](https://www.python.org/downloads/release/python-343/)
* [pyglet 1.2.3](https://bitbucket.org/pyglet/pyglet/wiki/Download)
* [AVbin 10](http://avbin.github.io/AVbin/Download.html)
* openssl to create an SSL certificate
* (opcional) A Python IDE like [PyCharm](https://www.jetbrains.com/pycharm/download/) (or just a text editor)

¡Ah! Of course you need a InMov robot with all the servos connected to the Arduinos as written in the documentation of the [site of InMoov](http://www.inmoov.fr).

## Instalation
At first you have to install Python 3 in your computer, as well as pyglet y AVbin. In the _inmoovbrain.py_ you should set the host and port where the application would work using the variables _hostPort_ and _hostName_ (by default localhost:8443).

In order to work with SSL you should create a certificate with the following command:

```
openssl req -new -x509 -keyout localhost.pem -out localhost.pem -days 365 -nodes
```

## Setup
When the program starts, an instance of _InMoov_ class is created (called _myInMoov_). Then, the _setup_ method of the _main.py_ module is called in order to initialize all the object are needed to control the InMoov. Other operations you want to to at startup (like connection to the serial port) should be done here. There is an example of a basic initialization script:

```
def setup(myInMoov):
    if not myInMoov.init('/dev/tty.usbmodemfa141', 57600):
        print ("Error initializing serial port")
        return False
    myInMoov.head.neck.servoPin=12
    myInMoov.head.rotate.servoPin=13
    return True
```


## Run
To start the InMoovBrain you should execute the file _inmoovbrain.py_. 

```
MBPUgo:InMoovBrainServer Ugo$ python3 inmoovbrain.py
Running setup...
Starting server...
Server Starts - localhost:8443
```

After that you only have to open the user interface by pointing your web browser to the URL [http://localhost:8443/console/inmoovconsole?lang=en-US](http://localhost:8443/console/inmoovconsole?lang=en-US), and you are ready to play!. 


## I can't get this to work! 
We are working in a standalone application in order you don't need to installa anything in your system. While we release this app, if you can't get this to work (or simply you don't feel like installing and configuring Python and other libreries) email me and I would try to send you a standalone app for your operating system (tha way you could also help me betatesting the app!)