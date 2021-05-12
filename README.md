# hackchallenge

# DailyHoroscope: get your horoscope here... daily
This app provides a simple interface for all of the astrology lovers to hear their daily horoscope. Have fun!

iOS GITHUB: https://github.com/EmoryWalsh/hackchallenge
Backend Deployed at: https://ajw282dailyhoroscope.herokuapp.com/api/<int:_number_of_sign>

Requirements:
backend: we've addressed all requirements
- there are more than 4 endpoints
- we have a relational database
- we used Heroku deployment

ios dev: we've addressed all requirements
- we used NSLayoutConstraint
- we used a UINavigationController
- we used a UITableView
- we've integrated with backend's API

Pictures:

<img width="342" alt="Screen Shot 2021-05-11 at 9 13 26 PM" src="https://user-images.githubusercontent.com/34355275/117903711-0eee3080-b29e-11eb-8f0b-416357a73312.png">

<img width="342" alt="Screen Shot 2021-05-11 at 9 16 23 PM" src="https://user-images.githubusercontent.com/34355275/117903802-3218e000-b29e-11eb-8c81-9b3f3d3ea6f3.png">


Has five routes, two tables which are connected via foreign key (to implement a one-to-many relationship), and API specs are below.

POST /api/users/

Request:
{
  "Name" : <User Input>
  "Sign" : <User input (must be one of the signs with a capital letter)>
}
  
Success Response:
{
  "success": true,
  "data": {
            "id" : <ID>,
            "name" : <User Input for Name>,
            "sign_id" : <ID of Associated Sign>
          }
}
  
  
GET /api/users/{user_id}/

{
  "success": true,
  "data": {
            "id" : <ID>,
            "name" : <User Input for Name>,
            "sign" : <User Input for Sign>
          }
}
  
  
DELETE /api/users/{user_id}/

Success Response:
{
  "success": true,
  "data": {
            "id" : <ID>,
            "name" : <User Input for Name>,
            "sign" : <User Input for Sign>
          }
}
  
  
GET /api/{sign_number}/
  
Success Response:
{
  "success": true,
  "data": {
            "id" : <ID>
            "sign" : <Sign>,
            "horoscope" : <Associated Horoscope>,
            "users" : [<Serialized Users>]
        }
}
  

GET /api/users/{user_id}/horoscope/

Success Response:
{
  "success": true,
  "data": {
            "horoscope" : <User Horoscope>,
        }
}


