## API Endpoints

* `/api/accounts/register/` - Registration endpoint with following credentials:

    **_username, password, password2, first_name, last_name_**

* `/api/token/` - Auth endpoint. Use you already created credentials(username + password) to get token
* `/api/token/refresh/` - Token refresh endpoint
* `/api/accounts/<user_id>/update/` - User update endpoint. Provide user id. You can update:

  **_first_name, last_name, description, photo_**

* `/api/comments/` - Endpoint with GET and POST methods. GET - get all comments, POST - create(necessary fields: **_text_** and **_to_**(id of some user)) new comment
* `/api/accounts/<user_id>/received_comments/` - Endpoint to get received comments by some user. Provide user id