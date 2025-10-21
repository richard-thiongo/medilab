from flask import Blueprint, request
from controllers.dependantController import DependantController

dependant_blueprint = Blueprint('dependant', __name__, url_prefix='/dependant')
dependant_controller = DependantController()

@dependant_blueprint.route('/create', methods=['POST'])
def create_dependant():
    return dependant_controller.addDependant(request)

@dependant_blueprint.route('/view', methods=['POST'])
def view_dependant():
    return dependant_controller.viewDependants(request)

@dependant_blueprint.route('/update', methods=['PUT'])
def update_dependant():
    return dependant_controller.updateDependant(request)


@dependant_blueprint.route('/getdependantbyid', methods=['POST'])
def get_dependant_by_id():
    return dependant_controller.getDependantById(request)



@dependant_blueprint.route('/get_dependant_by_member_id', methods=['POST'])
def get_dependant_by_member_id():
    return dependant_controller.getDependantByMemberId(request)



@dependant_blueprint.route('/delete', methods=['DELETE'])
def delete_dependant():
    return dependant_controller.deleteDependant(request)