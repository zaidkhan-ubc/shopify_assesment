import sys

braille_map = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e', 'OOO...': 'f',
    'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j', 'O...O.': 'k', 'O.O.O.': 'l',
    'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o', 'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r',
    '.OO.O.': 's', '.OOOO.': 't', 'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x',
    'OO.OOO': 'y', 'O..OOO': 'z', '......': ' ' 
}

text_map = {x: i for i, x in braille_map.items()}
numbers = ['j', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
braille_capital = '.....O' 
braille_number = '.O.OOO'  

def braille_to_text(braille: str) -> str:
    english_text = ''
    capital = False
    number = False

    braille_chars = [braille[i:i+6] for i in range(0, len(braille), 6)]
    for char in braille_chars:
        if char == '......':
            english_text += ' '
            number = False
            continue
        if char == braille_capital: 
            capital = True
            continue
        if char == braille_number:  
            number = True
            continue

        if char in braille_map:
            temp_letter = braille_map[char]
            if number:
                if temp_letter in numbers:
                    temp_letter = str(numbers.index(temp_letter))
            if capital:
                temp_letter = temp_letter.upper()
                capital = False
            english_text += temp_letter
        else:
            english_text += '?'
    
    return english_text


def text_to_braille(text: str) -> str:
    braille_text = ''
    number_mode = False  
    for char in text:
        if char.isupper():
            braille_text += braille_capital 
            char = char.lower()  
        
        if char.isdigit():
            if not number_mode:
                braille_text += braille_number 
                number_mode = True
            char = numbers[int(char)]
        else:
            number_mode = False  
        if char == ' ':
            braille_text += '......' 
        elif char in text_map:
            braille_text += text_map[char]
        
    return braille_text



def translate(input_text):
    unique_chars = set(input_text)
    if len(unique_chars) > 2:
        input_type = "text"
    else:
        input_type = "braille"

    if input_type == "braille":
        return braille_to_text(input_text)
    else:
        return text_to_braille(input_text)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    input_text = ' '.join(sys.argv[1:])
    final_output = translate(input_text)
    
    print(final_output, end='')
