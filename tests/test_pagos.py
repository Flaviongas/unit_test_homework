import random
from unittest.mock import Mock, patch
 
 
days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri' , 'sat']
 
random.choice = Mock(return_value='wed')
print(random.choice())

#using patch
with patch('random.choice', return_value='wed'):
    print(random.choice(days))