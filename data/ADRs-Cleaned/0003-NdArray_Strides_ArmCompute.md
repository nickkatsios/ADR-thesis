libndj ndarray padded buffer stride armcompute library wrapper implemented proposed abdelrauf discussed integration process library armcompute faced ndarray stride flexible cant set properly without special manual handling let say array shape last index moving faster order stride far know last index stride different called overall stride follow cyclic strict rule dependency stridesindex stridesindex shapesindex armcompute besides stride also padding top right bottom left increase stride change offset adn well total size mostly done performance reason see hosting ndarray shape buffer bigger ndarray shape armcompute padding applied last dimension nchw define like newh padtop padbottom neww padleft padright stride calculated shape newh neww offset first element offset padleft strideofneww padtop strideofnewh proposal introduce helper function checking case stridesindex stridesindex shapesindex add generic method padded buffer simulate armcompute padding int paddingsrank total padding int paddingoffsetsrank offset index first element could padd ndarray shape calculate stride based keeping original shape paddoffsets could determine beginning first element though interface ismore generic drawback armcompute possible padd keeping rank one supply one dimension consequence test tested subarray could break require fix writing additional test case advantage alignment possibility cpu alignment required speed vectorization easier integration library case armcompute last two dimension sometimes padded disadvantage advantage big modern cpu unaligned vector load possible exposing user desirable excessive usage creates unnecessary memory space performance problem could result unnecessary complication function implementation possibility requiring additional test fix technical detail addition functionality ndarray little investigation showed current ndarray actually constructor specify stride constructor could shapedescriptorh addition shapedescriptor validate willbe validation stride cetera way create ndarray shapedescriptor alone flexible correctness alloclength return minimal buffer size given stride shape missing libndj side paddedbufferdescriptor helper method returning shapedescriptor padded buffer ndarrayfactory method shapedescriptor validation shapedescriptor paddedbuffer furthermore indicate shape ndarray paddedbuffer flag arrayhaspaddedbuffer possible know ndarray padded furthermore still possible recover padding allocation size padded ndarray easy task get paddingoffsets offset recovered full shape thats requires storing fortunately armcompute tensor manual padding know total size offset first element dont change internals much padded buffer follows strict rule instead loose one padding obtained rule stridesindex stridesindex shapesindex pseudo code order int rank shapesafterpaddingj stridesj stridesj shapesafterpadding bufferallocsize stride padding index rank paddingsindex shapesafterpaddingindex shapeindex technical note armcompute library main drive proposal avoid unnecessary performance memory allocation also keep mind newer version armcompute new implementation padding requirement removed diminish necessity proposed change version desired function implemented note armcompute tensor armcompute tensor mostly max dimension let show order ndarray shapeinfo shapeinfo float type armcompute tensor equivalent first map ndarray datatypes armcompute armcomputeutilscppll reversed shape ndarraynzyx tensorshapexyzn total length byte shape stride byte stride element padding armcompute tensor paddingleftright top bottom opencl neon vector load store instruction access data buffer order avoid special case handle border image tensor library must padded different way padding calculated accurate padding case importan configure allocate auto padding guarantee allocation enough padding run provided function padding manual padding padding affect stride offset total size armcompute tensor width height padded thats affect stride let show picture top left right width height bottom stride calculation pseudo code tensor xyz stridex elementsize float stridey paddingleft tensorshape paddingright stridex stridez paddingtop tensorshape paddingbottom stridey requiredoffsetfirstelement paddingleft stridex paddingtop stridey example armtensor padding left right top bottom total shape stride byte note current wrapper implementation simple wrapper arm function input output tensor armcomputeutilshll could see flag padded ndarrays manual padding version armcompute tensor padding information changed configure process copy ndarray buffer new allocated armtensor buffer output case without padding armtensor could buffer desired call configure run separately avoid multiple configure call discussed armcompute wrapper proposal conclude two creating ndarray autopadding stride modifying current wrapper still configure called foreach run auto padding memory small ndarrays able accurate padding properly call configure ndarray memory allocation import investigate graph declarableops ndarrays usage lifecycle auto padding kernel compute element time worst case scenario read value last element extrapadx tensorshapenumdimensions padx tensorshapenumdimensions pady tensorshapenumdimensions paddingsizepady padx extrapadx pady padx discussion