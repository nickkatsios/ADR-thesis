dedicate separate haproxy machine loadbalancing kubernetes three controller node listening single address represent kubernetes master additionally worker node listens order expose nodeport service outside world rather choose particular worker node talk make sense loadbalance request well whichever worker node currently online whats written straightforward enough add current haproxy config however kubernetes doesnt provide support claiming address outside internal network rather kubernetes merely indicates want address service example let say web service listening port set exposure loadbalancer kubernetes indicate set nodeport mapping example might map job following outside kubernetes notice new service requesting type loadbalancer choose address isnt already configure load balancer claim floating address configure load balancer round robin request address kubernetes worker node respectively would good didnt hand automate mean haproxy config could changing routinely could affect production service kubernetes get haproxy server separate one currently configured puppet time puppet configure also provides simple list peer address one day capable configuring consequence make change load balancer kubernetes without worrying breaking access firstclass service already production even though detail server similar separation let view haproxy machine load balancer rather highly available gateway kubernetes