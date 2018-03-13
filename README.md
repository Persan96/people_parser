# people_parser
Small test to parse a type of file to an xml file with people and their information.

# USAGE
Tested in powershell on windows 10

$ py pypeople_parser.py <file>

# EXAMPLE

Parser will recieve file looking like ex:

P|firstname|lastname

F|name|birth_year

A|address|city|zip_code

T|mobile_phone_number|landline_number

and turn input file into:

``
<people>

  <person>
  
    <firstname>firstname</firstname>
    
    <lastname>lastname</lastname>
    
    <family>
    
      <name>name</name>
      
      <birth>birth_year</birth>
      
      <address>
      
        <street>address</street>
        
        <city>city</city>
        
        <zip>zip_code</zip>
        
      </address>
      
      <phone>
      
        <mobile>mobile_phone_number</mobile>
        
        <landline>landline_number</landline>
        
      </phone>
      
    </family>
    
  </person>
  
</people>
``
