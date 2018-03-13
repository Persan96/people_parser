#Importera sys för att ta in argument
import sys

#Open file
file = open(sys.argv[1], "r")
person_found = False
family_found = False
#Variable to store output
output = [ "<people>\n" ]
#loop over each line in file
for i, line in enumerate(file):
    #remove newlines
    line.replace('\n', '').replace('\r', '')
    #Split line with | as delimiter
    line_arguments = line.split("|")
    #check first character for definition
    if (line_arguments[0] == "P"):
        #If this person is the first found person continue to set person found to true too keep track, and append user information on person
        if(person_found == False):
            person_found = True
            output.append("<person>\n<firstname>" + line_arguments[1] + "</firstname>\n<lastname>" + line_arguments[2] + "</lastname>\n")
        #If person found is set to True check if family is found and end person to start a new person
        else:
            #If family is set to true, end family and set to false
            if(family_found == True):
                output.append("</family>\n")
                family_found = False
            output.append("</person>\n<person>\n<firstname>" + line_arguments[1] + "</firstname>\n<lastname>" + line_arguments[2] + "</lastname>\n")
    #If family found
    if (line_arguments[0] == "F"):
        #If family found is set to false, set family found to true and start family
        if(family_found == False):
            family_found = True
            output.append("<family>\n<name>" + line_arguments[1] + "</name>\n<birth>" + line_arguments[2] + "</birth>\n")
        else:
        #If family found is set to true, end family and start new family
            output.append("</family>\n<family>\n<name>" + line_arguments[1] + "</name>\n<birth>" + line_arguments[2] + "</birth>\n")
    #If address found, add information about address
    if (line_arguments[0] == "A"):
        output.append("<address>\n<street>" + line_arguments[1] + "</street>\n<city>" + line_arguments[2] + "</city>\n<zip>" + line_arguments[3] + "</zip>\n</address>\n")
    #If phone found, add information about phone
    if (line_arguments[0] == "T"):
        output.append("<phone>\n<mobile>" + line_arguments[1] + "</mobile>\n<landline>" + line_arguments[2] + "</landline>\n</phone>\n")

output.append("</person>\n</people>")

outputfile = open("output.txt", "w")

outputfile.write("".join(output))
