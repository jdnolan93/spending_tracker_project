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
    return render_template("places/index.html", places = places)

@places_blueprint.route("/places/new")
def new_place():
    return render_template("/places/new.html")

@places_blueprint.route("/places", methods=["POST"])
def create_place():
    place_name = request.form["name"]
    new_place = Place(place_name)
    place_repository.save(new_place)
    return redirect("/places")

@places_blueprint.route("/places/<id>/edit")
def edit_place(id):
    place = place_repository.select(id)
    return render_template('places/edit.html', place=place)

@places_blueprint.route("/places/<id>", methods=["POST"])
def update_place(id):
    name = request.form["name"]
    place = Place(name, id)
    place_repository.update(place)