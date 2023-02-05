function httpGet()
{
    url = 'https://2zi3sm5r6e.execute-api.us-east-1.amazonaws.com/api/trenddata';
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url, false ); // false for synchronous request
    xmlHttp.send( null );
    console.log(parseJson(xmlHttp.responseText));
    return xmlHttp.responseText;
}

function parseJson(jsonData)
{
    const obj = JSON.parse(jsonData);
    return obj;
}