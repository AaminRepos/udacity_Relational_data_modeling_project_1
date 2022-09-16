 The database created here would be critical to the sparkify platform to understand and obtain different kinds of information for analytical needs like which songs are being played the longest or if free users tend to listen longer premium users or viceversa, understanding this kind of information is again critical for any startup to properly allocate business resources.
 
 This repository contains 3 python files, 'create_tables.py', 'etl.py' and 'sql_queries.py'.
First, with the 'sql_quries.py' file it is used by the 'create tables' file which we have to run via a terminal using the 'python' command only when python is fuly installed on the device used. Next we run the 'etl.py' wich stands for EXTRACT, TRANSFORM and LOAD using the same terminal and the same 'python' command.

 Create_tables.py is a program provided by udacity that contains multiple functions that creates our database based on the desinged table structures coded in the sql_queries.py file.
 
 Finally the etf.py file is our final step in extracting and transforming the data from the data files and loading it into our database depending on the data's respective table specified in the sql_queries.py file.
 
 In this project, a 1 fact table vs a 4 dimension tables star database schema was created.
 A fact vs dimension star schema is a database design where all the other tables created point to one fact table like how in this design all 4 tables users, artists, songs and time are all pointing or are directly related to the songsplay table wich has all of the other table's primary keys in its coulumns.
 
 Here a star schema is ideal for that the size of the data here is small enough to suffice multiple queries with all the easy JOIN statements and with all the great and famous COUNT and GROUP BY statements at a good speed.
 



refrences used:
https://pandas.pydata.org/docs/reference/api/pandas.read_json.html
https://www.geeksforgeeks.org/postgresql-data-types/
https://stackoverflow.com/questions/70184839/zipping-dictionary-to-pandas
https://www.freecodecamp.org/news/list-index-out-of-range-python-error-message-solved/
https://www.postgresql.org/docs/current/functions-datetime.html
https://stackoverflow.com/questions/12328817/postgres-how-do-i-format-an-int-timestamp-as-readable-date-string
https://dba.stackexchange.com/questions/289053/converting-date-and-time-integers-to-timestamp
https://www.postgresql.org/docs/current/sql-insert.html#:~:text=ON%20CONFLICT%20DO%20UPDATE%20guarantees,%E2%80%94%20%E2%80%9CUPDATE%20or%20INSERT%E2%80%9D.
