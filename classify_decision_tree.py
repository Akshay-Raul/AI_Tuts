def classify(animal)
	if animal.lays_eggs:
		if animal.swimming:
			if animal.legs>0:
				return crocodile
			else:
				return fish
		else:
			return bird
	else:
		if animal.is_carnivore:
			if animal.is_domestic:
				if animal.can_climb:
					return cat
				else:
					return dog
			else:
				if animal.can_climb:
					if animal.legs>2
						return racoon
					else:
						return monkey
				else:
					return wolf
		else:
			if animal.can_climb:
				return loris
			else:
				return giraffe