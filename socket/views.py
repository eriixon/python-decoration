def index():
    with open('pages/index.html') as temp:
        return temp.read()


def blog():
    with open('pages/blog.html') as temp:
        return temp.read()
