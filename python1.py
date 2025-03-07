def count_vowels(word):
    # Define vowels (both lowercase and uppercase)
    vowels = 'aeiouAEIOU'
    # Count vowels in the word
    return sum(1 for char in word if char in vowels)

def process_string(input_string):
    # Split the string into words
    words = input_string.split()
    
    # Process each word and store results
    results = []
    for word in words:
        vowel_count = count_vowels(word)
        results.append(f"{word} ({vowel_count})")
    
    # Join results with spaces and return
    return " ".join(results)

# Test the program
def main():
    # Get input from user
    text = input("Enter a string: ")
    
    # Process and print the result
    result = process_string(text)
    print(result)

# Run the program
if __name__ == "__main__":
    main()