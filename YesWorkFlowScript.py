# @begin Data_Cleaning_Food_Inspections.csv @desc Display one or more greetings to the user.
# @in Food_Inspections_CSV @as Food_Inspection.csv
# @out Food_Inspection_Facility_Violations.csv @desc Greeting displayed to user.

# @begin Standarized_Facilities @desc Use Open Refine to Change Variants of Facilty Type to standard format \n Ex. restaurant, RESTAURANT & Restaurant standarized to Restaurant
# @in Food_Inspection_CSV @as Food_Inspection.csv
# @out Food_Inspection-Standard_Facilities @as Food_Inspection-Standard_Facilities

# @end Standarized_Facilities

# @begin Remove_Empty_Cells @desc Use Open Refine to remove all empty cells for Facility Type and Violations
# @in Food_Inspection-Standard_Facilities @as Food_Inspection-Standard_Facilities
# @out Food_Inspection-Cleaned.csv @as Food_Inspection-Cleaned.csv

# @end emphasize_greeting

# @begin Standarized_Violations @desc Add a ' ' in front of violations row to make Violations match regex.
# @in Food_Inspection-Cleaned.csv @as Food_Inspection-Cleaned.csv
# @out FIC_standard_violations @as FIC_standard_violations_dataframe

# @end Standarized_Violations

# @begin FIC_Violation_Number_Only @desc filter out all words from violations columns by using regex: '[^[a-zA-Z0-9][1-9][0-9]?\.\s]*'
# @in FIC_standard_violations @as FIC_standard_violations_dataframe
# @out FIC_Filtered_Violations @as FIC_Filtered_Violations_dataframe

# @end FIC_Violation_Number_Only

# @begin FIC_Violation_Number_only_Cleaned @desc Replace all NaN values with 0
# @in FIC_standard_violations @as FIC_Filtered_Violations_dataframe
# @out FIC_Filtered_Violations_no_NaN @as FIC_Filtered_Violations_dataframe_no_NaN

# @end  FIC_Violation_Number_only_Cleaned

# @begin Identify_Violation_Range @desc Identify the Largest Violation Number
# @in FIC_Filtered_Violations_no_NaN @as FIC_Filtered_Violations_dataframe_no_NaN
# @out Violation_Ranges @as Violation_Ranges

# @end  Identify_Violation_Range

# @begin Load_Data_to_New_DataFrame @desc Load Data onto a new data frame with column \n indicating violation type and row a specific facility.
# @in Violation_Ranges @as Violation_Ranges
# @in FIC_Filtered_Violations_dataframe_no_NaN @as FIC_Filtered_Violations_dataframe_no_NaN
# @out Food_Inspection_Facility_Violations.csv @as Food_Inspection_Facility_Violations.csv

#@end Load_Data_to_New_DataFrame

# @end Data_Cleaning_Food_Inspections.csv