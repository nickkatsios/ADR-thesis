title implement individual sorting area core tag repository dal entity sort product shop owner able define custom sorting product listing search result page administration possible define system default sorting product listing top result default search page suggest route sort product score currently define custom sorting define service tag shopwaresaleschannelproductlistingsorting somewhat tedious make impossible define individual sorting via administration possible define custom sorting via administration individual sorting stored database table productsorting translatable label productsortingtranslation table possible define system default product listing sorting stored systemdefaultcorelistingdefaultsorting however influence default top result sorting search page suggest route result define custom sorting via plugin either write migration store database method recommended sorting managed via administration productsorting table look like following column type note binary urlkey varchar key unique shown url sorting chosen priority int unsigned higher priority mean sorting sorted top active tinyint inactive sorting shown sort locked tinyint locked sorting edited via dal field json json field sort listing createdat datetime updatedat datetime json field column look like json field productname property sort mandatory order desc asc desc mandatory priority order sorting applied higher priority come first mandatory naturalsorting field productcheapestprice order asc priority naturalsorting otherwise subscribe productlistingcriteriaevent add productsortingentity available sorting fly php namespace shopwarecorecontentproductsaleschannelsortingexample shopwarecorecontentproducteventsproductlistingcriteriaevent shopwarecorecontentproductsaleschannelsortingproductsortingcollection shopwarecorecontentproductsaleschannelsortingproductsortingentity symfonycomponenteventdispatchereventsubscriberinterface class examplelistingsubscriber implement eventsubscriberinterface public static function getsubscribedevents array return productlistingcriteriaeventclass addmycustomsortingtostorefront public function addmycustomsortingtostorefrontproductlistingcriteriaevent event void var productsortingcollection availablesortings availablesortings eventgetcriteriagetextensionsortings new productsortingcollection mycustomsorting new productsortingentity mycustomsortingsetiduuidrandomhex mycustomsortingsetactivetrue mycustomsortingsettranslatedlabel custom sorting mycustomsortingsetkeymycustomsort mycustomsortingsetpriority mycustomsortingsetfields field productname order desc priority naturalsorting availablesortingsaddmycustomsorting eventgetcriteriaaddextensionsortings availablesortings consequence old behaviour defining custom sorting tagged service deprecated removed