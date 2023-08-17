#!/bin/bash

# GET Request
curl http://127.0.0.1:5000/get_user/Alice

# POST Request
curl -X POST http://127.0.0.1:5000/add_user/Diana/1200

# PUT Request
curl -X PUT http://127.0.0.1:5000/update_user/Bob/1700

# DELETE Request
curl -X DELETE http://127.0.0.1:5000/delete_user/Eve