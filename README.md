# vulncheck

Small application to assist with keyword searches on any supported API's for vulnerability checks. 

 
 Currently Supported API's:
| Name        | Supported           | API Key Required?  |
| ------------- |:-------------:| :-------------:|
| https://nvd.nist.gov/developers/vulnerabilities| Yes | No |
| https://vuldb.com/?kb.api| Yes | Yes |


- Environment Variables 
--A template .env file has been provided just request an API key from the vendors and update that value in the .env. These variables can also be driven from within your runtime environment. The Keys will need to be named appropiately for the base class to located the corresponding data. 
