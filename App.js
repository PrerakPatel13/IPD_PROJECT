import React, { useState, useRef } from 'react';
import './App.css';
function App() {
  const [cameraOn, setCameraOn] = useState(false);
  const [imageUpload, setImageUpload] = useState(false);
  const [newlabel, setNewLabel] = useState('');
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const labelContainerRef = useRef(null);

  const startWebcam = async () => {
    setCameraOn(true);
    const constraints = {
      video: true,
      audio: false,
    };
  
    try {
      const stream = await navigator.mediaDevices.getUserMedia(constraints);
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
        videoRef.current.play();
      }
    } catch (error) {
      console.error('Error accessing webcam:', error);
    }
  };
  
  const stopWebcam = async () => {
    setCameraOn(false);
    if (videoRef.current && videoRef.current.srcObject) {
      const stream = videoRef.current.srcObject;
      if (stream) {
        const tracks = stream.getTracks();
        tracks.forEach((track) => track.stop());
      }
    }
  };
  
  const handleLoadImage = async () => {
    const fileUploadControl = document.getElementById('fruitimg');
    if (!imageUpload) {
      if (labelContainerRef.current) {
        labelContainerRef.current.removeChild(newlabel);
      }
      if (canvasRef.current) {
        canvasRef.current.remove();
      }
    }
  
    if (cameraOn) {
      alert('Please turn off the webcam and select an image instead.');
      return;
    }
  
    if (fileUploadControl.files.length > 0) {
      const file = fileUploadControl.files[0];
      const canvas = document.createElement('canvas');
      canvas.width = 224;
      canvas.height = 224;
      const context = canvas.getContext('2d');
  
      if (canvasRef.current) {
        document.getElementById('uploadedImage').appendChild(canvas);
      }
      if (labelContainerRef.current) {
        labelContainerRef.current.appendChild(newlabel);
      }
    }
  };

  return (
    <div>
      <div>
      <nav className="navbar navbar-dark" style={{ backgroundColor: '#000980' }}>
        <a className="navbar-brand title" href="#">
          Fruit Quality Detector
        </a>
      </nav>

      <div className="container" id="main">
        <div className="row justify-content-center">
          <div className="col-lg-10 col-md-12">
            <div className="card m-4">
              <div className="card-body" id="box-cont">
                <h3 className="card-title py-3 title" id="detect">Determine whether your fruit is fresh or rotten</h3>
                <p className="px-3">
                  You can choose only <span className="yellow">Banana</span>, <span className="orange">Orange</span> or 
                  <span className="red"> Apple</span> for testing.
                </p>
                <p className='px-3'>
                For doing so you can either use your web camera and show the fruit
                  or upload an image from your device.
                </p>
                <label htmlFor="webcam" className="ps-3 pt-3 pb-3">USE WEBCAM:</label>
                <button id="webcam" type="button" className="btn btn-outline-primary ms-3" onClick={cameraOn ? stopWebcam : startWebcam}>
                  {cameraOn ? 'Close Webcam' : 'Start Webcam'}
                </button>
                <br />
                <label className="p-3" htmlFor="fruitimg">UPLOAD IMAGE:</label>
                <div className="input-group px-3 pb-3" id="inputimg">
                  <input type="file" className="form-control" accept="image/*" id="fruitimg" />
                  <button className="btn btn-outline-primary" id="loadBtn">
                    Load
                  </button>
                </div>
                <div id="webcam-container" className="px-3"></div>
                <div id="uploadedImage" className="px-3"></div>
                <div id="label-container" className="px-3 pt-3"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
      <video id="webcam-container" ref={videoRef}></video>
      <div id="uploadedImage" ref={canvasRef}></div>
      <div id="label-container" ref={labelContainerRef}></div>
    </div>
  );
}

export default App;
