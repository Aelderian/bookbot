def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    number_of_words = get_number_of_words(text)
    
    characters = get_number_of_characters(text)
      
    print_characters(characters,number_of_words)
    
    
    # print(characters)

def print_characters(characters,number_of_words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"Number of words: {number_of_words} \n")
    
    characters = sort_on_values(characters)

    for char, count in characters.items():
      if char.isalpha():
        print(f"The character '{char}' was found {count} times")        
    print("--- End of report ---")

def sort_on_values(dict):
  
  sort_characters = list(dict.items())
  
  sort_characters.sort(reverse = True, key=lambda x: x[1])
  
  temp_dict = {}
  for element in sort_characters:
    temp_dict[element[0]] = element[1]
    
  return temp_dict
  

def get_number_of_characters(text):
  count_characters = {}
  for word in text:
    word = word.lower()
    for char in word:  
      if char in count_characters:
        count_characters[char] += 1
      else:
        count_characters[char] = 1
        
  return count_characters

def get_book_text(path):
    with open(path) as f:
        return f.read().split()

def get_number_of_words(text):
    return len(text)

if __name__ == "__main__":
    main()