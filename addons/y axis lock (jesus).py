NAME 	= "Jesus"
VERSION = "1.4"
AUTHOR 	= "FrostedFreeze-18"
WEBSITE = "http://www.xfire.com/profile/frostedfreeze/"
COMMANDS = {
	"jesusmode": ["<Nothing> or [off]", "Gives you the ability to walk on water."],
	"godmode": ["[height / off]","Gives you the ability to walk above <height>."],
	"lockheight": ["<Nothing> or [off]","Gives you the ability to walk above your current height."]
}
 
WATER_LEVEL = {
	"clearing":			25,
	"crystal_coast":		23,
	"dalian_plant":			141.4,
	"daqing_oilfields":		130,
	"dragon_valley":		52,
	"freeze_map":			62,
	"fushe_pass":			61.6,
	"greatwall":			100,
	"gulf_of_oman":			24,
	"highway_tampa":		25,
	"kubra_dam":			46.1,
	"mashtuur_city":		32.5,
	"maze01":			105,
	"midnight_sun":			77,
	"operation_blue_pearl":		22.1,
	"operation_clean_sweep":	29,
	"operationharvest":		20,
	"operationroadrage":		44,
	"operationsmokescreen":		88,
	"road_to_jalalabad":		36,
	"sharqi_peninsula":		70,
	"songhua_stalemate":		167,
	"strike_at_karkand":		146,
	"taraba_quarry":		98,
	"wake_island_2007":		83,
	"zatar_wetlands":		33
}
 
import host
 
class Addon:
 
	def __init__(self, core):
		self.core = core
 
	def onPlayerConnect(self, playerObject):
		playerObject.walkMode = [False, None, 0]
 
	def chat_jesusmode(self, p, params):
		if not self.toggleMode(p, params):
			if host.sgl_getMapName().lower() not in WATER_LEVEL: return
			self.changeMode(p, float(WATER_LEVEL[host.sgl_getMapName().lower()]))
 
	def chat_godmode(self, p, params):
		if not self.toggleMode(p, params):
			self.changeMode(p, float(params[0]))
 
	def chat_lockheight(self, p, params):
		if not self.toggleMode(p, params):
			self.changeMode(p, (p.getVehicle().getPosition()[1] - 1.0))
 
	def toggleMode(self, p, params):
		if len(params) > 0 and params[0].lower() == "off":
			p.walkMode = [False, None, 0]
			return True
		return False
 
	def changeMode(self, p, float):
		if float > 10000: float = 10000
		obj = None
		if p.walkMode[1] != None: obj = p.walkMode[1]
		else:
			for o in p.objects:
				if o.templateName.replace("_mp", "") == "glassplane01": obj = o
			if not obj:
				p.sendMsg("Spawn a glass square first!")
				return
		p.walkMode = [True, obj, float]
		p.sendMsg("Minimum height set to " + str(float))
 
	def tickFrame(self):
		for p in self.core.getAlivePlayers():
			if p.walkMode[1] != None and p.walkMode[1] not in p.objects:
				p.walkMode = [False, None, 0]
			if p.walkMode[0] and p.getVehicle() == p.getDefaultVehicle():
				if p.walkMode[1]:
					pos = p.getVehicleRoot().getPosition()
					p.walkMode[1].setPosition((pos[0], p.walkMode[2] - 0.01, pos[2]))
					p.walkMode[1].setRotation((0.0, 0.0, 90.0))
					if pos[1] < p.walkMode[2] + 0.4:
						p.getVehicleRoot().setPosition((pos[0], p.walkMode[2] + 3.0, pos[1]))