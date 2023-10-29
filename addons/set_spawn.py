NAME 	= "set_spawn"
VERSION = "1.0"
AUTHOR 	= "Mike__MRM"
WEBSITE = "mikemrm.com"
DESCRIPTION = "Allows you to set your spawn location"
COMMANDS = {
	"setspawn": ["Sets your current position as your next spawn"],
	"setspawn": ["off", "Turns off your spawn"],
	"spawninfo": ["shows your current spawn status"],
	"resetspawn": ["resets your spawn to off and position to 0"]
}
import bf2

class Addon:

	def __init__(self, core):
		self.core = core
	
	def onPlayerConnect(self, playerObject):
		playerObject.spawn = 0
		playerObject.spawnPos = ""

	def onPlayerSpawn(self, playerObject, soldierObject):
		if playerObject.spawn == 1:
			playerObject.getVehicleRoot().setPosition(playerObject.spawnPos)
			
	def chat_setspawn(self, p, params):
		if len(params) == 1:
			if params[0] == "off":
				p.spawn = 0
				p.sendMsg("Spawn turned off")
			return
		try:
			p.spawnPos = p.getVehicleRoot().getPosition()
			p.spawn = 1
		except: p.sendMsg("Error setting spawn position")
		
		p.sendMsg("Spawn set, type @setspawn off to turn off")
		
	def chat_spawninfo(self, p, params):
		try:
			if p.spawn == 0:
				spawnmsg = "off"
			else:
				spawnmsg = "on"
			
			p.sendMsg("Your spawn is turned " + str(spawnmsg) + ", located at " + str(p.spawnPos))
		except:
			p.sendMsg("Error gathering information attempting to fix")
			try:
				p.spawn = 0
				p.spawnPos = (0,0,0)
				p.sendMsg("Fixed information try setting spawn again")
			except:
				p.sendMsg("Error fixing information")
	
	def chat_resetspawn(self, p, params):
		p.spawn = 0
		p.spawnPos = 0
		p.sendMsg("Spawn Reset")