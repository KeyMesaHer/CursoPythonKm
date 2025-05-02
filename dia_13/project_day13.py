""" 
Este modulo son las variables y funciones para la operación de un asistente vitual 
"""
import pyttsx3  # texto a voz
import speech_recognition as sr #voz a texto
import pywhatkit  # Automatización de acciones como buscar en YouTube o Google
import yfinance as yf  # Información financiera en Yahoo Finance
import pyjokes  # Chistes aleatorios en varios idiomas
import webbrowser  # Para abrir páginas web
import datetime  # Manejo de fechas y horas
import wikipedia  # Búsqueda de información en Wikipedia

# Identificadores de voces instaladas 
id1 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-MX_SABINA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0'
id3 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-ES_HELENA_11.0'  # Usada por el asistente
id4 = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0'

# Transforma el audio del micrófono en texto
def trasformar_audio_en_texto():
    r = sr.Recognizer()
    with sr.Microphone() as origen:
        r.pause_threshold = 0.8
        print("ya puedes hablar")
        audio = r.listen(origen)

        try:
            pedido = r.recognize_google(audio, language="es-ar")
            print("Dijiste: " + pedido)
            return pedido
        except sr.UnknownValueError:
            print("ups, no entendi")
            return "sigo esperando"
        except sr.RequestError:
            print("ups, no hay servicio")
            return "sigo esperando"
        except:
            print("ups, algo ha salido mal")
            return "sigo esperando"

# Permite que el asistente hable un mensaje en voz alta
def hablar(mensaje):
    engine = pyttsx3.init()
    engine.setProperty('voice', id3)  # Voz en español 
    engine.say(mensaje)
    engine.runAndWait()

# Informa qué día de la semana es hoy
def pedir_dia():
    dia = datetime.date.today()
    dia_semana = dia.weekday()
    calendario = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miércoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sábado',
        6: 'Domingo'
    }
    hablar(f'Hoy es {calendario[dia_semana]}')

# Informa la hora actual
def pedir_hora():
    hora = datetime.datetime.now()
    hora_str = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora_str)
    hablar(hora_str)

# Da un saludo inicial según la hora del día
def saludo_inicial():
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'
    hablar(f'{momento}, soy Helena, tu asistente personal. Por favor, dime en qué te puedo ayudar')

# Función que maneja los comandos del usuario
def pedir_cosas():
    saludo_inicial()
    comenzar = True

    while comenzar:
        pedido = trasformar_audio_en_texto().lower()
        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {
                'apple': 'AAPL',
                'amazon': 'AMZN',
                'google': 'GOOGL'
            }
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar("Perdón pero no la he encontrado")
                continue
        elif 'adiós' in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break

# Llamada a la función para iniciar el asistente
pedir_cosas()
