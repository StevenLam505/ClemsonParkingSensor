using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ParkingSpace : MonoBehaviour
{
    public string spaceName = "";
    public GameObject border;
    public GameObject car;
    private GameObject car_instance;
    public bool occupation = false;
    public string startcolor = "Green";
    private float opacity = 0.5f;
    // Start is called before the first frame update
    void Start()
    {
        if(spaceName == "")
        {
            spaceName = "A" + GameObject.Find("ParkingLot").GetComponent<ParkingManager>().count;
            GameObject.Find("ParkingLot").GetComponent<ParkingManager>().count++;
        }
        if (occupation)
        {
            car_instance = Instantiate(car, transform.position, transform.rotation, transform);
            car_instance.transform.position -= car_instance.transform.TransformDirection(new Vector3(0, 0, 30));
            border.SetActive(false);
        }
        SetColor(startcolor);
        gameObject.name = spaceName;
    }

    public void Occupied(bool occupied)
    {

        if (!occupation && occupied)
        {
            car_instance = Instantiate(car, transform.position, transform.rotation, transform);
            car_instance.transform.localPosition -= new Vector3(0, 0, 30);
            border.SetActive(false);
        }
        else if (occupation && !occupied)
        {
            border.SetActive(true);
            Destroy(transform.GetChild(1).gameObject);
        }
        occupation = occupied;
    }
    public void SetColor(string color)
    {
        if (color == "Orange")
        {
            border.GetComponent<MeshRenderer>().material.color = new Color(1, 124f/255f, 0, opacity);
        }
        else if (color == "Green")
        {
            border.GetComponent<MeshRenderer>().material.color = new Color(0, 1f, 0, opacity);
        }
        else if (color == "Purple")
        {
            border.GetComponent<MeshRenderer>().material.color = new Color(150f/255f, 0, 1f, opacity);
        }
        else if (color == "White")
        {
            border.GetComponent<MeshRenderer>().material.color = new Color(1f, 1f, 1f, opacity);
        }

    }
}
