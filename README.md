
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)  [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# Message-Encryption

## Approach

Message Encryption, as the name itself suggests can be used to encrypt messages by width character encoding generally used for electronic communication. Here, to encrypt messages I have used pybase64 module which provides methods for encrypting as well as decrypting the encrypted messages. The application is programmed in such a way that whenever someone tries to encrypt a message, the message is encrypted and a key is generated and both the encrypted message and key are saved in a csv file. Finally, to decode there is a decoder which requires the encrypted message and the key generated while encryption of that particular message to decrypt.

## Project

This project is divided into two parts:
1. Encoder
2. Decoder


## How to Use

* Clone the repository using :

        $ https://github.com/DhaivatV/Message-Encryption.git
                
* Enter the directory using:

        $ cd  Message-Encryption/
      
* Install the requirements using:

        $ pip install -r requirements.txt

* To encrypt a message run : 

        $ python3 main.py

* To decrypt a message run : 

        $ python3 Decoder.py
        
## Demo 
### Encoder
  <img align="left" alt="coding" width=400 src="https://github.com/DhaivatV/Message-Encryption/blob/main/Images/upload%201.png">
  <br></br>
  <br></br>
  <br></br>
  <br></br>
  <br></br>
  <br></br>
  <img align="left" alt="coding" width=400 src="https://github.com/DhaivatV/Message-Encryption/blob/main/Images/upload%202.png">
  <br></br>
  <br></br>
  <br></br>
  <br></br>
  <br></br>
  <br></br>
  <br></br>
  <br></br>
  <br></br>
  
 ### Decoder

  



  
 

## Results

* We have encrypted the message (Hello!! User) and a key is generated along with it.
* We have successfully decoded the message using the decoder.





## Author
* Dhaivat Vipat

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/) by [Dhaivat Vipat](https://www.linkedin.com/in/dhaivat-vipat-0b20851b9/)

## Contribution 

Contributions are always welcome! You can contribute to this project in the following way:
- [ ] Bug fixes if any
- [ ] Creating an application

