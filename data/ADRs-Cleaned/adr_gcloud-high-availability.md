adr gcloud high availability mode trellocard deadline author pylipp proposed problem statement gcloud host boxtribute mysql database cloud accessed app deployed google app engine developer via cloud sql proxy server resides europewest region zone europewestd gcloud instance configured high availability mode quoting doc purpose configuration reduce downtime zone instance becomes unavailable might happen zonal outage there hardware issue data continues available client application configuration provides data redundancy cloud sql instance configured also called regional instance primary secondary zone within configured region within regional instance configuration made primary instance standby instance synchronous replication zone persistent disk writes made primary instance replicated disk zone transaction reported committed event instance zone failure standby instance becomes new primary instance user rerouted new primary instance process called failover statviz project introduced read replica primary database instance transfer load reading large data set relatively data read common app usage read replica resides europewestc zone furthermore disaster recovery scenario promote replica convert primary instance way place instance thats region thats outage also promote replica replace instance thats corrupted read replica exact copy primary instance data change primary instance updated almost real time read replica read replica readonly cannot write read replica process query read request analytics traffic thus reducing load primary instance primary instance cannot failover read replica read replica unable failover way outage read replica mode enabled finally nightly backup configured primary database instance pointintime recovery enabled driver data safety want user app data persist even gcloud outage happens expense billed extra mode read replica charged rate standard sql instance app availability want minimize app downtime gcloud outage happens considered keep turn turn performed editing primary database instance gcloud console consequence data safety case gcloud outage data still available backup restored primary instance run lost data another possibility promote readreplica place failed primary instance expense monthly cost gcloud app availability without primary instance outage well react alert manually promote readreplica start outage promotion app usable moderate inconvenience could consider one following either case still wont possible user perform action update data configure boxtribute app readreplica user request read data graphql query implemented already similar way configure boxtribute app fallback readreplica connecting primary database instance fails reference httpscloudgooglecomsqldocsmysqlhighavailability httpscloudgooglecomsqldocsmysqlreplication httpscloudgooglecomsqldocsmysqlreplicationrrinfo httpscloudgooglecomsqldocsmysqlpricing httpscloudgooglecomsqldocsmysqlreplicationbilling httpsconsolecloudgooglecomsqlinstancesprojectdropapp