# people_parser
Small test to parse a type of file to an xml file with people and their information.

# USAGE
Tested in powershell on windows 10
$ py pypeople_parser.py <file>

# EXAMPLE

Parser will recieve file looking like ex:
P|firstname|lastname
F|name|birth_year
A|address|city|zip code
T|mobile_phone_number|landline_number

and turn input file into
<people>
  <person>
    <firstname>firstname</firstname>
    <lastname>lastname</lastname>
    <family>
      <name>name</name>
      <birth>birth year</birth>
      <address>
        <street>street</street>
        <city>city</city>
        <zip>zip code</zip>
      </address>
      <phone>
        <mobile>mobile number</mobile>
        <landline>landline number</landline>
      </phone>
    </family>
  </person>
</people>
  
