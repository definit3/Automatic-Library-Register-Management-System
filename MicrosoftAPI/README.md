# Automatic-Library-Register-Management-System
Automatic Library Register Management System is a software that can be used to automatically maintain the student registers in library of schools, colleges and institutes using face recognition.

## Getting Started

*	**create_person_group.py:** Creates a new person group in which people can be added and recognized when needed.
*	**adddata.py:** Takes the student details and face photos and stores them in the database.
*	**addface.py:** Creates unique personID of a person and uploads the respective face photos in the person group through Face API.
*	**train_person_group.py:** Trains the created person group.
*	**workbook.py:** Creates a new spreadsheet file.
*	**in.py & out.py:** Recognizes the person/s and update the spreadsheet file with entry and exit date and timing.

### Prerequisites

Python 2.7

## Built With

*	Sqlite3
*	Dlib
*	OpenCV
*	Microsoft Face API
*	Openpyxl

## Authors

* **Vivek Raj** - [definit3](https://github.com/definit3)
