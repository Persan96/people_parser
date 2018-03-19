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

``` 
<people>
	<person><firstname>Carl Gustaf</firstname><lastname>Bernadotte
</lastname>
		<phone><mobile>0768-101801</mobile><landline>08-101801
</landline></phone>
		<address><street>Drottningholms slott</street><city>Stockholm</city><zip>10001
</zip></address>
		<family><name>Victoria</name><birth>1977
</birth>
		<address><street>Haga Slott</street><city>Stockholm</city><zip>10002
</zip></address>
		</family>
		<family><name>Carl Philip</name><birth>1979
</birth><phone><mobile>0768-101802</mobile><landline>08-101802
</landline></phone>
		</family>
</person>
		<person><firstname>Barack</firstname><lastname>Obama
</lastname>
		<address><street>1600 Pennsylvania Avenue</street><city>Washington, D.C
</city><zip>NO-INPUT</zip></address>
		</person>
</people>
