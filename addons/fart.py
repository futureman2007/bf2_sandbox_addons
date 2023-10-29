NAME    = "fart"
VERSION = "0.3"
AUTHOR  = "Nathanv69"
WEBSITE = "http://oldschoolsnipers.webs.com"
COMMANDS = {
        "fart": ["choose your fart!."]
}
 
 
class Addon:
        
        def __init__(self, core):
                self.core = core
        
        def chat_fart(self, p, params):
                p.sendMsg("who farted?!")

        def chat_loudfart(self, p, params):
                p.sendMsg("dairy air o.o")

        def chat_squickyfart(self, p, params):
                p.sendMsg("ow my ear!!!")

        def chat_popfart(self, p, params):
                p.sendMsg("god i hope those are pop rocks! -.-")

        def chat_squishyfart(self, p, params):
                p.sendMsg("need to wipe? O_o")

        def chat_smellyfart(self, p, params):
                p.sendMsg("SOMEONE CALL THE POLICE!")

        def chat_flappyfart(self, p, params):
                p.sendMsg("you really gotta start working out if it flaps...")

        def chat_firefart(self, p, params):
                p.sendMsg("*lights butt on fire*")