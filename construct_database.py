import sqlite3
import os

conn = sqlite3.connect("si608.db")
c = conn.cursor()


##################
# CREATE TABLES  #
##################

drop_committee = "DROP TABLE IF EXISTS Committee"
drop_candidate = "DROP TABLE IF EXISTS Candidate"
drop_CC_linkage = "DROP TABLE IF EXISTS CC_linkage"
drop_contri_to_can_from_com = "DROP TABLE IF EXISTS contri_to_can_from_com"
drop_contri_by_indv = "DROP TABLE IF EXISTS contri_by_indv"

create_committee = "CREATE TABLE Committee(\
	CMTE_ID VARCHAR2(9) PRIMARY KEY,\
	CMTE_NM VARCHAR2(200),\
	TRES_NM VARCHAR2(90),\
	CMTE_ST VARCHAR2(2),\
	CMTE_DSGN VARCHAR2(1),\
	CMTE_TP VARCHAR2(1),\
	CMTE_PTY_AFFILIATION VARCHAR2(3),\
	ORG_TP VARCHAR2(1),\
 	CONNECTED_ORG_NM VARCHAR2(200),\
	CAND_ID VARCHAR2(9)\
)"

create_candidate = "CREATE TABLE Candidate(\
	CAND_ID VARCHAR2(9) PRIMARY KEY,\
	CAND_NAME VARCHAR2(200),\
	CAND_PTY_AFFILIATION VARCHAR2(3),\
	CAND_ELECTION_YR NUMBER(4),\
	CAND_OFFICE_ST VARCHAR2(2),\
	CAND_OFFICE VARCHAR2(1),\
	CAND_ICI VARCHAR2(1),\
	CAND_STATUS VARCHAR2(1),\
 	CAND_PCC VARCHAR2(9)\
)"

create_CC_linkage = "CREATE TABLE CC_linkage(\
	CAND_ID VARCHAR2(9),\
	CAND_ELECTION_YR NUMBER(4),\
	CMTE_ID VARCHAR2(9),\
	CMTE_TP VARCHAR2(1),\
	CMTE_DEGN VARCHAR2(1),\
	LINKAGE_ID VARCHAR2(12) PRIMARY KEY\
)"

create_contri_to_can_from_com = "CREATE TABLE contri_to_can_from_com(\
	CMTE_ID VARCHAR2(9),\
	TRANSACTION_PGI VARCHAR2(5),\
	TRANSACTION_TP VARCHAR2(3),\
	ENTITY_TP VARCHAR2(3),\
	NAME VARCHAR2(200),\
	EMPLOYER VARCHAR2(38),\
	TRANSACTION_AMT NUMBER(14,2),\
	OTHER_ID VARCHAR2(9),\
	CAND_ID VARCHAR2(9),\
	MEMO_CD VARCHAR2(1),\
	SUB_ID NUMBER(19) PRIMARY KEY\
)"

create_contri_by_indv = "CREATE TABLE contri_by_indv(\
	CMTE_ID VARCHAR2(9),\
	TRANSACTION_PGI VARCHAR2(5),\
	TRANSACTION_TP VARCHAR2(3),\
	ENTITY_TP VARCHAR2(3),\
	NAME VARCHAR2(200),\
	STATE VARCHAR2(2),\
	EMPLOYER VARCHAR2(38),\
	TRANSACTION_AMT NUMBER(14,2),\
	OTHER_ID VARCHAR2(9),\
	TRAN_ID VARCHAR2(32),\
	SUB_ID NUMBER(19) PRIMARY KEY\
)"

c.execute(drop_committee)
c.execute(create_committee)
c.execute(drop_candidate)
c.execute(create_candidate)
c.execute(drop_CC_linkage)
c.execute(create_CC_linkage)
c.execute(drop_contri_to_can_from_com)
c.execute(create_contri_to_can_from_com)
c.execute(drop_contri_by_indv)
c.execute(create_contri_by_indv)


##################
# DATA INSERTION #
##################

# committee table
committee_desired_columns = [0, 1, 2, 6, 8, 9, 10, 12, 13, 14]
committee_files = os.listdir("dataset/Committee")

