target_book = input()
current_text = input()
books_searched = 0

while (current_text != 'No More Books'):
  if current_text == target_book:
    print(f'You checked {books_searched} books and found it.')
    exit()

  books_searched += 1
  current_text = input()

print(f'The book you search is not here!\nYou checked {books_searched} books.')
