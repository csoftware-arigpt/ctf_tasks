def check_payload(text):
    if not text:
        return True
    
    if '--' in text or '#' in text:
        return False
        
    blacklist = ['union', 'select', 'or', 'and']
    
    for word in blacklist:
        if word in text:
            return False
            
    return True