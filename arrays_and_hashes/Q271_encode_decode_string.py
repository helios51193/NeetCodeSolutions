def encode(s):
    """
    Encodes a list of strings to a single string.
    
    :type s: List[str]
    :rtype: str
    """
    
    # edge case
    if not s:
        return ""
    
    # initialize encoded string
    encoded = ""
    
    # encode each string in the list
    for string in s:
        # get the length of the string and convert it to a string
        length = str(len(string))
        
        # add the length of the string and the string itself to the encoded string
        encoded += length + ":" + string
    
    return encoded


def decode(encoded):
    """
    Decodes a single string to a list of strings.
    
    :type encoded: str
    :rtype: List[str]
    """
    
    # edge case
    if not encoded:
        return []
    
    # initialize decoded list
    decoded = []
    
    # initialize index
    i = 0
    
    # while loop to decode the encoded string
    while i < len(encoded):
        # initialize length
        length = ""
        
        # get the length of the string
        while encoded[i] != ":":
            length += encoded[i]
            i += 1
        
        # increment i to get to the start of the string
        i += 1
        
        # get the string
        string = encoded[i:i+int(length)]
        
        # add the string to the decoded list
        decoded.append(string)
        
        # increment i to get to the start of the next string
        i += int(length)
    
    return decoded