from page_view import PageView

# client
if __name__ == "__main__":
    page = PageView()
    page.render() # exibe a página
    print(page)   # chama método __repr__
    print(id(page))

    page2 = PageView()
    page2.render()
    print(page2)
    print(id(page2))

    page3 = PageView()
    page3.render()
    print(page3)
    print(id(page3))
