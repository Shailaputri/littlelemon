
## This is my submission for Backend Developer Capstone Project.   

I have developed a Django app called restaurant using rest framework. Kindly review my submission.
I take part in Open source projects. So if interested in pair programming, 
follow me on Github:https://github.com/Shailaputri.   


### First activate the venv using : source venv/bin/activate (for MAC users)  
### Load the requirements file using : pip install -r requirements.txt    

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
7. Got to "http://127.0.0.1:8000/restaurant/menu/bookings/" to view all reservations.
8. Go to "http://127.0.0.1:8000/restaurant/menu/book/"  to make a reservation.
9. Go to "http://127.0.0.1:8000/restaurant/menu/form/" to a Menu form to update menu items.

### Steps for unit testing: 
cd littlemon  
python manage.py test  
