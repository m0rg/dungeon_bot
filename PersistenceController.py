
class PersistenceController(object):
	players = {}



	def is_registered(self, user):
		if user.username in self.players.keys():
			return True
		return False
	
	def add_player(self, user, player):
		self.players[user.username] = player

	def get_ply(self, user):
		#if is_registered(user.username):
		return self.players[user.username]
		
instance = None
def get_persistence_controller_instance():
	if not instance:
		instance = ersistenceController()
	return instance

