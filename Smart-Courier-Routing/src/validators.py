import re 

def checkIfValid(data):

    # Regex for checking id Customer name is valid and single word
    customerRegex = re.compile(r"^[a-zA-ZæøåÆØÅ' -]+$")
    
    # Checks if floats are a number
    try:
        latitude = float(data["latitude"])
        longitude = float(data["longitude"])
        weight = float(data["weight"])
    except(ValueError, TypeError):
        
        return False

    # Lowecase and strip priority values so they wont be case sensetive
    priority = data["priority"].lower().strip()

    # Checks the all the values and if it gets triggered it will return false
    if not customerRegex.match(data["customer"]):

        return False
    
    elif not (-90 <= latitude <= 90):
        
        return False
    
    elif not (-180 <= longitude <= 180):
        
        return False
    
    elif priority not in ("high", "medium", "low"):
        
        return False
    
    elif  weight < 0:
    
        return False
    
    return True