def parse_encoded_string(encoded_string):
    parts=encoded_string.split("000")
    return {"first_name":parts[0], "last_name":parts[1], "id":parts[2]}

encoded_data="Shiven000Aggarwal000283"
result=parse_encoded_string(encoded_data)
print(result)