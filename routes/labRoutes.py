from flask import Blueprint, request
from controllers.labController import LabController


lab_blueprint = Blueprint('lab', __name__, url_prefix='/lab')
lab_controller = LabController()

# Routes which simply forward the request to the controllers

@lab_blueprint.route('/create', methods=['POST'])
def create_lab():
    return lab_controller.createLab(request)

@lab_blueprint.route('/login', methods=['POST'])
def labLogin():
    return lab_controller.labLogin(request)

@lab_blueprint.route('/profile', methods=['POST'])
def labProfile():
    return lab_controller.labProfile(request)

@lab_blueprint.route('/update', methods=['PUT'])
def updateLab():
    return lab_controller.updateLab(request)


