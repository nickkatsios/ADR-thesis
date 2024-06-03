# 6. I use AWS for ML and Event Driven Architecture

* Status: accepted 
* Date: 2018-06-03 <!-- optional -->

## Context and Problem Statement

I have to select a platform where I implement my event driven architecture as well as my machine learning. While the hurdle is lower with Google as it offer more ML serverless, most Biotech companies currently use AWS.

## Decision Drivers <!-- optional -->

* Learning materials and community
* Fit with Biotech requirements
* Cost 
* Easy of use

## Considered Options

* AWS
* GCP

## Decision Outcome

Chosen option: "AWS", because I want to get started and therefore the basics are enough, further I can use it at work and the cost for learning are low.

Positive Consequences: <!-- optional -->
* I have lower cost and use it at work
* I have the stack that is searched by biotech startups

Negative consequences: <!-- optional -->
* Later I will have to check GCP 
* I can not use it for private projects

## Pros and Cons of the Options <!-- optional -->

### AWS

* Good, because it is used by a lot fo biotech startups (also searching for this skill)
* Good, because of many blog post
* Good, because I can use it at work
* Bad, because not mnany out of the box solutions (a lot of adminstration)
* Bad, because not the tech leader (google is better in AI)

### GCP

* Good, because of many serverless data implementations (e.g. BigQuery, Dataflow/Beam) that remove most of the admin overhead and let me focus on the logic
* Good, because of many open source components (Apache Beam, Airflow)
* Good, because low cost for private projects
* Good, because many examples provided by google
* Bad, because the community setteled around AWS
* Bad, because the biotech startup mostly use AWS (also search for AWS)
* Bad, because on GCP the cloud functions do not support Python as well es environment varibales (there not very feasable to develop applications)
* Bad, because can not be used at work

## Links <!-- optional -->

* ...