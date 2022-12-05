import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance
import pyjokes
import webbrowser
import datetime
import wikipedia


# escuchar nuestro micrófono y devolver el audio como texto
def transformar_audio_en_texto():
    # almacenar recognizer en una variable
    r = sr.Recognizer

    # configurar el micrófono
    with sr.Microphone() as origen:

        # tiempo de espera
        # r.pause_threshold = 0.8

        # infomar que comenzó la grabación
        print('Ya puedes hablar')

        # guardar lo que escuche como audio
        audio = r.listen(self=origen, source=origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-ES")

            # prueba de que pudo ingresar
            print('Dijiste: ' + pedido)

            # devolver pedido
            return pedido

        # en caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendió el audio
            print('Ups, no entendí')

            # devolver error
            return 'sigo esperando'

        # en caso de que no puede resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendió el audio
            print('Ups, hay servicio')

            # devolver error
            return 'sigo esperando'

        # error inexperado
        except:

            # prueba de que no comprendió el audio
            print('Ups, algo ha salido mal')

            # devolver error
            return 'sigo esperando'


transformar_audio_en_texto()
