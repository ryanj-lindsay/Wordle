from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def rand_word():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://perchance.org/fiveletter')

    try:
        iframe = driver.find_element(By.CSS_SELECTOR, '#outputIframeEl')
        driver.switch_to.frame(iframe)
        word = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#output-container > main > section:nth-child(1) > p')))
        return word.text
    finally:
        driver.quit()
    
def check_word(wordle, player_word): 
    correct = 0
    i = 0
    for char in wordle:
        if char in player_word:
            correct += 1
        if wordle[i] == player_word[i]:
            print("The letter", char, "is in the", i + 1, "position!")
        i += 1
    if player_word == wordle:
        return correct, True
    else:
        return correct, False
        
def main():
    word = rand_word()
    attempts = 5
    game = True
    print("You have", attempts, "attempt(s) remaining")
    while game:
        player_guess = input("Enter a five letter word or enter stop to quit: ")
        lower_word = player_guess.lower()
        if player_guess == "stop":
            print("Stopping game")
            game = False
        elif len(lower_word) != 5 or not lower_word.isalpha():
            print("Please enter a five letter word") 
        else:
            result = check_word(word, lower_word)
            if result == (5, True):
                print(f"Great job! You guessed", word,"in",6 - attempts,"attempt(s)!")
                game = False
            else:
                print(f"You have", result[0], "letter(s) correct keep trying!")
                attempts -= 1
                print("You have", attempts, "attempt(s) remaining")
                if attempts == 0:
                    print("You ran out of attempts! The word was,",word)
                    game = False

if __name__ == '__main__':
    main()