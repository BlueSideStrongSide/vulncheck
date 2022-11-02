# vulncheck

Small application to assist with keyword searches on any supported API's for vulnerability checks.
 
**DEV BRANCH CODE MAY BREAK< USE WITH CARE** 

 Currently Supported API's:
| Name        | Supported           | API Key Required? |
| ------------- |:-------------:| -----:|
| https://nvd.nist.gov/developers/vulnerabilities| Yes | No |
| https://vuldb.com/?kb.api| Yes | Yes |


### Environment Variables 
A template .env file has been provided just request an API key from the vendors and update that value in the .env. These variables can also be driven from within your runtime environment. The Keys will need to be named appropiately for the base class to located the corresponding data. 


### Fixes/Features/Updates

- [x] Remove all synchronous code 
- [x] Migrate project to ASYNC
- [ ] Export configuration within base class
- [ ] Honor API timeouts
- [ ] Common result handler across project
- [ ] Store results locally  from API's
- - [ ] Process cache before submitting to API
- - [ ] Create parameter to disable/enable cache check
- [ ] Extend additional API interactions using new methods in the API modules
- [ ] Type Checking throughout
- [ ] Linting Throughout