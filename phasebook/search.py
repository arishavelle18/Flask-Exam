from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


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
    arr = []
    # check all the users
    for argUser in USERS:
        check = False
        # loop the keys
        for argUserKey in argUser.keys():
            # loop the args key
            for arg in args.keys():
                # check if the key is the same
                if arg == "id":
                    if argUser[argUserKey] == args[arg]:
                        if check == False:
                            arr.append(argUser)
                            check = True
                elif arg == "age":
                    if argUser[argUserKey] == int(args[arg]) or argUser[argUserKey] == int(args[arg]) + 1 or argUser[argUserKey] == int(args[arg]) - 1:
                        if check == False:
                            arr.append(argUser)
                            check = True
                # check if arg is name and occupation
                elif arg == "name" and argUserKey == "name" or arg == "occupation" and argUserKey == "occupation":
                    if args[arg].lower() in argUser[argUserKey].lower() :
                        if check == False:
                            arr.append(argUser)
                            check = True
                
                # if argUser[argUserKey] == args[arg]:
                #     if check == False:
                #         a["as"].append(argUser)
                #         check = True
    
    # return USERS
    return arr if len(args) != 0 else USERS
