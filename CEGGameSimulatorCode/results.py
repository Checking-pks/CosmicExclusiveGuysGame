from simulation import *

class Results:

	def __init__(self):
		# Generate an empty array to save the times a player has passed a tile
		self.hits = [0] * 41
		self.wins = 0

	def addHitResults(self, hits):
		# Add hits given to the local hits array
		for i in range(0, 41):
			self.hits[i] += hits[i]

	def addWins(self):
		# Add hits given to the local hits array
		self.wins += 1

	def writeHTML(self, games, turns, cards, freeSpaceTravel, autoExploration):
		# Open the file
		file = open("results.html", "w")

		# Write the beginning HTML
		barHeight = 100.0 / float(len(self.hits))
		file.write("<!DOCTYPE html><html><head><title>Monopoly Results</title><link href=\"https://fonts.googleapis.com\
			/css?family=Nunito+Sans\" rel=\"stylesheet\"><style>*{margin: 0;padding: 0;}body, html{height: 100%;\
			font-family: 'Nunito Sans', sans-serif;}.header{width: 20rem;height: 100%;padding: 1.5rem;\
			box-sizing: border-box;box-shadow: 0 0 50px 1px rgba(0,0,0,0.25);}.results{position: absolute;top: 0;\
			left: 20rem;right: 0;bottom: 0;padding: 1.5rem;font-size: 0.75rem}.settings{margin: 3rem -0.5rem 0 -0.5rem;\
			}.setting{display: inline-block;box-sizing: border-box;width: 10rem;padding-left: 0.5rem;}.value{\
			display: inline-block;}.bold{font-weight: bold;border-bottom: 1px solid rgba(0,0,0,0.5);}\
			.settings>div:not(.bold):nth-child(odd){background-color: rgba(0,0,0,0.05);}.row{width: 100%;height: " + \
			str(barHeight) + "%;overflow: hidden;box-sizing: border-box;border-bottom: 1px solid rgba(0,0,0,0.15);}\
			.row:first-child{border-top: 1px solid rgba(0,0,0,0.15);}.name{float: left;width: 9rem;height: 100%;}\
			.bar-container{height: 100%;margin-left: 9rem;}.bar{max-width: 100% !important;height: 100%;color: white;\
			text-align: right;box-sizing: border-box;background-color: #E85D75;}</style></head><body>\
			<div class=\"header\"><h1>CEG Game simulation results</h1><div class=\"settings\"><div class=\"bold\">\
			<div class=\"setting\">Setting</div><div class=\"value\">Value</div></div>")

		# Write simulation configuration
		file.write("<div><div class=\"setting\">Games</div><div class=\"value\">%s</div></div>" % games)
		file.write("<div><div class=\"setting\">Turns</div><div class=\"value\">%s</div></div>" % turns)
		file.write("<div><div class=\"setting\">Cards</div><div class=\"value\">%s</div></div>" % (cards if "True" else "False"))
		file.write("<div><div class=\"setting\">Free Space Travel</div><div class=\"value\">%s</div></div>" % (freeSpaceTravel if "True" else "False"))
		file.write("<div><div class=\"setting\">Auto Exploration</div><div class=\"value\">%s</div></div>" % (autoExploration if "True" else "False"))

		file.write("<div class=\"settings\"><div class=\"bold\">\
			<div class=\"setting\">Results</div><div class=\"value\">Value</div></div>")
		file.write("<div><div class=\"setting\">Wins</div><div class=\"value\">%s</div></div>" % self.wins)
		file.write("<div><div class=\"setting\">Loses</div><div class=\"value\">%s</div></div>" % (games - self.wins))
		file.write("<div><div class=\"setting\">Winning Rate</div><div class=\"value\">%s</div></div>" % (self.wins / games))

		# Write inbetween
		file.write("</div></div><div class=\"results\">")

		# Calculate results (max, sum)
		hitSum = 0
		for hits in self.hits:
			hitSum += hits

		percentages = [None] * len(self.hits)
		for i in range(0, len(self.hits)):
			percentages[i] = float(self.hits[i]) / hitSum * 100.0

		maxPercentage = 0
		for percentage in percentages:
			if percentage > maxPercentage:
				maxPercentage = percentage

		# Write results
		for i in range(0, len(self.hits)):
			name = playerTile[i]
			percentage = percentages[i]
			width = percentage / maxPercentage * 100.0
			file.write("<div class=\"row\"><div class=\"name\">%s</div><div class=\"bar-container\"><div class=\"bar\" \
				style=\"width:%f%%\">%f%%</div></div></div>" % (name, width, percentage))

		# Write rest of the file
		file.write("</div></body></html>")

		# Close and write the file
		file.close()