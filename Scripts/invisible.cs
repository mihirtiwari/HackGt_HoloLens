using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class invisible : MonoBehaviour {

    public Canvas canvas;
    public GameObject Controller;
    public float goodFactor = 0.5f;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
        GestureHandler gesture = new GestureHandler();
        if (GestureHandler.tookPic == false)
        {
            canvas.scaleFactor = 0;
        }
        else
        {
            canvas.scaleFactor = goodFactor;
        }
	}
}
