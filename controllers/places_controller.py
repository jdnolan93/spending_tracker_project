from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.place import Place
import repositories.place_repository as place_repository
import repositories.purchase_repository as purchase_repository

places_blueprint = Blueprint("places", __name__)