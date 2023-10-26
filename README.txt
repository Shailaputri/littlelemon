Testing Credentials:
Username = 'testuser'
Password = 'mnbvcxza!'

Steps for API endpoint testing (using Postman or Insomnia):
To find token using above username and password: /restaurant/menu/api-token-auth/
Use token found for all authorisation in order to test API endpoints. 
Menu API : /restaurant/menu/menu/
Booking Table API : /restaurant/booking/tables/</ol>

Steps for Browsable API testing : 
1. Go to "http://127.0.0.1:8000/api-auth/login/" to login using username and password.
2. Go to "http://127.0.0.1:8000/restaurant/menu/menu/" to see or update all menu items
3. Go to "http://127.0.0.1:8000/restaurant/menu/menu/1" to see or update individual menu item.
4. Go to "http://127.0.0.1:8000/restaurant/booking/tables/" to see or update table bookings.
5. Go to "http://127.0.0.1:8000/api-auth/logout/" to logout after testing.