/**
 * @class OutputICS outputICS.h
 * @author Miranda Postma
 * @brief Code implementing OutputType strategy for .ics output
 * @details Concrete "strategy" component of the Strategy Pattern
 * @date 28Nov2021
 * @version C++ Version: 4.2.1
 */
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <time.h>
#include "outputICS.h"
#include "output.h"

/** 
 * @fn virtual const void generateOutput(const Output output) const
 * @brief Generate a new .ics file for each deadline
 * @details Concrete implementation of .ics Strategy function 
 * @param output Output object containing filename and vector of Deadline objects
 * @return NULL
 */
const void OutputICS::generateOutput(const Output output) const {
    
    /** Create a unique numeric identifier for the number of upcoming deadlines */
    int count = 1;

    /** Declare temporary variables to be utilized in the loop */
    std::string line;
    std::string UTCstart;
    std::string UTCend;

    /** Save the dateArray Deadline vector from output for local reference */ 
    std::vector<Deadline> dateArray = output.getDateArray();

    /** Loop over all deadlines stored in the dateArray Deadline vector */
    for (std::vector<Deadline>::iterator date = dateArray.begin(); date < dateArray.end(); date++) {
        
        /** Get the due date for the current Deadline */
        std::time_t dueDate = (*date).getDueDate();

        /** Convert the due date to a UTC date */
        struct tm UTCdate;
        gmtime_r(&dueDate, &UTCdate);

        /** Separate the components of the date into different variables */
        std::string year = std::to_string(UTCdate.tm_year + 1900);
        std::string month = std::to_string(UTCdate.tm_mon + 1);
        std::string day = std::to_string(UTCdate.tm_mday);
        std::string hour = std::to_string(UTCdate.tm_hour);
        std::string min = std::to_string(UTCdate.tm_min);

        /** If month, day, hour, or minute is <10, pad with an extra 0 */
        if (std::stoi(month) < 10) {
            month = "0" + month; 
        }
        if (std::stoi(day) < 10) {
            day = "0" + day; 
        }
        if (std::stoi(hour) < 10) {
            hour = "0" + hour; 
        }
        if (std::stoi(min) < 10) {
            min = "0" + min; 
        }

        /** Recombine the different variables as a UTC timecode (seconds set to 00) */ 
        UTCstart = year + month + day + "T" + hour + min + "00Z";
        UTCend = year + month + day + "T" + hour + min + "00Z";

        /** Prepare a unique file name for each Deadline */ 
        std::string filename = (*date).getDueCourse() + "_deadline_" + std::to_string(count); 

        /** Create a new file named using the dueCourse field and the unique ID */
        /** Store all .ics output in a subfolder of output called "ics" */
        std::ofstream outFile("./output/ics/" + filename + ".ics"); 

        /** Write the necessary Calendar tags and values to the file */
        outFile << "BEGIN:VCALENDAR" << std::endl;
        outFile << "BEGIN:VEVENT" << std::endl; /** Initialize event start */ 

        line = "DTEND:" + UTCend; /** End time of event in UTC */ 
        outFile << line << std::endl; 

        line = "DTSTART:" + UTCstart; /** Start time of event in UTC */
        outFile << line << std::endl;

        outFile << "SEQUENCE:0" << std::endl; /** Change log */
                
        line = "SUMMARY: " + (*date).getDueCourse() + " - " + (*date).getDueName(); /** Event description */
        outFile << line << std::endl;

        outFile << "TRANSP:OPAQUE" << std::endl; /** Event visibility */

        outFile << "END:VEVENT" << std::endl; /** Initialize event end */ 
        outFile << "END:VCALENDAR" << std::endl;

        /** Save and close the file */
        outFile.close();

        /** Increment the count of posted deadlines */
        count++;
        
    }
}
