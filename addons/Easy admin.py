NAME 	= "EasyAdmin"
VERSION = "1.8.0"
AUTHOR 	= "Andokool12"
WEBSITE = "www.cheetocommunity.co.cc"
COMMANDS = {
	"kick": ["Kicks the player via ID.  If PB is on, use @pbkick instead."],
	"ban": ["Bans the player via ID, for how long.  If PB is on, use @pbban instead."],
	"an": ["Announce something in the top chat."],
	"scream": ["Giant annoying green text version of announce."],
	"banlist": ["A list of banned IP addresses in the server's console.  Use @pbbanlist if PB is on."],
	"unban": ["Unban a user via IP address.  If PB is on, use @pbunban instead."],
	"nukebans": ["Unban everyone banned on the server.  Only works if PB is enabled."],
	"nextmap": ["Displays next map."],
	"reboot": ["Restart the current map."],
	"runnextmap": ["Run the next map."],
	"help": ["Get help."],
	"advert": ["Quickly advertise EA Script."],
	"maintenance": ["Does maintenance automatically.  DOES NOT REQUIRE A RESTART!"],
	"pbkick": ["Kicks players via Punkbuster.  MUCH more stable than @kick.  Only works if PB is enabled."],
	"pbban": ["Bans players via Punkbuster.  MUCH more stable than @ban.  Only works if PB is enabled."],
	"players": ["Shows a list of players in the server's console."],
	"pbbanlist": ["Works like @banlist, just more stable and uses PB."],
	"pbunban": ["Works like @unban, just uses PB instead and is obviously more stable because of this."]
	}

PERMISSIONS = {
    "chat": {
        "kick": 20,
        "ban": 20,
	"an": 20,
	"scream": 20,
	"banlist": 20,
	"unban": 20,
	"nukebans": 21,
	"nextmap": 20,
	"reboot": 20,
	"runextmap": 20,
	"ifail": 20,
	"help": 20,
	"advert": 20,
	"maintenance": 20
    }
}

import host

