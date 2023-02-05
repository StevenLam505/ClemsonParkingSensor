function httpGet()
{
    url = 'https://2zi3sm5r6e.execute-api.us-east-1.amazonaws.com/api/trenddata';
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

function retrieveData()
{
    const obj = JSON.parse(httpGet());
    const capacityPercents = [];
    for(let i = 0; i < 53; i++){
        capacityPercents.push(obj[i]['occupancypct']);
    }
    console.log(capacityPercents);
}
