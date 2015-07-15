import random
import util
import enemies
class Dungeon(object):
	def __init__(self, uid, name, description, players, rooms = [], current_room = 0):
		self.uid = uid
		self.name = name
		self.description = description
		self.rooms = rooms		
		self.players = players
		self.current_room = 0

		self.difficulty = sum([p.stats["level"] for p in players])/len(self.players)

	def get_enemy(self, difficulty=None):
		if not difficulty:
			difficulty = self.difficulty
		return enemies.retrieve_enemy_for_difficulty(difficulty)

	def generate_rooms(self, amount):
		for i in range(amount):
			room_type = random.choice(["enemy"])
			uid = util.get_uid()
			room = Room(uid, room_type)
			if room_type == "loot":
				#todo add loot rooms
				pass #retrieve a loot distribution event
			elif room_type == "riddle":
				#todo add riddle rooms
				pass
			elif room_type == "enemy":
				amount_of_enemies = random.randint(1, 3)
				combat_enemies = []
				for n in range(amount_of_enemies):
					combat_enemies.append(self.get_enemy())
				room.combat_enemies = combat_enemies
				
			self.rooms.append(room)

class Room(object):
	def __init__(self, uid, room_type):
		self.uid = uid
		self.room_type = room_type

	def enter(self):
		pass

def test_dungeon_creation():
	from creatures import Player
	dung = Dungeon("01", "Dungeon of testing", "A creepy dungeon of bugs", [Player("Orc", "The orc", "orc")])
	dung.generate_rooms(2)
	for room in dung.rooms:
		print("\nRoom #%s of type %s:"%(room.uid, room.room_type))
		for enemy in room.combat_enemies:
			print(enemy.examine_self())
