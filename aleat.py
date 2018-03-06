#!/usr/bin/python3
"""
    Servidor URLs aleatorias nuevo
    Jaime Fernández Sánchez
"""

import webapp
import random

class aleatApp(webapp.webApp):

    def responder(self):
        respuesta = ("<p>Hola. <a href = http://localhost:4003/" 
            + str(self.random_url) + ">Dame Otra URL </a></p>")
        return respuesta

    def parse(self,request):
        if request.split()[1] == "/favicon.ico":
            return None
        else:
            return request.split()[1]
    def process(self,parsedRequest):
        if parsedRequest == None:
            return ("200 OK", "<html><body><h1>Vete!</h1></body></html>")

        self.random_url = random.randint(0,1000000)
        parsedRequest = self.responder();

        return ("200 OK","<html><body><title>URLs Aleatorias</title>"
        + "<h1>" + parsedRequest + "</h1></body></html>")

if __name__ == "__main__":
    testWebApp = aleatApp("localhost",4003)