package main

import (
    "fmt"
    "os"
    "io/ioutil"
    "strings"
    "bytes"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

/*type phone struct {
    mobile string
    landline string
}
type location struct {
    address string
    street string
    ZIP_code string
}
type family struct {
    name string
    birth_year int
}
type person struct {
    first_name string
    last_name string
}*/

func main() {
    //-----------------------------------------------------------------Read argument as filename
    dat, err := ioutil.ReadFile(os.Args[1])
    //-----------------------------------------------------------------Check if file was read successfully
    check(err) 
    //-----------------------------------------------------------------split read data by lines
    lines := strings.Split(string(dat), "\n")
    //-----------------------------------------------------------------Buffer for output
    var buffer bytes.Buffer
    //-----------------------------------------------------------------Append start of xml file to output buffer
    buffer.WriteString("<people>\n")
    //-----------------------------------------------------------------Iterate through lines to find family or 
    for k := range lines{
        //-------------------------------------------------------------Split lines by |
        _data := strings.Split(lines[k], "|")
        for i := range _data {
            fmt.Print(_data[i])
        }
        if(_data[0] == "P") {
            buffer.WriteString("<person>\n<firstname>" + _data[1] + "</firstname>\n")
            buffer.WriteString("<lastname>" + _data[2] + "</lastname>\n")
            //---------------------------------------------------------Iterate until next person
            /*for i := k+1; i <= len(lines); i++ {
                P_data := strings.Split(lines[i], "|")
                switch P_data[0] {
                    case "P":
                        //---------------------------------------------Next person found
                        buffer.WriteString("</person>\n")
                        { break }
                    case "F":
                        buffer.WriteString("<family>\n<name>" + P_data[1] + "</name>\n<born>" + P_data[2] + "</born>")
                        //---------------------------------------------Iterate until next family or person
                        /*for y := i+1; y <= len(lines); y++ {
                            if(len(lines) == 0){
                                { break }
                            }
                            F_data := strings.Split(lines[y], "|")
                            switch F_data[0] {
                                case "P":
                                    { break }
                                case "F": 
                                    buffer.WriteString("</family>\n")
                                    { break }
                                case "A":
                                    buffer.WriteString("<address>\n<street>" + F_data[1] +"</street>\n<city>" + F_data[2] + "</city>\n<zip>" + F_data[3] + "</zip>\n</address>")
                                case "T":
                                    buffer.WriteString("<phone>\n<mobile>" + F_data[1] + "</mobile>\n<landline>" + F_data[2] + "</landline>\n</phone>\n")
                            }
                        }*/
                    /*case "A":
                        buffer.WriteString("<address>\n<street>" + P_data[1] +"</street>\n<city>" + P_data[2] + "</city>\n<zip>" + P_data[3] + "</zip>\n</address>")

                    case "T":
                        buffer.WriteString("<phone>\n<mobile>" + P_data[1] + "</mobile>\n<landline>" + P_data[2] + "</landline>\n</phone>\n")
                }
            }*/
            buffer.WriteString("</person>")
        }
    }
    buffer.WriteString("</people>")
    fmt.Println(buffer.String())
}
/*
#LOOP THROUGH LINES
    #PARSE LINE
    #SPLIT LINE
    #FIRST LETTER
    #IF P
        #ADD FIRST NAME AND LAST NAME TO LIST
    #IF F
        #ADD NAME AND YEAR TO LIST 
    #IF T
        #ADD PHONE NUMBERS TO LIST
    #IF A
        #ADD STREET INFORMATION TO LIST
*/