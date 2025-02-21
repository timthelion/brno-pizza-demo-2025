import jwt
import argparse
from datetime import datetime, timedelta

def create_token(username, secret, is_admin=False):
    exp = datetime.now() + timedelta(hours=2)
    exp_timestamp = int(exp.timestamp())

    mountpoint = "" if is_admin else f"/users/{username}/"

    payload = {
        "exp": exp_timestamp,
        "username": username,
        "client_attrs": {
            "mountpoint": mountpoint
        }
    }

    return jwt.encode(payload, secret, algorithm='HS256')

def main():
    parser = argparse.ArgumentParser(description='Generate JWT token with optional admin privileges')
    parser.add_argument('--username', type=str, required=True, help='Username for the token')
    parser.add_argument('--secret', type=str, default="foo", help='JWT secret')
    parser.add_argument('--admin', action='store_true', help='Generate admin token with empty mountpoint')

    args = parser.parse_args()

    token = create_token(args.username, args.secret, args.admin)
    print(token)

if __name__ == "__main__":
    main()
