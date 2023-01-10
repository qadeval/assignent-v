"""
json
"""
import json
import os
os.linesep
from itertools import count

import pytest




class Test_team:

	
	def test_non_indian_players(self):
		"""
		It uses the open() function to open the file 'rcb.json' in read mode and assigns it to the variable 'f'.
It loads the JSON data from the file object 'f' directly with json.load(f) and assigns it to the variable 'data'.
It accesses the 'player' key from the 'data' JSON object.
Then it uses a list comprehension to create a list of players from the 'player' key, where the country of the player is not India, and assigns it to the variable 'non_indian_players'.
It asserts that the length of 'non_indian_players' is 4.
Then it prints the number of non-Indian players.
Then it uses any() function with generator expression to check if there is at least one player whose role is 'Wicket-keeper' and asserts that with a message 'Team does not have a wicketkeeper'
Then it uses filter() function to filter out all the players where role is 'Wicket-keeper' and assigns that to variable wicket_keepers
Then it loops through wicket_keepers and prints the name and details of each wicket-keeper

		:return:
		non_indian player == 4 only
		at_least keeper == 1
		keeper name & detail print in console
		"""
		# Open the json file in read mode
		with open("../jsonfile/rcb.json", 'r') as f:
			# Load the data directly from open file object
			data = json.load(f)
			# Access the 'player' key from json object
			player = data['player']
			# Use list comprehension to get all the non-Indian players
			non_indian_players = [p for p in player if p.get("country") != "India"]
			# asserting non_indian player is 4 only as per requirement
			assert len(non_indian_players)== 4
			# Print out the number of non-Indian players
			print("Non-Indian players count:", len(non_indian_players))
			# assert at least one w_keeper in team
			assert any(player["role"] == "Wicket-keeper" for player in player), "Team does not have a wicketkeeper"
			wicket_keepers = filter(lambda x: x["role"] == "Wicket-keeper", player)
			for wicket_keeper in wicket_keepers:
				print("Wicket-keeper name: ", wicket_keeper["name"])
				print("Wicket-keeper details: ", wicket_keeper)
			

	
		