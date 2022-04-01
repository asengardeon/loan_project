# Loan project 

## Business rules
It's a service with one HTTP endpoint that returns the annual percentage rate (APR) for a vehicle loan.

The input for this endpoint will be:

- The loan amount
- The loan term (in months)
- The person credit score
- The vehicle year
- The vehicle mileage

The annual percentage rate (APR) is calculated using the base rate table below:


| Term            | score >= 700 | score between 600 and 699 | score < 600 |
------------------|--------------|---------------------------|-------------|
| Up to 36 months | 4.75%        | 5.75%                     | 12.75%      |
| Up to 48 months | 5%	         | 6%	                     | 13.25%      |
| Up to 60 months | 5.5%         | 6.65%                     | N/A   s     | 


And the following rules:

1. The minimum loan amount for loans up to 36 months is $ 5,000
2. The minimum loan amount for loans up to 48 months is $ 10,000
3. The minimum loan amount for loans up to 60 months is $ 15,000
4. The maximum loan amount for a credit score equal to 700 or above is $ 100,000
5. The maximum loan amount for a credit score between 600 and 699 is $ 75,000
6. The maximum loan amount for a credit score below 600 is $ 50,000
7. If the vehicle year is before 2015, the base rate should be increased by 1.00%
8. If the vehicle mileage is over 100,000, the base rate should be increased by 2.00%

### **Example**

For the following input data the annual percentage rate should be 5.75%:

- Loan amount: `$ 10,000`
- Loan term: `36 months`
- Credit score: `700`
- Vehicle year: `2014`
- Mileage: `50.000`


**Architecture choosed**: Port and Adapters

**Packages definitions**
* app - application
* app.ports - package with adapters to transform applications args in Loan classes structure 
* app.loan - package model. files and classes to business implementations
* app.service - packages with services that executes the business rules implemented in the app.loan
***
**Develop techniques**: TDD 

**Language to develop**: Python, 3.10 version  
***

**Compiling and executing the project**  

###Option 1

Step 1 - execute the command in the root folder 
```sh
$ pipenv install
````

Step 2 - execute the main
```sh
$ python3  app/main.py
````

###Option 2
There is a Dockerfile tha can be executed if you prefer use docker

#### The default port in this two options is 5000


## Endpoint to APR

The enpoint to calculate APR is [server:port]/api/v1/apr and the params are:  

|param | type|  
-------|------   
|amount|integer|
|term|integer|
|credit_score|integer|
|vehicle_year|integer|
|vehicle_mileage|integer|


####Example to request:
``
localhost:5000/apr?amount=10000&term=36&credit_score=700&vehicle_year=2014&vehicle_mileage=50000
``