class Addon:
	
	def __init__(self, core):
		self.core = core
		self.time = 0
		self.EAv = "1.8.0"
		self.PB = False
		self.AUB = False
		self.PBSS = False

	def chat_kick(self, p, params):
		host.rcon_invoke("admin.kickplayer " + str(params[0]))

	def chat_ban(self, p, params):
		host.rcon_invoke("admin.banplayer " + str(params[0]))

	def chat_an(self, p, params):
		self.core.sendMsg(" ".join(params))

	def chat_scream(self, p, params):
		self.core.sendMsg("§3" + " ".join(params))

	def chat_banlist(self, p, params):
		host.rcon_invoke("admin.listBannedAddresses ")

	def chat_unban(self, p, params):
		host.rcon_invoke("admin.removeAddressFromBanList " + str(params[0]))

	def chat_nukebans(self, p, params):
		host.rcon_invoke("PB_SV_BanEmpty ")
		self.core.sendMsg("The ban list has been cleared.")

	def chat_setnext(self, p, params):
		host.rcon_invoke("maplist.insert " + str(params[0]))

	def chat_reboot(self, p, params):
		host.rcon_invoke("admin.restartMap ")

	def chat_runnextmap(self, p, params):
		host.rcon_invoke("admin.runNextLevel ")

	def chat_help(self, p, params):
		p.sendMsg("Yo, I'm too lazy to update this command with every revision so just type @ainfo EasyAdmin or whatever it's saved as.")

	def chat_advert(self, p, params):
		self.core.sendMsg("This server is running EasyAdmin " + str(self.EAv) + ".  Who needs BF2CC!?")

	def chat_maintenance(self, p, params):
		host.rcon_invoke("PB_SV_Enable ")
		self.core.sendMsg("PB Re-enabled.")
		host.rcon_invoke("PB_SV_BanLoad ")
		self.core.sendMsg("Banlist reloaded.")
		host.rcon_invoke("PB_SV_UpdBanFile ")
		self.core.sendMsg("Banlist updated.")
		host.rcon_invoke("PB_SV_Update ")
		self.core.sendMsg("Updating client-side PB.")
		host.rcon_invoke("PB_SV_WriteCfg ")
		self.core.sendMsg("Updating config files - Current server settings saved.")
		
	def chat_pbkick(self, p, params):
		host.rcon_invoke("PB_SV_Kick " + str(params[0]))
		
	def chat_pbban(self, p, params):
		host.rcon_invoke("PB_SV_Ban " + str(params[0]))
		
	def chat_players(self, p, params):
		host.rcon_invoke("PB_SV_PList")
	
	def chat_pbbanlist(self, p, params):
		host.rcon_invoke("PB_SV_BanList ")

	def chat_pbunban(self, p, params):
		host.rcon_invoke("PB_SV_UnBan " + str(params[0]))

	def tickOneSec(self):
		self.time += 1
		time = 1440 - self.time
		if self.time == 0:
			self.core.sendMsg("§3" + "This server runs on Easy Admin " + str(self.EAv) + ".")
		if self.time == 60:
			self.core.sendMsg("Easy Admin is written and developed by Andokool12.  www.cheetocommunity.co.cc")
		if self.time == 120:
			self.core.sendMsg("§3" + "This server runs on Easy Admin " + str(self.EAv) + ".")
		if self.time == 180:
			self.core.sendMsg("Easy Admin is written and developed by Andokool12.  www.cheetocommunity.co.cc")
		if self.time == 240:
			self.core.sendMsg("§3" + "This server runs on Easy Admin " + str(self.EAv) + ".")
		if self.time == 300:
			self.core.sendMsg("Easy Admin is written and developed by Andokool12.  www.cheetocommunity.co.cc")
		if self.time == 360:
			self.core.sendMsg("§3" + "This server runs on Easy Admin " + str(self.EAv) + ".")
		if self.time == 420:
			self.core.sendMsg("Easy Admin is written and developed by Andokool12.  www.cheetocommunity.co.cc")
		if self.time == 480:
			self.core.sendMsg("§3" + "This server runs on Easy Admin " + str(self.EAv) + ".")
		if self.time == 540:
			self.core.sendMsg("Easy Admin is written and developed by Andokool12.  www.cheetocommunity.co.cc")
		if self.time == 600:
			self.core.sendMsg("§3" + "This server runs on Easy Admin " + str(self.EAv) + ".")
		if self.time == 660:
			self.core.sendMsg("Easy Admin is written and developed by Andokool12.  www.cheetocommunity.co.cc")
		if self.time == 720:
			self.core.sendMsg("§3" + "This server runs on Easy Admin " + str(self.EAv) + ".")
		if self.time == 780:
			self.core.sendMsg("Easy Admin is written and developed by Andokool12.  www.cheetocommunity.co.cc")
		if self.time == 840:
			self.core.sendMsg("§3" + "This server runs on Easy Admin " + str(self.EAv) + ".")
		if self.time == 900:
			self.core.sendMsg("Easy Admin is written and developed by Andokool12.  www.cheetocommunity.co.cc")
		if self.time == 960:
			self.core.sendMsg("§3" + "This server runs on Easy Admin " + str(self.EAv) + ".")
		if self.time == 1020:
			self.core.sendMsg("Easy Admin is written and developed by Andokool12.  www.cheetocommunity.co.cc")
		if self.time == 1080:
			self.core.sendMsg("§3" + "This server runs on Easy Admin " + str(self.EAv) + ".")
		if self.time == 1140:
			self.core.sendMsg("Easy Admin is written and developed by Andokool12.  www.cheetocommunity.co.cc")
		if self.time == 1200:
			self.core.sendMsg("§3" + "This server runs on Easy Admin " + str(self.EAv) + ".")
		if self.time == 1260:
			self.core.sendMsg("Easy Admin is written and developed by Andokool12.  www.cheetocommunity.co.cc")
		if self.time == 1320:
			self.core.sendMsg("§3" + "This server runs on Easy Admin " + str(self.EAv) + ".")
		if self.time == 1380:
			self.core.sendMsg("Easy Admin is written and developed by Andokool12.  www.cheetocommunity.co.cc")
		if self.time == 1440:
			self.time = 0