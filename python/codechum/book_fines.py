books = int(input('Enter number of books: '))
book_kept = [int(book) for book in input('Enter days kept: ').split()[:books]]
raw_fines = [(book-7)*5 for book in book_kept if book >7]
final_fines = [50 if fine > 50 else fine for fine in raw_fines]
print('Total fine:', sum(final_fines))
