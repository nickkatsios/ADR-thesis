dynamodb composite primary key design dynamodb table item attribute core component work table collection item item collection attribute dynamodb primary key uniquely identify item table secondary index provide querying flexibility two type primary key dynamodb first kind partition key partition key hash determines physical storage item placed partition key must unique second kind composite primary key consists partition key sort key partition key stay doesnt unique isolation rather sort key partition key pair must unique real system would probably push towards streamname partition key event logically live together physically live together event number stream sort key order item stored physical medium match order likely read introduces unwanted complexity time code tracking event number instead event number sort key introduce uuid eventid streamname hash key streamnames unique anyway consequence performance testing check significant impact item effectively randomly sorted