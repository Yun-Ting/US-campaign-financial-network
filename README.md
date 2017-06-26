# US-campaign-financial-network

the CREATE and INSERT function had basically been done. 
I've tested the code with data in 2018 and inserted the data into si608.db.

I guess if the schema of the database doesn't change 
(as we go back to data of previous years),  
data could be automatically inserted into si608.db if we download
data from the website and put them in the directory, which was named after the name of the table.
For example, candidates' data fells into the path: /dataset/Candidate. 
The os.listdir function will automatically open the file and insert 
the data for us. 
Please refer to construct_database.py for more details!

Sorry for my bad coding style, the variable names are very long.
Feel free to optimize the code!! It is currently not so clean lol.


