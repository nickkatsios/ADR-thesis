record transition mainstream format publishing api derived search index definition throughout document format refers rummager field format document type provided publishing api contentstoredocumenttype every contentstoredocumenttype mapped single format mainstream example search index want retire document also apply government detailed index building new search index publishing api data currently replacing existing search index mainstream government detailed single index govuk derived publishing api existing index populated least different application change improve quality data search system relies format handled consistent manner update document publishing event publishing withdrawing unpublishing tagging easier rebuild revert old backup lifecycle search index rumamgers search index long lived content regularly updated derive popularity field recent pageviews adr popularity updating without index lock update rather rebuilding search index every time separate task place reindex content currently search index zero downtime something adding new field otherwise changing elasticsearch mapping field work properly problem addressing neither mechanism add remove document search index mean edition ever published search index doesnt get updated stay next time document updated edition unpublished without rummager notified stay search index forever long term wed like able easily rebuild whole govuk index scratch avoid kind problem arent aiming right immediate able populate govuk index document already exist start index search api also want able reindex everything published within short period time day easily recover index backup moving format one time intending switch new index formatbyformat querying old new index filter select index get format mean retire old search indexing code publishing apps search index longer needed without populate everything also revert back old index simple configuration change something wrong problem weve discovered approach relevancy document within index depends document index index partially populated tfidf statistic representative affect search result firstly well implement task bulkreindex chunk content publishing api rummager process content way regular publishing update reindexing format let initially populate new index reindexing range let bring govuk index restoring backup secondly change indexing process format new index format following phase phase untransitioned search time rummager read untransitioned format old index document belonging untransitioned format stored govuk index filtered index time rummager ignore publishing api message affecting untransitioned format nightly update job update popularity field untransitioned format mainstream index also copy untransitioned format document mainstream index govuk index doesnt matter order two thing happen net effect untransitioned format considered tfidf statistic transitioned format ready returned govuk index phase indexed search time behaviour untransitioned format index time rummager insert document govuk index nightly update update popularity field govuk index one task well delete existing data format govuk index reindex net effect data govuk index come publishing api data indexed format phase transitioned search time rummager read transitioned format govuk index document belonging transitioned format stored mainstream index filtered index time rummager insert document govuk index nightly update update popularity field govuk index net effect search api publishing apiderived data transitioned format consequence copying mainstream data govuk add layer complexity nightly popularity updater wont able get rid weve retired index since weve decided implement ability generate index scratch content removed search unpublished stay way forever continue address manually removing content search admin