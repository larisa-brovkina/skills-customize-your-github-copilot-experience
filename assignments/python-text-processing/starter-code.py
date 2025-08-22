# Starter code for Python Text Processing assignment

# Task 1: Text File Analyzer
# Complete the functions below to analyze text files

def analyze_text_file(filename):
    """
    Analyze a text file and return statistics about its content.
    """
    try:
        with open(filename, 'r') as file:
            text = file.read()
            
        # TODO: Implement the following calculations:
        # - Count lines, words, characters
        # - Find most frequent words (top 5)
        # - Calculate average word length
        # - Find longest and shortest sentences
        
        # Example structure for your results:
        stats = {
            'characters': 0,
            'words': 0,
            'lines': 0,
            'average_word_length': 0.0,
            'most_frequent_words': [],
            'longest_sentence': '',
            'shortest_sentence': ''
        }
        
        return stats
        
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
        return None

# Task 2: Text Formatter and Cleaner
def clean_and_format_text(input_filename, output_filename):
    """
    Clean and format text from input file and save to output file.
    """
    try:
        with open(input_filename, 'r') as file:
            text = file.read()
        
        # TODO: Implement text cleaning:
        # - Remove extra whitespace and blank lines
        # - Convert to title case
        # - Replace multiple punctuation marks
        # - Remove/replace special characters
        
        cleaned_text = text  # Replace with your cleaning logic
        
        with open(output_filename, 'w') as file:
            file.write(cleaned_text)
            
        print(f"Text cleaned and saved to {output_filename}")
        
    except FileNotFoundError:
        print("Input file not found.")

# Task 3: Word Search and Replace Tool
def search_and_replace(filename, search_term, replace_term, case_sensitive=True):
    """
    Search for terms in a file and replace them.
    """
    try:
        # TODO: Create backup file first
        
        with open(filename, 'r') as file:
            text = file.read()
        
        # TODO: Implement search and replace logic
        # - Handle case sensitivity
        # - Count replacements made
        # - Save changes to file
        
        replacements_made = 0  # Count actual replacements
        
        print(f"Replaced {replacements_made} occurrences of '{search_term}' with '{replace_term}'")
        
    except FileNotFoundError:
        print("File not found.")

# Main program - uncomment and modify to test your functions
if __name__ == "__main__":
    # Test your functions here
    filename = input("Enter filename to analyze: ")
    
    # Test Task 1
    # stats = analyze_text_file(filename)
    # if stats:
    #     print("\n=== File Analysis ===")
    #     print(f"Characters: {stats['characters']}")
    #     print(f"Words: {stats['words']}")
    #     print(f"Lines: {stats['lines']}")
    
    # Test Task 2
    # clean_and_format_text(filename, "cleaned_" + filename)
    
    # Test Task 3
    # search_term = input("Enter search term: ")
    # replace_term = input("Enter replacement term: ")
    # search_and_replace(filename, search_term, replace_term)
