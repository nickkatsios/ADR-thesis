# 5. Use Dialogflow for chatbots

* Status: accepted 
* Date: 2018-06-02 <!-- optional -->

## Context and Problem Statement

I need a service that processes text input and extracts intents and entities. This solution should integrate well with other services like Facebook, Mobile Frontends and all other texts. 

## Decision Drivers <!-- optional -->

* I want a solution that has a good quality
* I want a easy to use solution
* I want a tool with a big developer community
* I want a solution that is activly developped
* I want a tool that use Python, Java or Javascript as this is used by Biotech companies
* I want a solution that is easy extendible through code
* I want a solution that I can also use at work and supports English and German

## Considered Options

* AWS Lex
* Google Dialogflow

## Decision Outcome

Chosen option: "Google Dialogflow", because of the better quality and the better support.

Positive Consequences: <!-- optional -->
* I have the best in class solution

Negative consequences: <!-- optional -->
* I am not on my preffered tech stack Python + AWS, therefore I need to integrate them by using the Fullfiment only as a route to Python AWS Lambda functions

## Pros and Cons of the Options <!-- optional -->

### AWS Lex

* Good, because it is near to code and easy extendible 
* Good, because it has support for python (my preferred tech stack at the moment)
* Bad, because the community is smaller then the one at Dialogflow
* Bad, because it the development activity of AWS is limited (many Alexa features are not available in Lex)  
* Bad, because it only supports English
* Bad, because the quality is lower then in Dialogflow 

### Google Dialogflow

* Good, because it is easy to use and offers also pre trained intents
* Good, because the quality of the recognition better then with AWS Lex
* Good, because it has a large developer community (blog posts, documentation, udemy courses)
* Good, because it is activly develop and promoted as a tool for Google Actions
* Good, because it supports English and German.
* Bad, because it only support Javascript for Fullfilment
* Bad, because it is not on my current prefered tech stack (Python + AWS)

## Links <!-- optional -->

* Background Info: http://www.dieproduktmacher.com/developing-chatbots-comparing-amazon-lex-and-api-ai/ 
* Background Info: https://www.quora.com/Can-you-compare-API-AI-Google-Watson-IBM-and-Lex-Amazon-AWS
