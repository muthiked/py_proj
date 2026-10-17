print("hello world")
def hello():
    print("hello new world")

def hellos():
    print("hello def world")

# Function to get a list of adult passengers' names
def get_adult_names(passenger_dict):
    is_adult = lambda age: age >= 18
    return [name for name, age in passenger_dict if  is_adult]


# Example usage
passenger_dict = {
    "Alice": 30,
    "Bob": 17,
    "Charlie": 22,
    "David": 15
}
adults = get_adult_names(passenger_dict)
print(adults)  # Expected Output: ['Alice', 'Charlie']
if __name__ == '__main__':
    hello( )