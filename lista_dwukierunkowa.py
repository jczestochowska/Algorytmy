#!/usr/bin/env python
# -*- coding: utf-8 -*-

class element():
	def __init__(self, x):
		self.wartosc = x
		self.nast = None
		self.poprz = None

	# def dodaj_nast(self, n):
	# 	self.nast = element(n)
	# 	return element(n)

	def zwroc_nast(self):
		return self.nast

	def zwroc_poprz(self):
		return self.poprz


class lista():
	def __init__(self, x: object) -> object:
		self.pocz = element(x)

	def znajdz_ost(self):
		war = True
		ost = self.pocz
		while war:
			if ost.nast:
				ost = ost.nast
			else:
				war = False
		return ost

	def dodaj(self,x):
		nowy = element(x)
		ost = self.znajdz_ost()
		nowy.poprz = ost
		ost.nast = nowy

	def usun(self, x):
		war = True
		ost = self.pocz
		while war:
			if ost.wartosc == x:
				nastepny = ost.zwroc_nast()
				poprzedni = ost.zwroc_poprz()
				war = False
			else:
				ost = ost.nast
		if nastepny and poprzedni:
			poprzedni.nast = nastepny
			nastepny.poprz = poprzedni
		elif poprzedni == None and nastepny:
			self.pocz = nastepny
		elif nastepny == None and poprzedni:
			poprzedni.nast = None
		ost = None

	def wypisz(self):
		print(self.pocz.wartosc)
		war = True
		n = self.pocz.nast
		while war:
			if n:
				print(n.wartosc)
				n = n.nast
			else:
				war = False

	def zwroc_rozmiar(self):
		war = True
		if self.pocz:
			el = self.pocz
			rozmiar = 1
			while war:
				if el.nast:
					rozmiar += 1
					el = el.nast
				else:
					war = False
			print(rozmiar)
			return rozmiar
		else:
			print("Twoja lista jest pusta")
			rozmiar = 0
			print(rozmiar)
			return rozmiar


if __name__ == "__main__":
	l = lista(5)
	l.dodaj(6)
	l.dodaj(9)
	l.wypisz()
	l.usun(5)
	l.wypisz()
	l.zwroc_rozmiar()
