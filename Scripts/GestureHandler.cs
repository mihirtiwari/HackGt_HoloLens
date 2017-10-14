using UnityEngine;
using UnityEngine.VR.WSA.Input;
using System.Linq;
using UnityEngine.VR.WSA.WebCam;
using System.Collections;

public class GestureHandler : MonoBehaviour
{
    //captured photo
    PhotoCapture photoCaptureObject = null;

    //captured targetTexture
    Texture2D targetTexture = null;

    //GestureHandler Instance
    public static GestureHandler Instance { get; private set; }

    //variable to see if a new picture was taken
    public static bool tookPic = true;


    //get tookPic
    bool getPic()
    {
        return tookPic;
    }

    //set tookPic's value to value
    void setPic(bool value)
    {
        tookPic = value;
    }


    // Represents the hologram that is currently being gazed at.
    //public GameObject FocusedObject { get; private set; }

    GestureRecognizer recognizer;

    //picture
    WebCamTexture webCamTexture;

    
    //Upload up= new Upload();

    //the final photo
    Texture2D photo;

    //url to upload to
    public string url = "http://www.something.com/";

    private void init()
    {
        //find and set resolution
        Resolution cameraResolution = PhotoCapture.SupportedResolutions.OrderByDescending((res) => res.width * res.height).First();

        //calculate target texture (fov of cam)
        targetTexture = new Texture2D(cameraResolution.width, cameraResolution.height);

        //get webCamTexture
        webCamTexture= new WebCamTexture();

        //capture a picture
        webCamTexture.Play();
        // Create a PhotoCapture object
        
    }

    //take_photo
    void TakePhoto()
    {
        Debug.Log("Inside take photo!Yay?\n");

        //set values of photo
        photo = new Texture2D(webCamTexture.width, webCamTexture.height);
        photo.SetPixels(webCamTexture.GetPixels());
        photo.Apply();
    }
    /*void OnCapturedPhotoToMemory(PhotoCapture.PhotoCaptureResult result, PhotoCaptureFrame photoCaptureFrame)
    {
        // Copy the raw image data into the target texture
        photoCaptureFrame.UploadImageDataToTexture(targetTexture);

        // Create a GameObject to which the texture can be applied
        GameObject quad = GameObject.CreatePrimitive(PrimitiveType.Quad);
        Renderer quadRenderer = quad.GetComponent<Renderer>() as Renderer;
        quadRenderer.material = new Material(Shader.Find("Custom/Unlit/UnlitTexture"));

        quad.transform.parent = this.transform;
        quad.transform.localPosition = new Vector3(0.0f, 0.0f, 3.0f);

        quadRenderer.material.SetTexture("_MainTex", targetTexture);

        // Deactivate the camera
        photoCaptureObject.StopPhotoModeAsync(OnStoppedPhotoMode);
    }

    void OnStoppedPhotoMode(PhotoCapture.PhotoCaptureResult result)
    {
        // Shutdown the photo capture resource
        photoCaptureObject.Dispose();
        photoCaptureObject = null;
    }*/

    // Use this for calling things
    void takeScreenShot()
    {
        if (!tookPic)           //check if pic has already been taken and just not handled
        {
            init();             //start taking picture
            StartCoroutine(UploadPNG(photo));           //start uploading picture
        }
        else
            Debug.Log("Waiting for server to return something");
    }


    //upload picture
    IEnumerator UploadPNG(Texture2D a)
    {
        byte[] bytes = a.EncodeToPNG();
        Debug.Log("Value="+bytes);
        yield return new WaitForEndOfFrame();
        WWWForm form = new WWWForm();
        form.AddBinaryData("image", bytes);
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


    //initialize things
    void Start()
    {
        Instance = this;

        // Set up a GestureRecognizer to detect Select gestures.
        recognizer = new GestureRecognizer();
        recognizer.TappedEvent += (source, tapCount, ray) =>
        {
            takeScreenShot();
            // Send an OnSelect message to the focused object and its ancestors.
            /*if (FocusedObject != null)
            {
                FocusedObject.SendMessageUpwards("OnSelect");
            }*/
        };

        //start capturing gestures
        recognizer.StartCapturingGestures();
    }

    // Update is called once per frame
    void Update()
    {
        // Figure out which hologram is focused this frame.
        //GameObject oldFocusObject = FocusedObject;

        // Do a raycast into the world based on the user's
        // head position and orientation.
        /*var headPosition = Camera.main.transform.position;
        var gazeDirection = Camera.main.transform.forward;

        RaycastHit hitInfo;
        if (Physics.Raycast(headPosition, gazeDirection, out hitInfo))
        {
            // If the raycast hit a hologram, use that as the focused object.
            FocusedObject = hitInfo.collider.gameObject;
        }
        else
        {
            // If the raycast did not hit a hologram, clear the focused object.
            //FocusedObject = null;
        }*/

        // If the focused object changed this frame,
        // start detecting fresh gestures again.
        /*if (FocusedObject != oldFocusObject)
        {
            recognizer.CancelGestures();
            recognizer.StartCapturingGestures();
        }*/
    }
}