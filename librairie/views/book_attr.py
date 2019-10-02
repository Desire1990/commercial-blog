from django.core.paginator import Paginator

def book_attrs(books, page):
    try:
        slide1 = books[0]
        slides = books[1:3]
    except IndexError:
        slide1 = None
        slides = None
    pages = Paginator(books, 20, orphans=8)
    page_content = pages.page(page)
    nom_app = "Livres"
    return (nom_app, slide1, slides, pages, page_content)
