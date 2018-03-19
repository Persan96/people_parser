import sys

first, second, third, forth = 0, 1, 2, 3
persons, families, phones, addresses = "P", "F", "T", "A"
file = open(sys.argv[1], "r")
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

outputfile = open("output.txt", "w")

outputfile.write("".join(output))
