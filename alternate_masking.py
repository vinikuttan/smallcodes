

def mask_alternate(myvalue):
    "Alternate characters masking"
    masked_data = list()
    if isinstance(myvalue, list):
        for each_item in myvalue:
            masked_data.append(mask_alternate(each_item))
        return masked_data

    elif isinstance(myvalue, int):
        return mask_alternate(str(myvalue))
        
    elif isinstance(myvalue, str):
        # masking logic
        mask = False
        for each_char in myvalue:
            mask = not mask
            if mask:
                masked_data.append('X')
            else:
                masked_data.append(each_char)
        return ''.join(masked_data)
        
    else:
        raise ValueError("Masking input should be in [integer, string,list] types")


data1 = "Hello world"
data2 = ["hello", 1234]
data3 = ["hello", "world", ["hello", "world"]]
print mask_alternate(data1)
print mask_alternate(data2)
print mask_alternate(data3)
