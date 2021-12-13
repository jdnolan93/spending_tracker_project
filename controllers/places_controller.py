from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.place import Place
import repositories.place_repository as place_repository
import repositories.purchase_repository as purchase_repository
import repositories.tag_repository as tag_repository

places_blueprint = Blueprint("places", __name__)

@places_blueprint.route("/places")
def places():
    places = place_repository.select_all()
    return render_template("places/index.html", all_places = places)