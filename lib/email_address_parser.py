import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string
    
    def parse(self):
        return sorted(set(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', self.email_string)))