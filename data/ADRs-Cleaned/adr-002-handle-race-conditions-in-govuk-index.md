record versioning handle race condition updating govuk index process creating new govuk index replace existing mainstream government detailed index new index populated rummager publishing unpublishing event message pulled queue controlled publishing api rummager cannot rely message queue processed order generated mean either rummager handle edge case accept consequence document published twice quick succession second publishing event arrives rummager first later stale message overwrite recent data index document unpublished immediately republished republishing message processed first later stale unpublishing message ignored published document remain search index document published immediately unpublished unpublishing event processed first later stale publishing message readd document search index remain unpublished elasticsearchs external versioning elasticsearch support external versioning document mean document includes version number external system case publishing event number publishing api version number set elasticsearch optimistic locking ensure document never updated deleted new version number equal existing version number take care edge case two publishing event arrive order second stale event ignored version number lower result document index end expected state recent version republishing message arrives earlier unpublishing message unpublishing ignored version number lower result document remains index expected delete unpublished document simplest way handle unpublishing event delete document index unfortunately could lead race condition leave index bad state document published immediately unpublished unpublished message arrives first initially deleted index stale republishing message arrives incorrectly recreate document result document remains search index despite unpublished considered handling storing unpublished document tombstone record would temporary would cleaned reindexing task would present long enough prevent race condition unpublishing message arrives first save document unpublished flag stale republishing message arrives message ignored version lower unpublishing message result tombstone record remains search index expected decided postpone implementation tombstone record time work meantime race condition may occur sequence event leading expected rare rely reindexing fix inconsistency intend schedule regular reindexing job create new index scratch latest version data publishing api fix inconsistent document caused unhandled race condition consequence described race condition handled correctly versioning system race condition unpublishing may lead occasional unpublished document appearing search index next time whole index recreated mean user might see name description unpublished page govuk site search relevant finder click link unpublished page would see found page redirected different page depending page unpublished occur support team would several remove page search index remove document rake task publishing api resends unpublishing message remove document search admin tool nonurgent case wait reindexing