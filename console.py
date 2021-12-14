import pdb

from models.place import Place
from models.purchase import Purchase
from models.tag import Tag

import repositories.place_repository as place_repository
import repositories.purchase_repository as purchase_repository 
import repositories.tag_repository as tag_repository

place_repository.delete_all()
purchase_repository.delete_all()

place_1 = Place("The Chanter")
place_repository.save(place_1)

place_2 = Place("Greggs")
place_repository.save(place_2)

place_3 = Place("Tesco")
place_repository.save(place_3)

tag_1 = Tag("Pint", True)

tag_2 = Tag("Steak Bake", False)

tag_3 = Tag("Meal Deal", False)

purchase_1 = Purchase(3.50, place_1, tag_1)
purchase_repository.save(purchase_1)

purchase_2 = Purchase(1.50, place_2, tag_2)
purchase_repository.save(purchase_2)

purchase_3 = Purchase(3.00, place_3, tag_3)
purchase_repository.save(purchase_3)

