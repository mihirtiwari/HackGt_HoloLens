/*using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Upload : MonoBehaviour {
    public string url = "http://www.something.com/";
	// Use this for initialization
	void Start () {
        Texture2D abc = null;
        StartCoroutine(UploadPNG(abc));
	}

    IEnumerator UploadPNG(Texture2D a)
    {
        byte[] bytes = a.EncodeToPNG();
        yield return new WaitForEndOfFrame();
        WWWForm form= new WWWForm();
        form.AddBinaryData("image",bytes);
        WWW www = new WWW(url, form);
        yield return www;
        if (!string.IsNullOrEmpty(www.error))
        {
            print(www.error);
        }
        else
        {
            print("working");
        }

    }
	
	// Update is called once per frame
	void Update () {
		
	}
}
*/