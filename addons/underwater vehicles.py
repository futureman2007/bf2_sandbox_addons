NAME 	= "Underwater Vehicles"
VERSION = "1.0"
AUTHOR 	= "FrostedFreeze-18"
WEBSITE = "http://www.xfire.com/profile/frostedfreeze/"
DESCRIPTION = "Modifies vehicles so they can work underwater."
 
MODIFICATIONS = [
		"ObjectTemplate.armor.hpLostWhileInWater 0",
		"ObjectTemplate.armor.hpLostWhileInDeepWater 0"
		]
 
import host
 
class Addon:
 
	def __init__(self, core):
		self.core = core
		self.updateVehicles()
 
	def onGameStatusChanged(self, status):
		self.updateVehicles()
 
	def updateVehicles(self):
		for x in self.core.settings.vehicles:
			host.rcon_invoke("ObjectTemplate.activeSafe PlayerControlObject " + x)
			for i in MODIFICATIONS:
				host.rcon_invoke(i)