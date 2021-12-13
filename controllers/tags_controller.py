from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.purchase import Purchase
import repositories.place_repository as place_repository
import repositories.purchase_repository as purchase_repository
import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)