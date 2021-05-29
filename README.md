# tokenScanner
tokens/api/secret keys scanner to know what is this [tokens/api/secret] , and tell you how exploit if available.

# Description
many of times find tokens for api keys or any secret keys and not know what is this token and what is third party which related this token <br>
many of tokens we support..

```
slack [api key , access token, etc]
aws [client id , api key , secret key]
heroku [oauth token , etc]
Artifactory [API Token]
Vault [Token]
paypal [Access Token]
Google Maps [Api Key]
Google Cloud Platform [API Key]
many of google 
MailGun [api key]
AMS [Auth Token]
Foursquare [client key , api key , secret key]
picatic [api key]
Square [Access Token, OAuth secret , api key]
Facebook [OAuth2.0 token]
Basic Auth Credentials
++ 50 token again
```
The Tool will Recognize on token and will tell you how exploit this token [if available]
The tool have many of regex in file regex.txt you can edit it if you want add new regex <br>
The tool will be updated and will provide tokens/api/secrets every time 

# Install
sudo pip3 install colorama yaml re

# Usage 
python3 tokenScanner.py \<TheToken\>

### Notic: extract_with_nuclei.yaml as template file to extract all this tokens from urls by nuclei tool [Develop by me] you can use it.
