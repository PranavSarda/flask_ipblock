# flask_ipblock

Python Server which limits the number of requests made from a particular IP address, thereby preventing bruteforce attacks.




Commands for making requests:

USAGE:


--> Open up two terminal tabs on the machine.


--> Run the flask server on one terminal window


--> Run the commands specified in the COMMANDS section to make the requests.
  
{"ip":"127.0.0.1","passwd":"<password>","timestamp":1596310199.211749,"username":"<username>"} =====> if the GET request was successful
  
curl: (52) Empty reply from server =====> if the request limit has reached.

success =====> if the POST request was successful

     
     
     COMMANDS:
      
     flask run
     
     curl -X POST http://127.0.0.1:5000/
     
     curl -X GET http://127.0.0.1:5000/
    
     
   
