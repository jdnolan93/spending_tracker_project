from flask import Flask, render_template, request, redirect
from flask import Blueprint
# from controllers.places_controller import places
from models.purchase import Purchase
import repositories.place_repository as place_repository
import repositories.purchase_repository as purchase_repository
import repositories.tag_repository as tag_repository

purchases_blueprint = Blueprint("purchases", __name__)

@purchases_blueprint.route("/purchases")
def purchases():
    pre_total = purchase_repository.total_amount()
    purchases = purchase_repository.select_all()
    total = round(pre_total, 2)
    return render_template("purchases/index.html", purchases = purchases, total=total)

@purchases_blueprint.route("/purchases/new")
def new_purchase():
    places = place_repository.select_all()
    tags = tag_repository.select_all()
    return render_template ("/purchases/new.html", places = places, tags = tags)

@purchases_blueprint.route("/purchases", methods=["POST"])
def create_purchase():
    place_id = request.form["place_id"]
    tag_id = request.form["tag_id"]
    price = request.form["price"]

    place = place_repository.select(place_id)
    tag = tag_repository.select(tag_id)
    new_purchase = Purchase(price, place, tag)
    purchase_repository.save(new_purchase)

    return redirect("/purchases/index.html")

# @purchases_blueprint("/purchases/<id>/edit")
# def edit_purchase(id):
#     purchase = purchase_repository.select(id)
#     places = place_repository.select_all()
#     tags = tag_repository.select_all()
#     return render_template("purchases/edit.html", purchase = purchase, places = places, tags = tags) 
# # NEED TO WORK OUT WHY ITS NOT WORKING 

