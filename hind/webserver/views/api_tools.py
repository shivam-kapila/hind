from flask.globals import request
from werkzeug.exceptions import BadRequest
from flask import request

 
def _get_non_negative_param(param, default=None):
    """ Gets the value of a request parameter, validating that it is non-negative
    Args:
        param (str): the parameter to get
        default: the value to return if the parameter doesn't exist in the request
    """
    value = request.args.get(param, default)
    if value is not None:
        try:
            value = int(value)
        except ValueError:
            raise BadRequest("'{}' should be a non-negative integer".format(param))

        if value < 0:
            raise BadRequest("'{}' should be a non-negative integer".format(param))
    return value
