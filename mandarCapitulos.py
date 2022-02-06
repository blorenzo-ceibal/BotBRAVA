import numpy as np
from random import seed
from random import randint
import requests
import json

seed(1)

#Referencia Crear bot : https://atareao.es/tutorial/crea-tu-propio-bot-para-telegram/bot-en-python-para-telegram/
#Datos del bot
#  t.me/testBRAVAbot
#  Nombre: testBRAVAbot
#  Token: 5288631989:AAFAsj8eMXuzlZt-qxINslDqpdEPns62gCs
#  For a description of the Bot API, see this page: https://core.telegram.org/bots/api

#  ID Brian Telegram:   1570464576
#  LEDi ID Telegram:    -1001354886396
#Listado de todos los usuarios (lista de objetos "usuario")
usuarios = []

TOKEN_BRAVAbot = '5288631989:AAFAsj8eMXuzlZt-qxINslDqpdEPns62gCs'
ID_LEDI = '-1001354886396'

class usuario: 
    ID = ''
    capituloActual = ''

    def getID(usuario):
        ID_encontrada = randint(0,100)
        usuario.ID = ID_encontrada
        return usuario.ID

def eliminarUltimo(listUsers):
    if len(listUsers) > 0:
        listUsers.remove(listUsers[0])
    else:
        print("No hay usuarios para eliminar")
        print("La lista de usuarios está vacía")

def eliminarUsuario(usuario):
    if usuario in usuarios:
        if len(usuarios) > 0:
            usuarios.remove(usuario)
        else:
            print("No hay usuarios para eliminar")
            print("La lista de usuarios está vacía")
    else:
        print("El usuario indicado no se encuentra en la lista")

def nuevo(listUsers): 
        listUsers = [usuario()] + listUsers
        listUsers[0].getID()
        listUsers[0].capituloActual = 0     #Arranca en capítulo 0 por defecto
        print("Nuevo usuario creado")
        return listUsers


requests.post('https://api.telegram.org/bot' + TOKEN_BRAVAbot  + '/sendMessage', data={'chat_id': ID_LEDI, 'text': 'test 2'})

#requests.post('https://api.telegram.org/bot<TOKEN>/sendMessage',
#              data={'chat_id': '<CHAT_ID>', 'text': '<TEXTO>'})
#updates = requests.post('https://api.telegram.org/bot' + TOKEN_BRAVAbot '/getUpdates' )