NAME 	= "Portal"
VERSION = "1.0"
AUTHOR 	= "Smasher816"

import bf2

class Addon:
	def __init__(self, core):
		self.core = core
		for p in self.core.getAllPlayers(): self.settings(p)

	def onPlayerConnect(self, playerObject):
		self.settings(playerObject)
	
	def settings(self, playerObject):
		playerObject.trigs = {}
		playerObject.portals = {}
	
	def chat_delall(self, p, params): self.portaldelall(p)

	def chat_lportals(self, p, params):
		mode = 0
		for portal in p.portals.values():
			if params[0] == "all":
				portal[1] = 0
				mode = 0
			elif params[0] == "team":
				portal[1] = 1
				mode = 1
			elif params[0] == "squad":
				portal[1] = 2
				mode = 2
			elif params[0] == "me":
				portal[1] = 3
				mode = 3
		if mode == 0: p.sendMsg("All portals useable to everyone")
		if mode == 1: p.sendMsg("Portals only useable to your team")
		if mode == 2: p.sendMsg("Portals only useable to your squad")
		if mode == 3: p.sendMsg("Portals only useable to you")
		
	def chat_lportal(self, p, params):
		name = params[0]
		if params[1] == "all":
			p.portals[name][1] = 0
			p.sendMsg("Portal " + name + " useable to everyone")
		elif params[1] == "team":
			p.portals[name][1] = 1
			p.sendMsg("Portal " + name + " only useable to your team")
		elif params[1] == "squad":
			p.portals[name][1] = 2
			p.sendMsg("Portal " + name + " only useable to your squad")
		elif params[1] == "me":
			p.portals[name][1] = 3
			p.sendMsg("Portal " + name + " only useable to you")		

	def chat_rportals(self, p, params): self.portaldelall(p)
	def chat_rportal(self, p, params):
		name = params[0]
		del p.portals[name]
		if p.trigs.has_key(name):
			trig = p.trigs[name]
			bf2.triggerManager.destroy(trig)
			del p.trigs[name]
			p.sendMsg ("Portal " + name + "(" + str(trig) + ") destroyed")
		else: p.sendMsg("Portal allready destroyed")
			
	def chat_portal(self, p, params):
		if p.grabObject:
			object = p.grabObject[0]
			name = params[0]
			radi = params[1]
			if not radi: radi = "1"
			radi = float(radi)
			if radi <= 0: radi = 0.1
			if radi > 15: radi = 15
			if p.trigs.has_key(name): bf2.triggerManager.destroy(p.trigs[name])
			trigid = bf2.triggerManager.createRadiusTrigger(object.root, self.onPortalTrigger, '<<PCO>>', radi, (p,name))
			p.trigs[name] = trigid
			p.portals[name] = [None, 0]
			self.core.rcon_btnDrop(p, ())
			p.sendMsg(str(radi) + " distance portal named as " + name + "(" + str(trigid) + ")")
		else: p.sendMsg("No object Grabed")

	def chat_eportal(self, p, params):
		if p.grabObject:
			object = p.grabObject[0]
			name = params[0]
			if p.portals.has_key(name):
				p.portals[name][0] = object
				p.sendMsg("Exit linked to portal " + name)
			else: p.sendMsg("You must create portal " + name + " before you can use @eportal")
			self.core.rcon_btnDrop(p, ())
		else: p.sendMsg("No object Grabed")

	def onPortalTrigger(self, triggerID, object, vehicle, enter, params):
		owner = params[0]
		trigname = params[1]
		trig = owner.trigs[trigname]
		object = owner.portals[trigname][0]
		lock = owner.portals[trigname][1]
		pos = None
		if object: pos = object.getPosition()
		if enter:
			if object and pos:
				if vehicle:
					vehicle = bf2.objectManager.getRootParent(vehicle)
					driver = vehicle.getOccupyingPlayers()[0]
					if lock == 0: bf2.objectManager.getRootParent(vehicle).setPosition(pos)
					elif lock == 1:
						if owner.getTeam() == driver.getTeam():
							vehicle.setPosition(pos)
						else: self.core.sendMsg("Portal only for " + owner.getName() + "'s team")
					elif lock == 2:
						if owner.getSquadId() == driver.getSquadId():
							vehicle.setPosition(pos)
						else: self.core.sendMsg("Portal only for " + owner.getName() + "'s squad")
					elif lock == 3:
						if owner.getName() == driver.getName():
							vehicle.setPosition(pos)
						else: self.core.sendMsg("Portal only for " + owner.getName())
			else: self.core.sendMsg("No exit for " + owner.getName() + "'s portal " + trigname + "(" + str(trig) + ")")

	def portaldelall(self, p):
		p.portals = {}
		for trig in p.trigs.values(): bf2.triggerManager.destroy(trig)
		p.trigs = {}
		p.sendMsg ("All portals deleted.")