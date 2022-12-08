#initialisation 
bus_pass = 0  #bus passengers 
buses = 0 
personal_vehicals = 0 
loaded_trucks = 0 




year = [2000 , 2001 , 2002 , 2003 , 2004 , 2005 , 2006 , 2007 , 2008 , 2009 , 2010 , 2011 , 2012]

bus_pass = [317205 , 291421 , 282859 , 234620 , 277018 , 296390 , 294028 , 306898 , 306006 , 282949, 368763 , 395680 , 410941]

buses = [11728 , 10374 , 10415 , 11290 , 8345 , 8465 , 8317 , 8124 , 8418 , 8565 , 8980 , 9544 , 9935]

personal_vehicals = [980130 , 1012592 , 1039135 , 999836 , 1001278 , 973706 , 973957 , 1022895 , 948008 , 1040154 , 1029593 , 1054081 , 1138536]

loaded_trucks = [432097 , 342618 , 323495 , 350893 , 351224 , 344634 , 360181 , 336287 , 328081 , 267813 , 260367 , 250686 , 245442]



#menu interface 
print("="*40)
print("Border crossing database (2000-2012)")
print("Please choose a option 1, 2 , 3 or 4")
print("A -display the total number of vehicals crossing the border in a particular year")
print("B -display the mean number of crossing per vehical type")
print("C -display the 3 lowest number of vehicals in the transport mode in the corresponding years that they occur")
print("D -plots sum of buses and personal vehicals vs the year as the line plot ")
print("Q -quit programme")
print("="*40)
print("vehical types:")
print("1- buses")
print("2- personal vehicals")
print("3- loaded trucks")
print("="*40)

#option selection 
user_input = input("please choose a option (A-D or Q): ")
#option A 
if user_input == "A" or user_input == "a" : 
    year_input = input("please select a year (2000-2012): ")
    for idx in range(13) :
        total = buses[idx] + personal_vehicals[idx] + loaded_trucks[idx]
print(f"The total vehicals crossing the border in {year[idx]} was {total}") 

        
        


















#option B 






    


