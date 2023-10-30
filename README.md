
## This is my submission for Backend Developer Capstone Project.   

I have developed a Django app called restaurant using rest framework. Kindly review my submission.
I take part in Open source projects. So if interested in pair programming, 
follow me on Github:https://github.com/Shailaputri.   


### First activate the venv using : source venv/bin/activate (for MAC users)  
### Load the requirements file using : pip install -r requirements.txt   

### Steps for Full Stack testing
Head to http://127.0.0.1:8000/restaurant/menu/ for instructions.
No authentication has been implemented for frontend for now.
API testing needs authentication. 

### Note for Meta Certification Peer Reviewers : 
### To make it easy for reviewers, I have tested all project requirements
### and attached screenshots in PeerReviewQnsDjango.md. 
### Please check that.

### Steps for testing using Client app like Postman or Insomnia:  
To register for new user: /register/  
To find token using above username and password: /api-token-auth/  
Menu API : /restaurant/menu/menu/  
Booking Table API : /restaurant/booking/tables/  

### Steps for Browsable API testing:   
1. Go to "http://127.0.0.1:8000/register/" to register new user.  
2. Go to "http://127.0.0.1:8000/api-auth/login/" to login using username and password.  
3. Go to "http://127.0.0.1:8000/restaurant/menu/menu/" to see or update all menu items  
4. Go to "http://127.0.0.1:8000/restaurant/menu/menu/1" to see or update individual menu item.  
5. Go to "http://127.0.0.1:8000/restaurant/booking/tables/" to see or update table bookings.  
6. Go to "http://127.0.0.1:8000/api-auth/logout/" to logout after testing.  
7. Got to "http://127.0.0.1:8000/restaurant/menu/allbookings/" to view all reservations.
8. Go to "http://127.0.0.1:8000/restaurant/menu/book/"  to make a reservation.
9. Go to "http://127.0.0.1:8000/restaurant/menu/menu_items" to a Menu form to update menu items.

### Steps for unit testing: 
cd littlemon  
python manage.py test  


### Features : -
About page
![Alt text](Attachments/aboutpage.png?raw=true)&nbsp; 
  
Menu form
![Alt text](Attachments/menuform.png?raw=true)&nbsp;

Booking form
![Alt text](Attachments/reservationbooking.png?raw=true)&nbsp;

All Bookings in JSON format
![Alt text](Attachments/allbookings.png?raw=true)&nbsp;

MySQL Data Layer
![Alt text](Attachments/database.png?raw=true)&nbsp;

API - to generate token
![Alt text](Attachments/generatetoken.png?raw=true)&nbsp;

API - Menu GET
![Alt text](Attachments/MenuAPIPostman.png?raw=true)&nbsp;
![Alt text](Attachments/menupostman.png?raw=true)&nbsp;

API - Menu POST
![Alt text](Attachments/postmenuapopostman.png?raw=true)&nbsp;

APi - Single Menu
![Alt text](Attachments/Singlemenuapipostman.png?raw=true)&nbsp;

