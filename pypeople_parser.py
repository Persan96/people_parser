import sys

first_argument, second_argument, third_argument, forth_argument = 0, 1, 2, 3
persons, families, phones, addresses = "P", "F", "T", "A"
file = open(sys.argv[1], "r")
person_found = False
family_found = False
output = [ "<people>\n\t" ]
for i, line in enumerate(file):
    line.replace('\n', '').replace('\r', '')
    line_arguments = line.split("|")
    if (line_arguments[first_argument] == persons):
        if(person_found == False):
            person_found = True
            output.append("<person><firstname>" + line_arguments[second_argument] + "</firstname><lastname>" + line_arguments[third_argument] + "</lastname>\n\t\t")
        else:
            if(family_found == True):
                output.append("</family>\n")
                family_found = False
            output.append("</person>\n\t\t<person><firstname>" + line_arguments[second_argument] + "</firstname><lastname>" + line_arguments[third_argument] + "</lastname>\n\t\t")
    if (line_arguments[first_argument] == families):
        if(family_found == False):
            family_found = True
            output.append("<family><name>" + line_arguments[second_argument] + "</name><birth>" + line_arguments[third_argument] + "</birth>\n\t\t")
        else:
            output.append("</family>\n\t\t<family><name>" + line_arguments[second_argument] + "</name><birth>" + line_arguments[third_argument] + "</birth>")
    if (line_arguments[first_argument] == addresses):
        output.append("<address><street>" + line_arguments[second_argument] + "</street><city>" + line_arguments[third_argument] + "</city><zip>" + line_arguments[forth_argument] + "</zip></address>\n\t\t")
    if (line_arguments[first_argument] == phones):
            output.append("<phone><mobile>" + line_arguments[second_argument] + "</mobile><landline>" + line_arguments[third_argument] + "</landline></phone>\n\t\t")
if(family_found == True):
    output.append("</family>\n\t\t")
output.append("</person>\n</people>")

outputfile = open("output.txt", "w")

outputfile.write("".join(output))
