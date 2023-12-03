import webbrowser

# Декоратор нужен для выполнения кода до и после определенной функции

def validator(func):
    def wrapper(url):
        print('Before function')
        func(url)
        print('After function')
    return wrapper

@validator
def open_url(url):
    webbrowser.open(url)


open_url('https://www.google.com/')