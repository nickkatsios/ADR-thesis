adr choosing aws rds high availability solution proposed production aws rds database configured high availablity support bluegreen architecture reduce risk exists way provide rds cover document goal choosing among criterion offering aligns aws archtectural best practice distinguishing high availability provides failover solution event database vpc availability zone fails disaster recovery provides recovery solution across geographically separated distance multiregion event disaster cause entire data center fail adr select architecture ensures high availability defer disaster recovery separate adr criterion choosing right architecture align aws best architectural practice cost effective minimizes eliminates disruption redline production application rds measure commonly referred mean time recovery mttr proposed solution rds multi pro easy enable multi property aws rds console nothing port syncronous replication instant consistency failover hot standby minimal downtime one dns name across standby replica eliminates application intervention level failover amazon failover technology vpc network disk crash unavailibility automatic failover dns update con dns cache ttl setting application may impact recovery failover standby availability zero aws region fails likely double cost rds hot replica network traffic sync data perhaps write latency synchonous writes standby replica scaling solution rds read replica possible create failover solution read replica though typically done read replica already deployed environment pro move anayltic reporting workload master rrs replica promoted event main fails manual procedure asyncronous read create delayed consistency replica provide zero latency writes main replica available within cross cross region con failover manual apps must update connection config read replica cannot serve writes endpoint migrate aurora rds service aurora cluster typically scalability high availability involves richer topology technology rds multi load balanced service pro transparent fast failover highly distributed high throughput database upd node cluster master write others read configured replica failover level region con application connection string must configured failover port learn manage amazon claim app transparent suspicion apply rds multi architecture add high availability rds production instance recommended best practice adding existing rds instance consequence choosing aurora would part larger product design outside adr scope high availability failover protection improves stability product framework address disaster recovery also part overall scope product framework multi architecture fairly transparent rds application failover condition alerting mechanism understood prior implementation