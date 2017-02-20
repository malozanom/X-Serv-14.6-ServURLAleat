#!/usr/bin/python3

"""
Miguel Ángel Lozano Montero.
Programa que recrea el generador de URLs aleatorias
con un servidor orientado a objetos.
"""

import webapp
import random


class urlaleat(webapp.webApp):

    def process(self, parsedRequest):
        aleatorio = random.randrange(1000000000)
        return("200 OK", "<html><body><h1>Hola. <a href=http://localhost:" +
               "1234/" + str(aleatorio) + ">Dame otra</a></h1></body></html>")

if __name__ == "__main__":
    testWebApp = urlaleat("localhost", 1234)
