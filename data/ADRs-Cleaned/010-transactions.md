database transaction author opqdonut macroz introduction adr written aftermath production incident issue describe current design choice database transaction design philosophy point software lifecycle rem err side caution try guarantee consistency data cost performance every api call transaction remsapitransactionmiddleware middleware wrap api call transaction transaction run isolation level serializable strictest serialization level see postgresql doc additionally transaction get request readonly guarantee get pure strict ordering command via locking application command processed roughly following way implementation remsservicecommandcommand get event application applicationevent table caching getallapplications getunrestrictedapplication compute application state run command handler given command application state command handler succeeds append new event applicationevent run process manager new event result new command approverbot processed immediately thread new row outbox blacklist row running command parallel serializable transaction wed get transaction conflict event added step todo verify conflict come guarantee command transaction processed sequentially weve added lock table applicationevent share row exclusive mode statement step mean command handler wait lock progressing problem lock couple incident production reason thread got stuck holding lock applicationtable prevented command processed additionally thing communicated user eventual http timeout mightve patience wait protect failure like set two postgresql config variable every connection implementation remsdbcore locktimeout second idleintransactionsessiontimeout second guarantee thread stuck holding lock command fail within second http service unavailable connection stuck thread holding get closed second freeing lock implementation future work handle transaction conflict exception guarantee happen isolation level serializable issue addition api call scheduled job like email outbox processing also transaction issue consider adding sort warningerror remsdbcore function called outside transaction done custom bindconnection macro issue