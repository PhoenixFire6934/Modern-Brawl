from Database.Tables.Player import *
from Utils.Helpers import *

from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Emotes import Emotes
from Files.CsvLogic.Skins import Skins
from Files.CsvLogic.Cards import Cards


import json

class Player:
	ID = 0
	token = None

	skinsID       = Skins.get_skins_id()
	emotesID      = Emotes.get_emotes_id()
	brawlersID    = Characters.get_brawlers_id()
	cardsSkillsID = Cards.get_spg_id()
	cardsUnlockID = Cards.get_brawler_unlock()


	brawlers_skins = {}
	for id in brawlersID:
		brawlers_skins.update({f'{id}': 0})

	gold, tickets, gems, starpoints, trophies = 10000, 500, 9999, 10000, 12000
	homeBrawler, homeSkin, nameColor, thumbnail, roomID, mapID, team = 0, 0, 0, 0, 0, 0, 0
	name, nameSet = '', False
	starpower, gadget = 76, 255
	dnd, useGadget = False, True


	Helpers = Helpers()


	def __init__(self, device):
		self.device  = device
		self.Data    = None
		self.ID      = Player.ID
		self.token   = Player.token
		self.Helpers = Helpers()


	def getPlayerAccount(self):
		if self.token:
			self.loadPlayerAccount()
		else:
			if self.ID == 0:
				self.createPlayerAccount()

		Player.name           = self.Data['Name']
		Player.nameSet        = self.Data['NameSet']
		Player.thumbnail      = self.Data['Thumbnail']
		Player.nameColor      = self.Data['NameColor']
		Player.trophies       = self.Data['Trophies']
		Player.tickets        = self.Data['Tickets']
		Player.gems           = self.Data['Diamonds']
		Player.starpower      = self.Data['Starpower']
		Player.gadget         = self.Data['Gadget']
		Player.homeBrawler    = self.Data['HomeBrawler']
		Player.homeSkin       = self.Data['HomeSkin']
		Player.brawlers_skins = self.Data['HomeSkins']


	def loadPlayerAccount(self):
		self.DB = DataBase()
		try:
			self.Data = json.loads(self.DB.getPlayerAccount(self.token)[0][3])
		except IndexError: # Account not found
			self.createPlayerAccount(token = self.token)


	def createPlayerAccount(self, token = Helpers.randomToken(), id = Helpers.randomID()):
		self.DB = DataBase()

		self.ID = id
		self.token = token

		data = {
			'ID': self.ID, 'Token': self.token, 'Name': 'Guest', 'NameSet': False, 'Trophies': 99999, 'Tickets': 8888,
			'Diamonds': 9999, 'Score': 99999, 'ExpPoints': 99999, 'HomeBrawler': 0, 'HomeSkin': 0, 'Starpower': 76,
			'Gadget': 255, 'Thumbnail': 0, 'NameColor': 0, 'HomeSkins': Player.brawlers_skins,
			'Resources': [{'ID': 1, 'Amount': 10000}, {'ID': 8, 'Amount': 10000}, {'ID': 9, 'Amount': 10000}, {'ID': 10, 'Amount': 10000}],
		}

		self.DB.createPlayerAccount(self.token, self.ID, 9999, json.dumps(data))
		self.Data = json.loads(self.DB.getPlayerAccount(self.token)[0][3])


	def updateAccount(self, var, value):
		self.DB = DataBase()

		self.Data[var] = value
		self.DB.updatePlayerAccount('data', json.dumps(self.Data), self.token)