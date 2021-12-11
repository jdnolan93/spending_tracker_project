import pdb

from models.place import Place
from models.purchase import Purchase

import repositories.place_repository as place_repository
import repositories.purchase_repository as purchase_repository

place_repository.delete_all()
purchase_repository.delete_all()

place_1 = Place("The Chanter")
place_repository.save(place_1)

place_2 = Place("NQ64")
place_repository.save(place_2)

place_3 = Place("The Hive")
place_repository.save(place_3)

place_4 = Place("Caley PictureHouse")
place_repository.save(place_4)

place_5 = Place("Brewdog")
place_repository.save(place_5)


purchase_1 = Purchase("Pint", 3.50)
purchase_repository.save(purchase_1)

purchase_2 = Purchase("Cocktail", 3.50)
purchase_repository.save(purchase_2)

purchase_3 = Purchase("Tequila Shot", 2.00)
purchase_repository.save(purchase_3)

purchase_4 = Purchase("Vodka mixer", 1.00)
purchase_repository.save(purchase_4)

purchase_5 = Purchase("Red wine", 4.50)
purchase_repository.save(purchase_5)