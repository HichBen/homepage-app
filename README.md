# homepage_api
Link of the api documentation that was deployed in AWS:
 - http://homepageservice-env.eba-34hauims.us-east-2.elasticbeanstalk.com/homepage/docs
    
## Steps to run it locally
 - Make sure you have installed `docker` and `docker-compose`
 - Run `docker-compose up -d`
 - Head over to http://localhost/homepage/docs for the api documentation
 
## Different Endpoints:
The api has 5 endpoints:
 - Two get methods:
    - /homepage : Which will return the json all available homepages.
    - /homepage/{id} : Which takes a group id and returns json of that group_id's homepage
 
 - Delete method:
    - /homepage/{id} : takes a group_id and deletes the homepage
  
 - Post Method:
    - /homepage : Takes a json and creates a new homepage
    
 - Patch method :
    - /homepage/{id}/ Takes a json of the fields that the user wants to update and updates them
