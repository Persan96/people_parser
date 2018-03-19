import sys

first, second, third, forth, amount_of_arguments, less_than_necessary = 0, 1, 2, 3, len(sys.argv), 3
if(amount_of_arguments < less_than_necessary):
    print("Usage:\n\t $ python .\pypeople_parser.py <input_file> <output_file>\n")
    sys.exit()
persons, families, phones, addresses, inputfile, outputfile, read, write = "P", "F", "T", "A", sys.argv[1], sys.argv[2], "r", "w"
file = open(inputfile, read)
person_found = False
family_found = False
output = [ "<people>\n\t" ]
for i, line in enumerate(file):
    line.replace('\n', '').replace('\r', '')
    lines = line.split("|")
    arguments = []
    for argument in lines:
        arguments.append(argument)
    for i in range(len(lines), 4):
        arguments.append("NO-INPUT")

    if(arguments[first] != persons and arguments[first] != families and arguments[first] != phones and arguments[first] != addresses):
        print("INVALID DATA TYPE, PLEASE CONTACT DEVELOPER!")
        sys.exit()
    if (arguments[first] == persons):
        if(person_found == False):
            person_found = True
            output.append("<person><firstname>" + arguments[second] + "</firstname><lastname>" + arguments[third] + "</lastname>\n\t\t")
        else:
            if(family_found == True):
                output.append("</family>\n")
                family_found = False
            output.append("</person>\n\t\t<person><firstname>" + arguments[second] + "</firstname><lastname>" + arguments[third] + "</lastname>\n\t\t")
    if (arguments[first] == families):
        if(family_found == False):
            family_found = True
            output.append("<family><name>" + arguments[second] + "</name><birth>" + arguments[third] + "</birth>\n\t\t")
        else:
            output.append("</family>\n\t\t<family><name>" + arguments[second] + "</name><birth>" + arguments[third] + "</birth>")
    if (arguments[first] == addresses):
        output.append("<address><street>" + arguments[second] + "</street><city>" + arguments[third] + "</city><zip>" + arguments[forth] + "</zip></address>\n\t\t")
    if (arguments[first] == phones):
            output.append("<phone><mobile>" + arguments[second] + "</mobile><landline>" + arguments[third] + "</landline></phone>\n\t\t")
if(family_found == True):
    output.append("</family>\n\t\t")
output.append("</person>\n</people>")

outputfile = open(outputfile, write)

outputfile.write("".join(output))
outputfile.close()
