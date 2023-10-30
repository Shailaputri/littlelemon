 have tested all requirements. Please find attached the test screenshots for reference. 
Follow my profile/connect https://github.com/Shailaputri on Github for project collaborations. 



### Q1. Is the app added inside the INSTALLED_APPS configuration present in the settings.py file?    
##### Implemented.  
![Alt text](Attachments/Q1.png?raw=true)&nbsp;   

### Q2. Has the configuration for DATABASES updated inside the settings.py file?   
##### Implemented.  
![Alt text](Attachments/Q2.png?raw=true)&nbsp;  
### Q3. Were the migrations performed over the Booking model? You can tell this by performing migrations locally. The command prompt will show No changes detected on running the command to makemigrations.   
##### Implemented.  
![Alt text](Attachments/Q3.png?raw=true)&nbsp;  
### Q4. Does the booking form have three form items like in the screenshot below? In other words, there should be a name, reservation date and reservation time slot item.   
##### Implemented.  
![Alt text](Attachments/Q4.png?raw=true)&nbsp;  
### Q5.Open the booking form and click on the reservation date field. Does a date selector pop up when you click on the reservation date field?   
##### Implemented.   
![Alt text](Attachments/Q5.png?raw=true)&nbsp;  
### Q6.Open the project in your browser and click on the reservation navigation item. Are all the bookings available as JSON data on the reservations page after you populate the form data?   
##### Implemented.   
![Alt text](Attachments/Q6.png?raw=true)&nbsp;  
### Q7.Open the booking form and make a booking for 10:00 AM. Now try to make another booking on the same day for 10:00 AM.  Is a duplicate booking of a specific time and date unavailable if that slot is already booked?  
##### Implemented.   
![Alt text](Attachments/Q7.png?raw=true)&nbsp;  
### Q8. Open the booking menu and change the date by clicking on the reservation date field. When you select a different date, do you see the reservations for that day on the right side?   
##### Implemented.   
![Alt text](Attachments/Q8.png?raw=true)&nbsp;  
### Q9. Open the booking form and make a booking for 10:00 AM. Now try to make another booking on the same day at 10:00 AM. Can you select the 10:00 AM slot from the dropdown list?   
##### Implemented.     
![Alt text](Attachments/Q9.png?raw=true)&nbsp;  
### Q10. Open the booking form and create a reservation on a specific date, for example, 2022-08-16. Now go to this API endpoint in your browser http://127.0.0.1:8000/bookings?date=2022-08-16  
![Alt text](Attachments/Q1.png?raw=true)&nbsp;  
### Can you see the reservation you just made?  
##### Implemented.     
![Alt text](Attachments/Q10.png?raw=true)&nbsp;  
### Q11. Open the booking form and change the date. If there are no reservations on that date, does it show No Bookings on the right side of this page?
##### Implemented. 
![Alt text](Attachments/Q11.png?raw=true)&nbsp;  
### Q12 . Open the booking form in your browser. Right-click on the page and select view page source. Now you are looking at the HTML code. Can you locate the fetch() function, which is the Fetch API used to retrieve data from the API in the JavaScript code block?
##### Implemented.
![Alt text](Attachments/Q12.png?raw=true)&nbsp;  
### Q13. Open the booking form and check the reservation date field. Is today’s date automatically selected when you open the booking form?    
##### Implemented.     
![Alt text](Attachments/Q13.png?raw=true)&nbsp;  