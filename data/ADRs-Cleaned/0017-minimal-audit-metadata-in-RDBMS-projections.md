adr minimal audit metadata rdbms projection proposed author damir murat damirmuratgit gmailcom reviewer none traditional application rely rdbms database quite common set audit column table main entity typically find column like createdat createdby lastupdatedat lastupdatedby also find version column system relying optimistic locking column helpful quick way collecting basic information table activity might handy database administrator application developer value populated updated database transaction time usually direct consequence user interaction communication external system think time database transaction moment system becomes aware external change event sense column createdat lastupdatedat represent moment recorded external fact perspective see audit column contain potentially valuable domain information moment recording reality eventsourced system moment recording event fact also valuable information however correspond moment inserting updating record rdbms projection table rather moment created related event system reason createdat lastupdatedat column contain projection database transaction time updated based event metadata information column name also reflect name like firsteventrecordedat lasteventrecordedat appropriate still reason time database transaction projection table still add corresponding column necessary however always aware column updated example start replay event creating fresh projection database transaction moment completely different previously may wonder interesting moment persist highly dependent concrete domain still typically find interesting moment occurrence real world moment people system become aware occurrence similar however cannot reduce common metadata information deal domainspecific way find detail multitemporal event reference system built top axon framework domain event event originating aggregate also contain another valuable information sequence number event aggregate sequence number handy various like poling latest projection data updating subscribing query projection query application physically separated implementing optimistic locking therefore also record sequence number column name like lasteventsequencenumber probably noticed skipped createdby lastupdatedby column several reason first commandside application projection application physically separated meaning share thread usually basis extracting securityprincipal information supply principal part event payload axon framework automatically provide necessarily bad thing second availability securityprincipal information may domain usecase specific might available occasion example dealing saga issuing command event handler reason leaving column adr architectural rdbms projection cargotrackingbookingappquerysideprojectionrdbms cargotrackingbookinglibquerysidemodelrdbmsjpa store minimal set event audit metadata following column projection table firsteventrecordedat moment recording first projected event related aggregate corresponding record projection table lasteventrecordedat moment recording last projected event related aggregate corresponding record projection table lasteventsequencenumber sequence number last projected event relative aggregate corresponding record projection table consequence positive minimal set event metadata available projection table stored event metadata basis implementing various domain technical concern neutral slight performance degradation event projection handling increase maintenance cost negative increase stored data every projected record considered minimal set audit metadata projection reference httpsverraesnetmultitemporalevents