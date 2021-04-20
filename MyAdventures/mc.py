import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import mcpi.entity as creature
import config
from mcpi.connection import RequestError


class ConnectPlayer:
    def __init__(self, minecraft_obj, nick):
        self.mc = minecraft_obj
        self.player_id = minecraft_obj.getPlayerEntityId(nick)

    def getDirection(self):
        return self.mc.entity.getDirection(self.player_id)

    def getPitch(self):
        return self.mc.entity.getPitch(self.player_id)

    def getPos(self):
        return self.mc.entity.getPos(self.player_id)
        # return self.mc.entity.getTilePos(self.player_id)

    def getRotation(self):
        return self.mc.entity.getRotation(self.player_id)

    def getTilePos(self):
        return self.mc.entity.getTilePos(self.player_id)

    def setPos(self, x, y, z):
        return self.mc.entity.setPos(self.player_id, x, y, z)

    def setTilePos(self, x, y, z):
        return self.mc.entity.setTilePos(self.player_id, x, y, z)


mc = minecraft.Minecraft.create(address = config.server)
world = mc
world.spawnCreature = world.spawnEntity
try:
    player = ConnectPlayer(mc, config.nickname)
except RequestError:
    player = mc.player
