using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    private bool done_lerp = true;
    private float timedur = 2f;
    private float curtime = 0f;
    // Start is called before the first frame update
    void Start()
    {
        GetComponent<Renderer>().material.color = Random.ColorHSV(0f, 1f, 0f, 0.5f, 0.0f, 0.5f);
    }
    private void Update()
    {
        if (done_lerp)
        {
            transform.localPosition += (Time.deltaTime/2) * new Vector3(0, 0, 26);
            curtime += Time.deltaTime;
            if(curtime > timedur)
            {
                done_lerp = false;
            }
        }
    }
    // Update is called once per frame
    void FixedUpdate()
    {
        //transform.rotation *= Quaternion.Euler(new Vector3(0, Input.GetAxis("Horizontal")*3, 0));
        //transform.position += transform.TransformDirection(new Vector3(0, 0, Input.GetAxis("Vertical")));
    }
}
