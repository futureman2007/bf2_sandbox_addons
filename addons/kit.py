NAME = "kit"
VERSION = "1.0.1"
AUTHOR = "BlueDuckraider50"
 
import host
import bf2
 
class Addon:
	def __init__(self, core):
		self.core = core
 
	def chat_kit(self, p, params):
		if params[0] == "mec_sniper":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate MEC_Sniper")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: Mec_sniper")
		if params[0] == "mec_assault":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate MEC_Assault")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: Mec_Assault")
		if params[0] == "mec_at":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate MEC_AT")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: MEC_AT")
		if params[0] == "mec_engineer":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate MEC_Engineer")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: MEC_Engineer")
		if params[0] == "mec_medic":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate MEC_Medic")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: MEC_Medic")
		if params[0] == "mec_specops":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate MEC_Specops")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: MEC_Specops")
		if params[0] == "mec_support":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate MEC_Support")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: MEC_Support")
		if params[0] == "mec_list":
			self.core.sendMsg("MEC Projectile list")
			self.core.sendMsg("MEC_Sniper, MEC_Assault, MEC_AT, MEC_Engineer, MEC_Medic, MEC_Specops, MEC_Support")
		if params[0] == "us_sniper":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate US_Sniper")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: US_sniper")
		if params[0] == "us_assault":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate US_Assault")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: US_Assault")
		if params[0] == "us_at":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate US_AT")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: US_AT")
		if params[0] == "us_engineer":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate US_Engineer")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: US_Engineer")
		if params[0] == "us_medic":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate US_Medic")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: US_Medic")
		if params[0] == "us_specops":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate US_Specops")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: US_Specops")
		if params[0] == "us_support":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate US_Support")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: US_Support")
		if params[0] == "us_list":
			self.core.sendMsg("US Projectile list")
			self.core.sendMsg("US_Sniper, US_Assault, US_AT, US_Engineer, US_Medic, US_Specops, US_Support")
		if params[0] == "eu_sniper":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate EU_Sniper")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: EU_sniper")
		if params[0] == "eu_assault":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate EU_Assault")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: EU_Assault")
		if params[0] == "eu_at":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate EU_AT")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: EU_AT")
		if params[0] == "eu_engineer":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate EU_Engineer")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: EU_Engineer")
		if params[0] == "eu_medic":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate EU_Medic")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: EU_Medic")
		if params[0] == "eu_specops":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate EU_Specops")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: EU_Specops")
		if params[0] == "eu_support":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate EU_Support")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: EU_Support")
		if params[0] == "eu_list":
			self.core.sendMsg("EU Projectile list")
			self.core.sendMsg("EU_Sniper, EU_Assault, EU_AT, EU_Engineer, EU_Medic, EU_Specops, EU_Support")
		if params[0] == "ch_sniper":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate CH_Sniper")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: CH_sniper")
		if params[0] == "ch_assault":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate CH_Assault")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: CH_Assault")
		if params[0] == "ch_at":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate CH_AT")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: CH_AT")
		if params[0] == "ch_engineer":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate CH_Engineer")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: CH_Engineer")
		if params[0] == "ch_medic":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate CH_Medic")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: CH_Medic")
		if params[0] == "ch_specops":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate CH_Specops")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: CH_Specops")
		if params[0] == "ch_support":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate CH_Support")
			host.rcon_invoke("ObjectTemplate.velocity 20")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 9999")
			self.core.sendMsg("Knife projectile changed to: CH_Support")
		if params[0] == "ch_list":
			self.core.sendMsg("CH Projectile list")
			self.core.sendMsg("CH_Sniper, CH_Assault, CH_AT, CH_Engineer, CH_Medic, CH_Specops, CH_Support")
		if params[0] == "reset":
			host.rcon_invoke("objecttemplate.active kni_knife")
			host.rcon_invoke("objecttemplate.projectiletemplate kni_knife_Projectile")
			host.rcon_invoke("ObjectTemplate.velocity 40")
			host.rcon_invoke("objecttemplate.fire.roundsperminute 120")
			self.core.sendMsg("Knife projectile resetet")