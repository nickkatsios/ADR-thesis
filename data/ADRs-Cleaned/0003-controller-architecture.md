controller basic architecture staus proposed controller responsible lifecycle framework reflects starting point mean controll needed action framework must load deps render view generate route etc framework requires simple easy controll end user turn interaction user controller simple understandable destructured smaller step would provide better grain detail controll application validation error management etc framework rational requires functional approach way would easy new user way would user previous concept knowledge similar framework programming language controller monadic explanation controller would composition different function step created initial draft luk rychteck would provide user ability controll step creation example clojure defn controller setroutes settemplate setresponse setmiddlewares setactions setdeps setsession controller state map explanation controller would feeded initial statemap user would provide statemap would hold data would needed build controller approach similar state monad would return result configuration discard initial state help two way enforce specific stucture definition statemap user would give clearer understanding ingredient controller would created user would map key would represent different stage controller would able validate statemap data example state map clojure def state httprequest method get url request action select params response header list contenttype txthtml charset utf body nil requestdata model foo template comp temp middlewares sessiondata deps state map schema clojure mali schema state map def statemap map httprequest map method enum get post put url vector request action enum select update delet insert response map header vector body string vector nil requestdata map model malli schema vector template hiccup static vector string middlewares list function middleware vector deps map session map controller statemap clojure defn controller statemap setroutes statemap settemplate statemap setresponse statemap setmiddlewares statemap setactions statemap setdeps statemap setsession statemap metosinreitit wrapper explanation controller would wraped thin reitit wrapper initial approach elevates reitit already implemented functionality safeguard availability perform validation map gurantee correct definition stage exapmle controller result map clojure route get template functionpoccoretemp response header contenttype txthtml charset utf body nil middlewares action action select params deps session nil result map schema clojure internal schema instance statemap def instancemap map route vector respones map header list body string vector template string vector action vector enum select delete update insert map deps map middlewares list session map controller build route clojure defn buildcontroller ctrl defn generateroutes ctrl ringringhandler ringrouter api route ctrl data coercion reititcoercionspeccoercion middleware rrccoerceexceptionsmiddleware rrccoercerequestmiddleware rrccoerceresponsemiddleware