from Utils.getPrice import extractPrice
from Utils.getratings import extractratings

def extractBook(book):
    img = book.find('div', attrs = {'class': 'image_container'}).a.img
    imgData = {
        'src': img.attrs['src'],
        'alt': img.attrs['alt']
    }
    price = extractPrice(book)
    
    rating = extractratings(book)

    title = book.find('h3').a.attrs['title']
    bookData = {
        'imgData': imgData,
        'price': price,
        'rating': rating,
        'title':title
    }

    return bookData