# 1. Use Serverless with Python and keep an eye on Istio as application runtime

* Status: accepted <!-- optional -->
* Date: 2018-05-31 <!-- optional -->

## Context and Problem Statement

To run the applications I need to decide which platform to chose.

## Considered Options

* AWS Lambda
* AWS EKS \(Kubernetes + Helm + Istio\)

## Decision Outcome

Chosen option: "AWS Lambda", because currently Istio as well as EKS is still in beta and for private projects AWS Lambda is the more cost efficient version. And for different workloads different solutions might be best e.g. [_BinaryAlert_](https://github.com/airbnb/binaryalert) \(Serverless\).

Positive Consequences: <!-- optional -->
* [e.g., improvement of quality attribute satisfaction, follow-up decisions required, …]
* …

Negative consequences: <!-- optional -->
* [e.g., compromising quality attribute, follow-up decisions required, …]
* …

## Pros and Cons of the Options

### AWS Lambda 

* Good, because I an use the Allianz AWS account
* Good, because it has lower cost for bootstrapping private projects
* Good, because it is tightly integrated with AWS
* Good, because it is fast to develop
* Good, because I can do it in Python with is the Language use by Biotech companies
* Bad, because it is not the Allianz strategy, so I cannot use it for work projects
* Bad, because it is AWS specific \(Locking\)
* Bad, because it is not very "evolutionary"
* Bad, because it misses some logging and routing features like Istio 

### AWS EKS

* Good, because it is more portable as I can integrate it with Istio and the complete kubernetes ecosystem
* Good, because I could use somethign similar for work projects
* Good, because it is the tech stack of bio tech companies like Synthego and Syapse
* Good, because I can use plain Docker and have a faster local development time
* Bad, because it is more expensive for private projects
* Bad, because Istio is currently still in development and important features like token validation, helm charts, egress policy is still in beta
* Bad, AWS EKS is not available yet

## Links <!-- optional -->

* [Integrate Serverless with Kubernetes](https://medium.com/@jeffzzq/how-to-integrate-an-aws-lambda-function-into-your-kubernetes-service-mesh-5d665f351675)
