NAME 	= "AutoLock"
VERSION = "1.0"
AUTHOR 	= "FrostedFreeze-18"
WEBSITE = "http://www.xfire.com/profile/frostedfreeze/"
HIDDEN = 1
 
class Addon:
 
	def __init__(self, core):
		self.core = core
 
	def onPlayerConnect(self, playerObject):
		playerObject.autoLock = True