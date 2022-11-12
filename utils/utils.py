import math
from flask import jsonify


def int_try_parse(input):
    try:
        return int(input), True
    except ValueError:
        return input, False


def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True

  
def map_error_to_response(e):
        return jsonify({
        "status_code": e.status_code,
        "eror_code": e.error_code,
        "message": e.message})


def success_response(txt):
        return jsonify({
        "status_code": 200,
        "message": txt})