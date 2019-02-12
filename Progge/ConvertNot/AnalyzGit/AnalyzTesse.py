# tests pour comprendre approche
from AnalyzNotElem import *
from time import sleep
import re


class AnalyseUn:
    def __init__(self, ba_ze=0, n_ba_ze=''):
        self._ba_ze = 0
        self.n_ba_ze = ''

    def gonott(self):
        ba = int(input('Votre premiere note: '))
        moddouz = lambda a : a % 12
        self._ba_ze = moddouz(ba)
        self.n_ba_ze = not_t[self._ba_ze]
    def imprimeNot(self):
        print('Cette note s\'appelle ', self.n_ba_ze )
        print('Avec ', self.n_ba_ze, 'les notes des accords de 3 sons seront:')
        print('Accord de quinte diminuée: ')
        for enne in accor_trois_sons_dim:
            print(not_t[self._ba_ze + enne])
        print('Accord mineur: ')
        for enne in accor_trois_sons_min:
            print(not_t[self._ba_ze + enne])
        print('Accord majeur: ')
        for enne in accor_trois_sons_maj:
            print(not_t[self._ba_ze + enne])
        print('Accord de quinte augmentés: ')
        for enne in accor_trois_sons_augm:
            print(not_t[self._ba_ze + enne])
        print('Les notes des accords de 4 sons seront:')
        print('Accord de septième diminuée: ')
        for enne in accor_quatre_sons_septieme_dim:
            print(not_t[self._ba_ze + enne])
        print('Accord de septième mineure: ')
        for enne in accor_quatre_sons_septieme_min:
            print(not_t[self._ba_ze + enne])
        print('Accord de septième de dominante: ')
        for enne in accor_quatre_sons_septieme_domin:
            print(not_t[self._ba_ze + enne])
        print('Accord de septième majeure: ')
        for enne in accor_quatre_sons_septieme_domin:
            print(not_t[self._ba_ze + enne])
        print('Accord de quinte augmentée avec septième majeure: ')
        for enne in accor_quatre_sons_quinte_augm_septieme_maj:
            print(not_t[self._ba_ze + enne])


#    def NotPosition(self):
'''        print(list_accor[1])
        for i in list_accor:
            ii = str(i)
            for cadire in ii:
                print(not_t[self._ba_ze + cadire])'''
if __name__ == '__main__':
    gao = 'o'
    while gao == 'o':
        gauAnalyz = AnalyseUn()
        gauAnalyz.gonott()
        sleep(1)
        gauAnalyz.imprimeNot()
        sleep(1)
        gao = input('\n---\nVoulez-vous ré-essayer? (o/n)')
    else:
        print('Merci pour votre participation!')
