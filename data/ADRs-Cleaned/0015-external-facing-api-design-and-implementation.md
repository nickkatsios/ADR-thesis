external facing api design implementation office head start expanding data sharing across internal system support tta hub would like make documented apis available external system reliable consistent secure way considered achieve two path considered expose existing internal apis tta hub robust set apis already implemented support react frontend pro already implemented well documented con api highly coupled tta hub become difficult change rapidly authentication based session stored browser cooky authorization fully limited existing tta hub role create new api layer external partner creating new api layer would decouple data tta hub pro existing api continue optimized consideration new api rigidly backwardscompatible authentication scheme easily customized authorization scopebased integrated full oauth implementation con two api endpoint maintained data model change new api layer chosen better set trade offs distinguish api flavor external api namespaced apiv route path authentication initial api client also utilizes singlesignon solution api authentication done passing token via authentication http header tta hub validate token verify user json format promote consistency external facing api conform jsonapi schema much possible first endpoint include object attribute may eventually migrate relationship tradeoff made due exponential growth required api endpoint object represented relationship section consequence result stable external api simple authentication logic maintaining agility uidriven internal api risk come undertaking maintaining second representation tta hub data