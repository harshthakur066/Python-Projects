import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + str(query_char)
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_password_leakes_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            # print(count)
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf8')).hexdigest().upper()
    first5_char, rest = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    # print(response)
    return get_password_leakes_count(response, rest)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f'{password} was found {count} times... you should probably change it!')
        else:
            print(f'{password} was not found. Carry on!')
    return print('done!')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
