class GameState:
    def __init__(self):
        self.sanity = 100
        self.inventory = []
        self.visited_rooms = set()
        self.game_over = False
        self.room_count = 0
        self.locked_door_found = False
        self.found_clues = 0
        self.cursed_item = False
        self.in_danger = False



