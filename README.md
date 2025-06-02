# Team Won Website

This repository contains a web application that integrates machine learning models for image classification. The project consists of a Flask backend and a React frontend.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- Node.js and npm
- Git

## Setup Instructions

### 1. Clone the Repository
```bash
git clone [your-repository-url]
cd team_won_website
```

### 2. Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install flask
pip install flask-cors
pip install numpy
pip install Pillow
pip install joblib
pip install tensorflow
```

4. Download Model Files:
   - The model files (.pkl) are too large to be included in the repository
   - Download the following files from our shared drive: [Add your shared drive link here]
     - svm_model.pkl
     - logistic_regression_model.pkl
     - label_encoder.pkl
     - scaler.pkl
   - Place these files in the `backend` directory

5. Start the Flask server:
```bash
python app.py
```
The server will run on `http://localhost:5000`

### 3. Frontend Setup

1. Open a new terminal and navigate to the project root directory

2. Install frontend dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```
The website will be available at `http://localhost:5173`

## Project Structure

```
team_won_website/
├── backend/
│   ├── app.py
│   ├── svm_model.pkl
│   ├── logistic_regression_model.pkl
│   ├── label_encoder.pkl
│   └── scaler.pkl
├── src/
│   ├── components/
│   ├── pages/
│   └── ...
└── ...
```

## Usage

1. Ensure both the backend and frontend servers are running
2. Open your browser and navigate to `http://localhost:5173`
3. Upload an image through the web interface
4. The model will process the image and return the prediction

## Troubleshooting

- If you encounter any issues with the model files, ensure they are properly downloaded and placed in the backend directory
- Make sure both the backend and frontend servers are running simultaneously
- Check the console for any error messages

## Contributing

[Add contribution guidelines if applicable]

## License

[Add license information] 