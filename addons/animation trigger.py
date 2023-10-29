NAME 	= "Trigger"
VERSION = "1.0"
AUTHOR 	= "FrostedFreeze-18"
WEBSITE = "http://www.xfire.com/profile/frostedfreeze/"
DESCRIPTION = "Adds text triggers and the ability for others to trigger a user's animation."
COMMANDS = {
	"t": ["[string]", "Activates an animation with the text trigger of [string]."],
	"tt": ["[string]", "Creates a text trigger under the name: [string]."],
	"rt": ["Removes the text trigger from the selected animation."],
	"gt": ["Tells you what the text trigger is for the selected animation."]
}
 
import bf2
from game.gamemodes import sbxObjectManager
from game.gamemodes import sbxGame_build
 
class Addon:
 
	def __init__(self, core):
		self.core = core
		sbxObjectManager.sbxObject.triggerSetting = 0
		sbxGame_build.MultiObjectAnimation.string = None
 
	def chat_t(self, p, params):
		if not params:
			p.sendMsg("You need to say a [string].")
			return
		string = (" ").join(params).lower()
		for a in self.core.animations:
			if a.string == string: a.onPresetTrigger(1, 1)
 
	def chat_tt(self, p, params):
		if p.selectedAnimation and params:
			p.selectedAnimation.string = (" ").join(params).lower()
			p.sendMsg("Text trigger created for this animation.")
		else:
			p.sendMsg("You need to have an animation selected and give a string to trigger it.")
 
	def chat_rt(self, p, params):
		if p.selectedAnimation:
			p.selectedAnimation.string = None
			p.sendMsg("Text trigger removed.")
 
	def chat_gt(self, p, params):
		if p.selectedAnimation:
			if p.selectedAnimation.string:
				p.sendMsg("The text trigger for this animation is: " + p.selectedAnimation.string)
			else:
				p.sendMsg("This animation does not have a text trigger.")
 
	def rcon_btnAnimTriggerUnset(self, p, params):
		if p.grabObject:
			p.grabObject[0].triggerSetting = 0
			p.selectedAnimation.string = None
 
	def rcon_btnAnimTriggerSet(self, p, params):
		if p.grabObject:
			object = p.grabObject[0]
			if object.triggerType >= 6:
				object.triggerSetting += 1
				self.newTrigger(p, object)
 
	def newTrigger(self, p, object):
		setting = ["Local","Global","Team","Squad"]
		bf2.triggerManager.destroy(object.trigger)
		object.trigger = None
		if object.triggerSetting >= 1 and object.triggerSetting < 4:
			trigid = bf2.triggerManager.createRadiusTrigger(object.root, self.onAnimTrigger, '<<PCO>>', 1.5, (p,p.selectedAnimation,object))
			object.trigger = trigid
		else:
			object.triggerSetting = 0
		p.sendMsg("Animation trigger set to " + setting[object.triggerSetting] + ".")
 
	def onAnimTrigger(self, triggerID, object, vehicle, enter, params):
		owner = params[0]
		animation = params[1]
		object = params[2]
		players = vehicle.getOccupyingPlayers()
		if object.triggerSetting == 1:
			animation.onTrigger(enter, object.triggerType)
		elif object.triggerSetting == 2:
			for p in players:
				if p.getTeam() == object.owner.getTeam():
					animation.onTrigger(enter, object.triggerType)
		elif object.triggerSetting == 3:
			for p in players:
				if p.getTeam() == object.owner.getTeam() and p.getSquadId() == object.owner.getSquadId():
					animation.onTrigger(enter, object.triggerType)
		else:
			for p in players:
				if self.core.getPlayerByObject(p) == owner:
					animation.onTrigger(enter, object.triggerType)
					break