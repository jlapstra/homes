# homes
CodingTest

### Dependancies
  Python3.8

### local run
python3 manage.py runserver

### Assumptions
All CSV's come with a first row with the fields listed (like the example)
With more time, I would have liked to worry about pagination and adding more filtering operations.
Over a few days, I took about 5 hours (with research) to complete the project.


### API

/api/singlehome/<zillow_id>
   - Getting single Home via zillow_id
   
/api/createhome/
   - Accepts data to create a new home listing
   
/api/homes/
   - Lists all homes
  
