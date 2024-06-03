# 3. For Machine learning select a vendor specific stack of a general stack

* Status: accepted 
* Date: 2018-05-31

## Context and Problem Statement

To add smart features to automate my job I need a data pipeline this could be a vendor neutral which is harder to maintain and takes longer to setup but can be ported to other platforms or a AWS specific setup.

## Considered Options

* AWS Sagemaker
* Kubernetes with Tensorflow

## Decision Outcome

Chosen option: "AWS Sagemaker", because currently I need something fast to show results therefor it is easier to use the managed solution from AWS. And I want to learn the business value not the infrastructure setup (In the future I see myself as the user not the maintainer).

Positive Consequences: <!-- optional -->
* [e.g., improvement of quality attribute satisfaction, follow-up decisions required, …]
* …

Negative consequences: <!-- optional -->
* I have to monitor AWS EKS and Tensorflow closely and reevaluate in few month if the EKS Tensorflow achieves better results then Sagemaker, currently I do not know if all features are available and what solution will be available inside AZD.

## Pros and Cons of the Options <!-- optional -->

### AWS Sagemaker

* Good, because I can use the Allianz account
* Good, because it has lower cost for bootstrapping private projects
* Good, because it is tightly integrated with AWS e.g. lex
* Good, because it is fast to develop
* Bad, because it is not the Allianz Strategy, so I cannot use it for work projects
* Bad, because it is AWS specific \(Lockin\)
* Bad, because it is not very "evolutionary"
* Bad, because it is only available online
* Bad, because Google seems to be in the lead with regards to machine learning. 

### Kubernetes with Tensorflow

* Good, because it is more portable as I can integrate it wit the complete kubernetes ecosystem (more evolutionary)
* Good, because I could use something similar for work projects
* Good, because I can develop locally
* Bad, because it is more expensive for private projects
* Bad, because AWS EKS is not available yet.
* Bad, because harder to setup and longer ramp up time
* Bad, because I have to manage the infrastructure.

## Links <!-- optional -->

* [Link type] [Link to ADR] <!-- example: Refined by [ADR-0005](0005-example.md) -->
* … <!-- numbers of links can vary -->
