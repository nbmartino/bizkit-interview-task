from flask import Blueprint, request

from .data.search_data import USERS

from .pd_search import pd_search_users,pd_sorted_search_users


bp = Blueprint("search", __name__)


@bp.route("/search")
def search():
    return search_users(request.args.to_dict()), 200

@bp.route("/search_v2")
def sorted_search():
    return sorted_search_users(request.args.to_dict()), 200

def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    
    return pd_search_users(args,USERS)


def sorted_search_users(args):
    return pd_sorted_search_users(args, USERS)
 