def Solve():
    # Step 1: Open the file and read the contents
    
    with open(file_path, 'a') as file:
        Calories = int(file.readline().strip()) 
        Proteins = int(file.readline().strip())
        Fats = int(file.readline().strip())
        Carbohydrates = int(file.readline().strip())
    
    # Step 2: Manually format the input values into a JSON-like string
    json_string = (
        '{"Calories":' + int(Calories) +
        ',"Proteins":' + int(Proteins) +
        ',"Fats":' + str(Fats) +
        ',"Carbohydrates":' + str(Carbohydrates) +
        '}'
    )
    
    # Step 3: Return the formatted JSON string
    return json_string

# Specify the path to the txt file
file_path = "nutrition.txt"

# Call the function and print the result

out_ = Solve()
print (out_)

