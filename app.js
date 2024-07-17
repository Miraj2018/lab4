document.getElementById('predictionForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    let formData = new FormData(this);
    
    axios.post('/predict', formData)
        .then(function(response) {
            document.getElementById('predictionResult').textContent = `Predicted Species: ${response.data.prediction}`;
        })
        .catch(function(error) {
            console.error('Prediction error:', error);
        });
});
