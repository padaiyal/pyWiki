import datetime
from functools import wraps
from flask import Flask, request, jsonify, make_response, Response
import jwt
from werkzeug.security import check_password_hash, generate_password_hash

""" 
References
 - https://datatracker.ietf.org/doc/html/rfc7519
 - https://www.bacancytechnology.com/blog/flask-jwt-authentication
 - https://blog.angular-university.io/angular-jwt/
"""

app = Flask(__name__)
"""
This is the secret key used to sign the JWT.
NOTE: This shouldn't be hardcoded in the program, instead placed in a configuration file outside the code with 
restrictive file permissions.
"""
app.config['SECRET_KEY'] = '004f2af45d3a4e161a7dd2d17fdae47f'


def is_valid_user_credentials(username: str, password: str) -> bool:
    """
    Checks if the provided user credentials are valid.
    :param username: Username.
    :param password: Plaintext password.
    :return: True if the credentials are valid. Else False.
    """
    # NOTE: The username and password hashes are usually verified from a database.
    expected_username = "testuser"
    expected_password_hash = generate_password_hash("dedewdewdew")

    if username != expected_username:
        return False
    elif not check_password_hash(expected_password_hash, password):
        return False
    return True


@app.route('/login', methods=['POST'])
def login_user() -> Response:
    """
    Handler for the user authentication.
    :return: If successful, returns a 200 status code with the JWT. Else, returns the appropriate error status code.
    """
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response(
            'could not verify',
            401,
            {'Authentication': 'login required"'}
        )

    if is_valid_user_credentials(auth.username, auth.password):
        token = jwt.encode(
            {
                'public_id': auth.username,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=45)
            },
            app.config['SECRET_KEY'],
            "HS256"
        )
        """
        An encoded JWT will look like this: 
            eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9
            .eyJwdWJsaWNfaWQiOiJ0ZXN0dXNlciIsImV4cCI6MTYzMjgzNzA5NH0
            .WYim4hf84SsQ5Eitc3TXQAc3PO7TbYtbDV2E3SDBxsA
        This is the base64 representation of: 
            {"typ":"JWT","alg":"HS256"}
            {"public_id":"testuser","exp":1632837094}
            b)8J9+\5;bWa7H0q
        
        Both the base64 and plaintext representation of the JWT has 3 parts.
         - Header aka JSON Object Signing and Encryption (JOSE) header : Contains metadata on JWT. 
           Eg: Type of signature etc
         - Payload : The actual user and session information.
         - Signature : A signature of the Header and Payload only verifiable by the server that has the private key 
         that signed it.
        """

        return jsonify({'token': token})

    return make_response(
        'could not verify',
        401,
        {'Authentication': '"login required"'}
    )


def token_required(f):
    """
    Decorator to handle JWT verification.
    :param f: Handler function to decorate.
    :return: The decorator.
    """
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            print(type(data))
            print(data.keys())
            current_user = data["public_id"]
        except Exception as e:
            print(e)
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)

    return decorator


@app.route('/')
@token_required
def hello(user: str = "Unknown"):
    """
    A sample handler to demonstrate JWT validation.
    :param user: Input username.
    :return: A user greeting.
    """
    return f"Hello, {user}!"


if __name__ == "__main__":
    # Run the web server so that it can be accessed by any host on the network via port 5001.
    app.run(host="0.0.0.0", port=5001)
