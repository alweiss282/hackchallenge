# hackchallenge

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
