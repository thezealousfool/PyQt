# PyQt
A demo project created to learn ***PyQt*** (Python wrapping of the famous Qt Library). The project communicates to a *MySQL* database using ***mysql.connector*** python module.

## Dependencies
* python (v2.x)
* mysql
* pyqt4
* mysql.connector

## Installing Dependencies (Ubuntu/Debian)

	sudo apt-get install python mysql-server python-qt4 python-mysql.connector

## Configuration

Edit the configuration.py file according to your mysql setup.

|     Name     |   Role             |
|:------------:|:-------------------|
| user         |MySQL Username      |
| password     |MySQL Password      |
| host         |MySQL Host          |
| database     |MySQL Database Name |
| logintable   |Login Table Name    |
| entriestable |Entries Table Name  |

## Table Specification

### Login Table

| Field    | Type        |
|:--------:|:------------|
| name     | varchar(20) |
| password | varchar(20) |
| role     | int(11)     |

NB: '**role**' field: 1 for admin, 2 for user, 3 for tester

### Entries Table

| Field   | Type         |
|:-------:|:-------------|
| creator | varchar(20)  |
| format  | varchar(400) |

## Execution

To execute the project:

	python main.py