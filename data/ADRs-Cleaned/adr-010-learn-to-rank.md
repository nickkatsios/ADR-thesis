record learning rank search team decided implement learning rank learning rank motivation implementation success look like learning rank learning rank ltr application machine learning create ranking model improve search relevance common approach advanced search application ranking search result website frequently determined machine learning model example airbnb yelp wikipedia bloomberg commercial search engine good explanation ltr httpselasticsearchlearningtorankreadthedocsioenlatestcoreconceptshtml httpsopensourceconnectionscomblogwhatislearningtorank learning rank work easiest explain example say searched harry potter search api might return following result hmrc sign harry potter world pottery barn harry potter good result ass search quality assign relevancy judgement result query range irrelevant perfect example result query rating document harry potter hmrc sign harry potter harry potter world harry potter pottery barn harry potter harry potter ranking quality metric normalised discounted cumulative gain ndcg assign score list result ndcg tell good result might get score result set could investigate result bad perhaps best bet popularity might pushing hmrc doc fix thing check new ndcg score might get query contrast learning rank search result rank would determined machine learning model without manually changing boost field learning rank would process rating search result harry potter pottery barn harry potter harry potter however would train model data rank result better model optimises ndcg train model combination relevancy judgement feature numeric measure indicate well think result match query text similarity score elasticsearch assigns field document example feature model try find correlation document feature relevancy judgement allows predict order document dont relevancy judgement query rating document titlescore viewcount recency pagerank harry potter pottery barn harry potter harry potter example take training dataset query harry potter qid qid popularity titlescore descriptionscore recency pagerank qid popularity titlescore descriptionscore recency pagerank note format frequently learning rank training datasets including tensorflow ranking library detail format graded querydocument pair feature train model model might learn title description score slightly useful popularity recency much certain circumstance rather manually tuning boost model learns relevancy judgement role feature play providing relevant result high level overview learning rank case lot research area within field information retrieval machine learning learning rank intersects lot learn detail plan implement learning rank see implementation section motivation decided try learning rank potential greatly improve search relevance way automatable scalable maintainable successful automatable model wont require human involvement tune field boost latest user data scalable automation also model provide better result data maintainable relevancy tuning automated become stale successful result achieve higher ndcg score clickthrough rate achieve manual tuning alone problem manual relevancy tuning work doesnt scale well eventually process becomes game whackamole downgrade popularity boosting query might better result query might worse result handtuning relevance doesnt work well field boost complex difficult maintain moreover field boost might dependency document type might benefit stronger title boost document type instance expressing elasticsearch would prohibitively complex almost impossible maintain validating learning rank assumed would able get better result learning rank validate assumption worked spike validation spike found could build model provided better ndcg score current search algorithm query manually gathered relevancy judgement validated learning rank feasible could lead relevant result user though learning rank wont make relevance tuning easier could make search result relevant final feel confident implementing learning rank ltr following reason think improve search relevancy citizen enabling find govuk validated assumption spike ltr well trodden path organisation written implementation varying level openness wikimedia govuk implemented machine learning project success related link topic taxonomy data science team search team already worked tensorflow provides offtheshelf ranking module solves machine learning problem ltr manual relevancy tuning scalable wont get level relevancy ltr implementation plan decided implement learning rank following work started validation spike beginning project section may accurately reflect final implementation machine learning library decided tensorflows ranking library implementation learning rank tensorflow well supported ranking library active development considered elasticsearchlearningtorank plugin however aws elasticsearch permit install custom plugins also considered pytorch however would require writing much custom machine learning code pytorch dont currently ranking library make around following area may subject adrs language divide ruby python hosting trained model dockerised training data pipeline architecture computeintensive training happen failure resilience happens reranker process fails backup datasets model monitoring alert testingvalidating model would ltr change local development success look like success look like clickthrough rate top top result ndcg search latency increase much deploy model must provide better ctr ndcg hope project able remove complexity deleting boosting code search api