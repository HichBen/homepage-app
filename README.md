# homepage_api
Link of the api documentation that was deployed in AWS:
 - http://35.175.138.192:8080/api/homepage/docs
    
## Steps to run it locally
 - Make sure you have installed `docker` and `docker-compose`
 - Run `docker-compose up -d`
 - Head over to http://localhost:8080/api/homepage/docs for the api documentation
 
## Different Endpoints:
The api has 5 endpoints:
 - Two get methods:
    - /api/homepage : Which will return the json all available homepages.
    - /api/homepage/{id} : Which takes a group id and returns json of that group_id's homepage
 
 - Delete method:
    - /api/homepage/{id} : takes a group_id and deletes the homepage
  
 - Post Method:
    - /api/homepage : Takes a json and creates a new homepage
    
 - Patch method :
    - /api/homepage/{id}/ Takes a json of the fields that the user wants to update and updates them