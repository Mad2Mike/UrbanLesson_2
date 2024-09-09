calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(string: str):
    global calls
    calls += 1
    st_ln = len(string)
    st_up = string.upper()
    st_dn = string.lower()
    str_info = (st_ln, st_up, st_dn)
    return str_info

def is_contains(string: str, list_to_search: list):
    global calls
    calls += 1
    if string.lower() in (i.lower() for i in list_to_search):
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
exit()