# go to the Committee directory and loop through all the files in that directory
for file in committee_files:
	committee_file = open(os.path.join("dataset/Committee", file))
	committee_content = [] # list of tuples (in order to insert into the database)
	for line in committee_file:
		line = line.rstrip()
		new_line = line.split('|')
		desired_column = []
		for column in committee_desired_columns:
			desired_column.append(new_line[column])
		committee_content.append(tuple(desired_column))

	committe_insertion = "INSERT INTO Committee VALUES (?,?,?,?,?,?,?,?,?,?)"
	c.executemany(committe_insertion, committee_content)
	committee_file.close()
#-----------------------------

# candiate table
candidate_desired_columns = [0, 1, 2, 3, 4, 5, 7, 8, 9]
candidate_files = os.listdir("dataset/Candidate")
for file in candidate_files:
	candidate_file = open(os.path.join("dataset/Candidate", file))
	candidate_content = [] # list of tuples (in order to insert into the database)
	for line in candidate_file:
		line = line.rstrip()
		new_line = line.split('|')
		desired_column = []
		for column in candidate_desired_columns:
			desired_column.append(new_line[column])
		candidate_content.append(tuple(desired_column))
		
	candidate_insertion = "INSERT INTO Candidate VALUES (?,?,?,?,?,?,?,?,?)"
	c.executemany(candidate_insertion, candidate_content)
	candidate_file.close()
#-----------------------------

# CC_linkage
CC_linkage_desired_columns = [0, 1, 3, 4, 5, 6]
CC_linkage_files = os.listdir("dataset/CC_linkage")
for file in CC_linkage_files:
	CC_linkage_file = open(os.path.join("dataset/CC_linkage", file))
	CC_linkage_content = [] # list of tuples (in order to insert into the database)
	for line in CC_linkage_file:
		line = line.rstrip()
		new_line = line.split('|')
		desired_column = []
		for column in CC_linkage_desired_columns:
			desired_column.append(new_line[column])
		CC_linkage_content.append(tuple(desired_column))
		
	CC_linkage_insertion = "INSERT INTO CC_linkage VALUES (?,?,?,?,?,?)"
	c.executemany(CC_linkage_insertion, CC_linkage_content)
	CC_linkage_file.close()
#-----------------------------

# contri_to_can_from_com
contri_to_can_from_com_desired_columns = [0, 3, 5, 6, 7, 11, 14, 15, 16, 19, 21]
contri_to_can_from_com_files = os.listdir("dataset/contri_to_can_from_com")
for file in contri_to_can_from_com_files:
	contri_to_can_from_com_file = open(os.path.join("dataset/contri_to_can_from_com", file))
	contri_to_can_from_com_content = [] # list of tuples (in order to insert into the database)
	for line in contri_to_can_from_com_file:
		line = line.rstrip()
		new_line = line.split('|')
		desired_column = []
		for column in contri_to_can_from_com_desired_columns:
			desired_column.append(new_line[column])
		contri_to_can_from_com_content.append(tuple(desired_column))
		
	contri_to_can_from_com_insertion = "INSERT INTO contri_to_can_from_com VALUES (?,?,?,?,?,?,?,?,?,?,?)"
	c.executemany(contri_to_can_from_com_insertion, contri_to_can_from_com_content)
	contri_to_can_from_com_file.close()
#-----------------------------

# contri_to_can_from_com
contri_by_indv_desired_columns = [0, 3, 5, 6, 7, 9, 11, 14, 15, 16, 20]
contri_by_indv_files = os.listdir("dataset/contri_by_indv")
for file in contri_by_indv_files:
	contri_by_indv_file = open(os.path.join("dataset/contri_by_indv", file))

	contri_by_indv_content = [] # list of tuples (in order to insert into the database)
	for line in contri_by_indv_file:
		line = line.rstrip()
		new_line = line.split('|')
		desired_column = []
		for column in contri_by_indv_desired_columns:
			desired_column.append(new_line[column])
		contri_by_indv_content.append(tuple(desired_column))
		
	#print committee_content
	contri_by_indv_insertion = "INSERT INTO contri_by_indv VALUES (?,?,?,?,?,?,?,?,?,?,?)"
	c.executemany(contri_by_indv_insertion, contri_by_indv_content)
	contri_by_indv_file.close()
#-----------------------------

conn.commit()
conn.close()


