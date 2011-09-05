#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       gcc-robot.py
#
#       Copyright 2009 Evaldo Junior (InFog) <junior@casoft.info>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import datetime
import smtplib
import sys

def enviar_email(dias=0) :
    servidor = smtplib.SMTP('localhost')
    de = 'robo-gccsd@gccsd.com.br'
    para = 'gccsd@lista.gccsd.com.br'
    mensagem = """
	To: gccsd@lista.gccsd.com.br
	From: robo-gccsd@gccsd.com.br

	Subject: Reunião do GCCSD em %s dias!

	Olá, participantes do GCC-SD!

	Este e-mail é para informar que em %s dias haverá a reunião mensal do
	Grupo de Compartilhamento do Conhecimento Santos Dumont.

	Te espero lá!

	Um abraço do amável e paranóico robô do GCC-SD.
    """ % (str(days), str(days))
    
    servidor.sendmail(de, para, mensagem)


if (__name__ == '__main__'):
    # Que é hoje?
    hoje = datetime.date.today()
    i = 2
    while i <= 5 :
        # Tem algum sábado nos próximos 2 a 5 dias?
        if (hoje + datetime.timedelta(days=i)).weekday() == 5 :
            # Eita, tem sábado sim! Será que é o primeiro do mês?
            if (hoje + datetime.timedelta(days=i)).day <= 7 :
                # É o primeiro sábado do mês! Bora mandar e-mail pras galera
                enviar_email(dias=i)
        i += 1
    sys.exit(0)
