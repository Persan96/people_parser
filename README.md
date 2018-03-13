# people_parser
Small test to parse a type of file to an xml file with people and their information.

# USAGE
Tested in powershell on windows 10\n
$ py pypeople_parser.py <file>

# EXAMPLE

Parser will recieve file looking like ex:\n
P|firstname|lastname\n
F|name|birth_year\n
A|address|city|zip code\n
T|mobile_phone_number|landline_number\n

and turn input file into\n
<people>\n
  <person>\n
    <firstname>firstname</firstname>\n
    <lastname>lastname</lastname>\n
    <family>\n
      <name>name</name>\n
      <birth>birth year</birth>\n
      <address>\n
        <street>street</street>\n
        <city>city</city>\n
        <zip>zip code</zip>\n
      </address>\n
      <phone>\n
        <mobile>mobile number</mobile>\n
        <landline>landline number</landline>\n
      </phone>\n
    </family>\n
  </person>\n
</people>
  
