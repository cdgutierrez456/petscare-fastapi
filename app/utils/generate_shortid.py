import shortuuid

def generate_shortid(length=4):
    """Genera un ShortID alfanumérico"""
    return shortuuid.ShortUUID().random(length=length).upper()
