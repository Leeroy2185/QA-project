# QA project 1

## Car Owner Database

The aim of the project is to produce a fully working CRUD application the remit is as follows:
"_To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training._"

### Project approach

initially the project took the form of a 3 table databse linking owners to vehicles via a registered vehicle table containing foreign keys for both the owners and vehicles.

![ERD_1initiall](https://user-images.githubusercontent.com/55799345/107163193-26b4d080-69a0-11eb-8c93-5245ada9ab19.png),  
 

On further consideration the registered vehicle table was not required as this table would be used typically to break up a many to many relationship. and as this would of     ulitmately ended up as a one to many relationship table. The revised table looked like this:


![ERD_2](https://user-images.githubusercontent.com/55799345/107163348-fa4d8400-69a0-11eb-8872-f64a483efe98.png)  

This was the intial ERD that i began working on to create the tables for my database to be implemented into my app. As i had no previous experience of creating a Flask app i decided to further simplfy the ERD diagram in order to actually get a fully functioning CRUD appliacation up and running as the main priority , the less information I had the easier it would be to me the requirements for the MVP. Further functionalitly e.g.(more tables , more fields ) could be something that could be added at a later date.  

![ERD 3 Final](https://user-images.githubusercontent.com/55799345/107164020-d3914c80-69a4-11eb-9afb-69d283d79cbc.png)  

## Trello board  

Due to the number of different tasks involed in the creation of the application a trello board was implemented into the design, this helped oraganise tasks into lists and helped to sort the design into smaller segments making the project more manageable.  










