nums = [5, 6, 7, 7, 1, 9, 111, 1, 5, 1, 1]

hash_map = dict()

for i in range(0, len(nums)):
    hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
print(hash_map)


# The get() method is used to safely retrieve a value from a dictionary using its key.
# It allows you to specify a default value to return if the key doesn’t exist, instead of raising an error.

# Syntax:-
# dictionary.get(key, default_value)

# key: The key you want to look up.
# default_value (optional): The value to return if the key is NOT found.

# Defaults to None if not provided.


# eg 1:- If the key doesn’t exist, returns None.

# user = {"name": "Alice", "age": 25}
# print(user.get("email"))      # Output: None


# eg 2:-

# user = {"name": "Alice"}

# # Direct access
# # user["age"]           --> Raises KeyError

# # get method
# user.get("age")              # Returns None, no error
# user.get("age", "N/A")       # Returns "N/A"


# Why use get()? :-
# Doesn’t raise a KeyError if the key doesn’t exist.
