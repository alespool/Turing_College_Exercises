from pprint import pprint

def passwd_to_dict(file):
    users = {}
    with open(file) as passwd:
        for line in passwd:

            # ignore lines that start with # or newline
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')

                # if the username string doesn't start with a letter, remove first char
                if not user_info[0].isalpha():
                    user_info[0] = user_info[0][1:]

                # the username is the key, the ID the value of our dictionary
                users[user_info[0]] = int(user_info[2])

    pprint(users, width = 20)

    return users

file = "~/Exercises/passwd.txt"

passwd_to_dict(file)
