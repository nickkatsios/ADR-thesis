alb health check platform application instance receive traffic routed load balancer typically application instance run nginx servername based vhost per application application vhost proxy request local port application listens load balancer health check determine instance send traffic health check depend type load balancer protocol usually going configure health check tcpport elbs httpportrequestpathresponsecode alb information health check look following link httpsdocsawsamazoncomelasticloadbalancinglatestclassicelbhealthcheckshtml httpsdocsawsamazoncomelasticloadbalancinglatestapplicationtargetgrouphealthcheckshtml configure http health check load balancer sends request without host header case nginx process request default vhost request configured default vhost serve response code indicates load balancer instance healthy ready receive traffic present problem starting redeploying application instance application port unavailable period time nginx serve response load balancer still see health check response continues sending traffic instance even though application ready receive traffic current alb health check rudimentary test basic nginx configuration place rather testing whether apps properly deployed instance terminated cause replacement added target group pool prematurely cause elevated rate instance running one application going route traffic instance alb application dedicated target group specific health check path following format healthcheckappname health check path configured default vhost proxy request upstream application rewrite request match application health check path also icinga check configured puppet govukappconfig healthcheckpath parameter alb includes routing rule based host header redirects traffic application target group host header match value appname consequence application health check broken hasnt deployed properly load balancer see target unhealthy wont send traffic going target group platform monitor closely number healthy host detected per target group make sure alert detect problem