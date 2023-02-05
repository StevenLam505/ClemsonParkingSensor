using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.Networking;
using Newtonsoft.Json;

[System.Serializable]
public class ParkingSpot
{
    public long spacid;
    public string lotname;
    public string spotname;
    public bool occupancy;
    public string spacecolor;
}
public class CameraMove : MonoBehaviour
{
    private PlayerInput input;
    private InputAction mouse;
    private InputAction click;
    private Vector3 init;
    public GameObject camera_p;
    public float webDelay = 10f;
    private int randomCars;
    private List<ParkingSpot> webList;
    // Start is called before the first frame update
    void Start()
    {
        input = GetComponent<PlayerInput>();
        mouse = input.actions["Turn"];
        click = input.actions["Click"];
        init = camera_p.transform.position;
   //     StartCoroutine(ChangeOccupancy());
        StartCoroutine(GetRequest("https://2zi3sm5r6e.execute-api.us-east-1.amazonaws.com/api/occupancy"));
    }

    // Update is called once per frame
    void Update()
    {
        if (click.ReadValue<float>() > 0.5)
        {
            transform.rotation *= Quaternion.Euler(new Vector3(0, mouse.ReadValue<Vector2>().x, 0));
        }
    }
//    private IEnumerator ChangeOccupancy()
//    {
//        yield return new WaitForSeconds(0.1f);
//        randomCars = Random.Range(0, 509);
//        GameObject.Find("A" + randomCars).GetComponent<ParkingSpace>().Occupied(Random.Range(0f, 1f) > 0.5 ? true:false);
//        GameObject.Find("A" + ((randomCars+50)%509)).GetComponent<ParkingSpace>().Occupied(Random.Range(0f, 1f) > 0.5 ? true : false);
//        StartCoroutine(ChangeOccupancy());

//    }
    IEnumerator GetRequest(string uri)
    {
        while (true)
        {
            using (UnityWebRequest webRequest = UnityWebRequest.Get(uri))
            {
                //webRequest.SetRequestHeader()
                // Request and wait for the desired page.
                yield return webRequest.SendWebRequest();
                switch (webRequest.result)
                {
                    case UnityWebRequest.Result.ConnectionError:
                    case UnityWebRequest.Result.DataProcessingError:
                        Debug.LogError(": Error: ");
                        break;
                    case UnityWebRequest.Result.ProtocolError:
                        Debug.LogError(": HTTP Error: ");
                        break;
                    case UnityWebRequest.Result.Success:
                        //Debug.Log(":\nReceived: " + webRequest.downloadHandler.text);
                        break;
                }
                GameObject parkingobj = null;
                ParkingSpace objref = null;
                webList = JsonConvert.DeserializeObject<List<ParkingSpot>>(webRequest.downloadHandler.text);
                foreach (ParkingSpot spot in webList)
                {
                    if (spot.lotname == "C-11")
                    {
                        parkingobj = GameObject.Find(spot.spotname);
                        if (parkingobj == null)
                        {
                            continue;
                        }
                        objref = parkingobj.GetComponent<ParkingSpace>();
                        objref.Occupied(spot.occupancy);
                        objref.SetColor(spot.spacecolor);

                    }
                }
            }
            yield return new WaitForSeconds(webDelay);
        }

    }
}
