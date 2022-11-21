import PIL.ImageOps
import io

from flask import Flask, request, send_file
from datetime import datetime
from PIL import Image
from utils.utils import map_error_to_response,success_response,int_try_parse,is_prime

from auth.service import login_user, create_user,authenticate_user
from auth.helpers import auth_data_check
from auth.exceptions import InvalidNumberError, AppError


app = Flask(__name__)


@app.route("/prime/<input>", methods=["GET"])
def check_prime_number(input):
    try:
        number, isNumber = int_try_parse(input)

        if not isNumber:
            raise InvalidNumberError()

        isPrime = is_prime(number)
        decided = 'jest' if isPrime else 'nie jest'

        return success_response(f"Podana liczba {decided} liczbą pierwszą")

    except AppError as e:
        return map_error_to_response(e)


@app.route("/picture/invert", methods=["POST"])
def reverse_image_colors():
    requestImage = request.get_data()

    imageBytes = io.BytesIO(requestImage)
    image = Image.open(imageBytes)
    invertedImage = PIL.ImageOps.invert(image.convert('RGB'))

    img_byte_arr = io.BytesIO()
    invertedImage.save(img_byte_arr, format='jpeg')
    img_byte_arr = img_byte_arr.getvalue()

    return send_file(
        io.BytesIO(img_byte_arr),
        mimetype='image/jpeg',
        as_attachment=True,
        attachment_filename='inverted.jpg')


@app.route("/register", methods=["POST"])
def signup():
    try:
        auth_data_check()
        create_user(request.json["email"], request.json["password"])
        return success_response("Udało się stworzyć nowe konto")

    except AppError as e:
        return map_error_to_response(e)


@app.route("/login", methods=["POST"])
def login():
    try:
        auth_data_check()
        token = login_user(request.json["email"], request.json["password"])
        return success_response(token)
    
    except AppError as e:
        return map_error_to_response(e)


@app.route("/time", methods=["GET"])
def time():
    try:
        authenticate_user()
        return success_response(datetime.now())
        
    except AppError as e:
        return map_error_to_response(e)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
