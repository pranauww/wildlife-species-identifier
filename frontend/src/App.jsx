import { useState } from 'react';
import './App.css';

function App() {
  const [image, setImage] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleImageUpload = async (e) => {
    const file = e.target.files[0];
    if (file) {
      setImage(URL.createObjectURL(file));
      setError(null);
      setPrediction(null);
      setLoading(true);

      const formData = new FormData();
      formData.append('file', file);

      try {
        const response = await fetch('http://localhost:5000/predict', {
          method: 'POST',
          body: formData,
        });
        
        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.error || 'Failed to get prediction');
        }

        const data = await response.json();
        console.log('Received prediction:', data); // Debug log
        setPrediction({ species: data.prediction });
      } catch (err) {
        console.error('Error:', err); // Debug log
        setError(err.message || 'Error connecting to the server');
      } finally {
        setLoading(false);
      }
    }
  };

  return (
    <div className="app-container">
      <h1 className="title">
        Wildlife Species Detector
      </h1>

      <div className="card">
        <input
          type="file"
          accept="image/*"
          onChange={handleImageUpload}
          className="file-input"
        />
        {image && <img src={image} alt="Uploaded" className="uploaded-image" />}
        {loading && <p>Processing image...</p>}
        {error && <p style={{ color: 'red' }}>{error}</p>}
        {prediction && (
          <div className="prediction">
            <p className="species">Species: {prediction.species}</p>
          </div>
        )}
      </div>

      {/*About Section */}
      <div className="about-section">
        <h2>About the Project</h2>
        <p>
          This project was created to help identify wildlife species from trap camera images.
          Our machine learning model was trained on a diverse dataset to predict species
          using image classification. Upload an image to see what the model detects!
        </p>
      </div>

      <footer className="footer">
        • machine learning student network •
      </footer>
    </div>
  );
}

export default App;
