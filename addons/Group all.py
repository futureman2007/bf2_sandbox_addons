NAME 	= "Group All"
VERSION = "1.3"
AUTHOR 	= "FrostedFreeze-18"
WEBSITE = "http://www.xfire.com/profile/frostedfreeze/"
COMMANDS = {
	"groupall": ["Adds all of your objects to a group."],
	"ungroupall": ["Ungroups all of your objects."],
	"saveall": ["name","Saves all of your objects as a group."]
}
 
class Addon:
 
	def __init__(self, core):
		self.core = core
 
	def rcon_groupall(self, p, params):
		self.chat_groupall(p, params)
 
	def rcon_ungroupall(self, p, params):
		self.chat_ungroupall(p, params)
 
	def rcon_saveall(self, p, params):
		self.chat_saveall(p, params)
 
	def chat_groupall(self, p, params):
		self.core.rcon_btnEndGroup(p, params)
		self.core.rcon_btnStartGroup(p, params)
		for x in p.objects:
			p.selectedGroup.addObject(x, None)
		self.core.rcon_btnEndGroup(p, params)
 
	def chat_ungroupall(self, p, params):
		if p.groups == []: return
		self.core.rcon_btnEndGroup(p, params)
		p.groups = []
		p.grabGroup = []
		p.selectedGroup = None
		p.sendMsg("GROUP_UNGROUPED")
 
	def chat_saveall(self, p, params):
		self.chat_ungroupall(p, params)
		self.chat_groupall(p, params)
		p.grabObject = [p.objects[0]]
		self.core.rcon_btnGrabGroup(p, params)
		if not params: params = ["QuickSave"]
		groupName = params
		p.sendMsg("Attempting to save the group as '" + " ".join(groupName) + "'...")
		self.core.chat_netsavegroup(p, groupName)