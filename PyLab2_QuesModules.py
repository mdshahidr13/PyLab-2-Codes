class ListOperations:
    def __init__(self, data):
        if not data:
            raise ValueError("The list cannot be empty.")
        self.data = data

    def get_max(self):
        return max(self.data)

    def get_min(self):
        return min(self.data)

    def calculate_sum(self):
        return sum(self.data)

    def calculate_average(self):
        return sum(self.data) / len(self.data)

    def find_median(self):
        sorted_data = sorted(self.data)
        length = len(sorted_data)
        midpoint = length // 2
        if length % 2 == 0:
            return (sorted_data[midpoint - 1] + sorted_data[midpoint]) / 2
        else:
            return sorted_data[midpoint]

        
# module_SetOperations.py

class SetOperations:
    def __init__(self, set_a, set_b):
        self.set_a = set_a
        self.set_b = set_b
    
    def add_to_set_a(self, item):
        self.set_a.add(item)
    
    def remove_from_set_a(self, item):
        self.set_a.discard(item)

    def get_union_and_intersection(self):
        combined_set = self.set_a.union(self.set_b)
        common_elements = self.set_a.intersection(self.set_b)
        return combined_set, common_elements

    def get_difference(self):
        return self.set_a.difference(self.set_b)

    def is_set_a_subset_of_set_b(self):
        return self.set_a.issubset(self.set_b)

    def count_elements_in_set_a(self):
        count = 0
        for _ in self.set_a:
            count += 1
        return count

    def get_symmetric_difference(self):
        return self.set_a.symmetric_difference(self.set_b)

    def generate_power_set(self):
        subsets = [[]]
        for element in self.set_a:
            subsets += [subset + [element] for subset in subsets]
        return [set(subset) for subset in subsets]

    def generate_unique_subsets(self):
        def create_subsets(current_set, index):
            if index == len(self.set_a):
                all_subsets.append(set(current_set))
                return
            create_subsets(current_set, index + 1)
            create_subsets(current_set + [list(self.set_a)[index]], index + 1)

        all_subsets = []
        create_subsets([], 0)
        return all_subsets



# dict_operations.py

class DictionaryUtils:
    def __init__(self, *dictionaries):
        self.dictionaries = dictionaries
    
    def combine_dictionaries(self):
        combined = {}
        for d in self.dictionaries:
            if isinstance(d, dict):
                combined.update(d)
            else:
                raise TypeError("All inputs must be dictionaries.")
        return combined

    def find_common_keys(self):
        if not self.dictionaries:
            return set()
        common_keys = set(self.dictionaries[0].keys())
        for d in self.dictionaries[1:]:
            if isinstance(d, dict):
                common_keys.intersection_update(d.keys())
            else:
                raise TypeError("All inputs must be dictionaries.")
        return common_keys

    def reverse_dictionary(self, dictionary):
        if not isinstance(dictionary, dict):
            raise TypeError("Input must be a dictionary.")
        
        reversed_dict = {}
        for key, value in dictionary.items():
            if value in reversed_dict:
                if isinstance(reversed_dict[value], list):
                    reversed_dict[value].append(key)
                else:
                    reversed_dict[value] = [reversed_dict[value], key]
            else:
                reversed_dict[value] = key
        return reversed_dict

    def find_common_key_value_pairs(self):
        if not self.dictionaries:
            return set()
        
        common_pairs = set(self.dictionaries[0].items())
        for d in self.dictionaries[1:]:
            if isinstance(d, dict):
                common_pairs.intersection_update(d.items())
            else:
                raise TypeError("All inputs must be dictionaries.")
        return common_pairs


# LibraryManager.py

class LibraryHandler:
    def __init__(self):
        self.collection = {}

    def add_book(self, title, author, publisher, volume, publication_year, isbn):
        if isbn in self.collection:
            raise ValueError("A book with this ISBN already exists.")
        self.collection[isbn] = {
            'title': title,
            'author': author,
            'publisher': publisher,
            'volume': volume,
            'year': publication_year,
            'isbn': isbn
        }

    def remove_book(self, isbn):
        if isbn not in self.collection:
            raise ValueError("No book found with this ISBN.")
        del self.collection[isbn]

    def get_book_info(self, isbn):
        return self.collection.get(isbn, "Book not found.")

    def search_books_by_query(self, query):
        results = []
        for book in self.collection.values():
            if query.lower() in book['title'].lower() or query.lower() in book['author'].lower():
                results.append(book)
        return results

    def list_all_books(self):
        return list(self.collection.values())

    def update_book_info(self, isbn, **details):
        if isbn not in self.collection:
            raise ValueError("No book found with this ISBN.")
        self.collection[isbn].update(details)

    def is_book_available(self, isbn):
        return isbn in self.collection

