#Question 1 code
print("-----------------Question 1 code-------------------")

from PyLab2_QuesModules import ListOperations

data = [50, 20, 46, 23, 90, 30, 55]

def demonstrate_list_operations(data):
    operations = ListOperations(data)
    print("List:", data)
    print("Max Value:", operations.get_max())
    print("Min Value:", operations.get_min())
    print("Total Sum:", operations.calculate_sum())
    print("Average Value:", operations.calculate_average())
    print("Median Value:", operations.find_median())
    print()

demonstrate_list_operations(data)

print("-----------------------------------------------------")

#Question 2 code
print("\n------------------Question 2 code-------------------\n")
# main_SetOperations.py

from PyLab2_QuesModules import SetOperations

def execute_set_operations():
    set_a = {7, 14, 21}
    set_b = {21, 28, 35}
    
    operations = SetOperations(set_a, set_b)
    
    print("Starting Sets:")
    print("Set1:", operations.set_a)
    print("Set2:", operations.set_b)
    print()

    operations.add_to_set_a(28)
    print("Set1 after adding 28:", operations.set_a)

    operations.remove_from_set_a(14)
    print("Set1 after removing 14:", operations.set_a)

    union_result, intersection_result = operations.get_union_and_intersection()
    print("Union of Set1 and Set2:", union_result)
    print("Intersection of Set1 and Set2:", intersection_result)

    difference_result = operations.get_difference()
    print("Difference (Set1 - Set2):", difference_result)

    is_subset_result = operations.is_set_a_subset_of_set_b()
    print("Is Set1 a subset of Set2?", is_subset_result)

    length_of_set1 = operations.count_elements_in_set_a()
    print("Number of elements in Set1:", length_of_set1)

    symmetric_diff_result = operations.get_symmetric_difference()
    print("Symmetric Difference of Set1 and Set2:", symmetric_diff_result)

    power_set_result = operations.generate_power_set()
    print("Power Set of Set1:", power_set_result)

    unique_subsets_result = operations.generate_unique_subsets()
    print("Unique Subsets of Set1:", unique_subsets_result)

execute_set_operations()
print("\n------------------------------------------------------\n")

#Question 3 code
print("-------------------Question 3 code----------------------\n")

from PyLab2_QuesModules import DictionaryUtils

def perform_dictionary_operations():
    dicta = {'x': 10, 'y': 20, 'z': 30}
    dictb = {'x': 10, 'w': 40, 'v': 50}

    operations = DictionaryUtils(dicta, dictb)

    # Combining dictionaries
    combined_dict = operations.combine_dictionaries()
    print("Combined Dictionary:")
    print(combined_dict)
    print()
    
    # Identifying common keys
    common_keys_result = operations.find_common_keys()
    print("Common Keys:")
    print(common_keys_result)
    print()
    
    # Reversing dictionary keys and values
    reversed_dict = operations.reverse_dictionary(dicta)
    print("Reversed Dictionary:")
    print(reversed_dict)
    print()
    
    # Finding shared key-value pairs
    shared_key_value_pairs = operations.find_common_key_value_pairs()
    print("Shared Key-Value Pairs:")
    print(shared_key_value_pairs)
    print()

perform_dictionary_operations()

print("---------------------------------------------------------\n")


print("----------------------Question 4 code----------------------\n")
# main.py
from PyLab2_QuesModules import LibraryHandler

def manage_library():
    lib_manager = LibraryHandler()
    
    lib_manager.add_book("Introduction to Algorithms", "Thomas H. Cormen", "MIT Press", "4th", 2022, "9780262033848")
    lib_manager.add_book("Deep Learning", "Ian Goodfellow", "MIT Press", "1st", 2023, "9780262038034")
    lib_manager.add_book("Artificial Intelligence: A Modern Approach", "Stuart Russell", "Pearson", "3rd", 2021, "9780136042594")
    
    # Remove a book
    lib_manager.remove_book("9780262038034")
    
    # Retrieve book details
    print("Details of the book with ISBN 9780136042594:", lib_manager.get_book_info("9780136042594"))
    
    # Search for books
    print("Search results for 'Deep Learning':", lib_manager.search_books_by_query("Deep Learning"))
    
    # List all books
    print("Books available in the library:", lib_manager.list_all_books())
    
    # Update book details
    lib_manager.update_book_info("9780136042594", volume="4th", year=2024)
    
    # Check book availability
    print("Is the book with ISBN 9780136042594 currently in the library?", lib_manager.is_book_available("9780136042594"))

manage_library()

print("\n-------------------------------------------------------------------\n")

#Question 5 code
print("----------------------Question 5 code----------------------\n")

weather_data = [
    {"date": "2024-07-22", "max_temp": 35, "min_temp": 25, "humidity": 80},
    {"date": "2024-07-23", "max_temp": 32, "min_temp": 24, "humidity": 70},
    {"date": "2024-07-24", "max_temp": 30, "min_temp": 22, "humidity": 65},
    {"date": "2024-07-25", "max_temp": 28, "min_temp": 21, "humidity": 60},
    {"date": "2024-07-26", "max_temp": 33, "min_temp": 23, "humidity": 75},
    {"date": "2024-07-27", "max_temp": 36, "min_temp": 26, "humidity": 85},
    {"date": "2024-07-28", "max_temp": 34, "min_temp": 24, "humidity": 77}
]

def find_temperature_extremes(weather_data):
    highest_temp = max(record['max_temp'] for record in weather_data)
    lowest_temp = min(record['min_temp'] for record in weather_data)
    return highest_temp, lowest_temp

def count_days_exceeding_30(weather_data):
    count = sum(1 for record in weather_data if record['max_temp'] > 30)
    return count

def calculate_average_humidity(weather_data):
    total_humidity = sum(record['humidity'] for record in weather_data)
    average_humidity = total_humidity / len(weather_data)
    return average_humidity

highest_temp, lowest_temp = find_temperature_extremes(weather_data)
days_above_30 = count_days_exceeding_30(weather_data)
average_humidity = calculate_average_humidity(weather_data)

print(f"Highest Temperature: {highest_temp}°C")
print(f"Lowest Temperature: {lowest_temp}°C")
print(f"Number of days with temperatures exceeding 30°C: {days_above_30}")
print(f"Average Humidity: {average_humidity:.2f}%")


print("--------------------------------------------------------")