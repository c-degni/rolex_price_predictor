import React, {useState} from 'react';

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5000";

function App() {
    const [model, setModel] = useState("");
    const [year, setYear] = useState("");
    const [condition, setCondition] = useState("");
    const [prediction, setPrediction] = useState(null)
    const [imageUrl, setImageUrl] = useState(null)

    async function handleSubmit(e) {
        e.preventDefault();

        // Include real aws server ip once set up
        try {
            const response = await fetch(`${API_URL}/predict`, {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({model, year, condition})
            });

            if (!response.ok) {
                throw new Error("Failed to fetch prediction.");
            }

            const data = await response.json;
            setPrediction(data.predicted_price);
            setImageUrl(`${API_URL}/${data.image_url}`);
        } catch (error) {
            console.error("Error fetching prediction: ", error);
        }
    }

    return (
        <div>
            <h1>Rolex Price Predictor</h1>
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="Model" onChange={(e) => setModel(e.target.value)} required/>
                <input type="number" placeholder="Year" onChange={(e) => setYear(e.target.value)} required/>
                <input type="text" placeholder="Condition" onChange={(e) => setCondition(e.target.value)} required/>
                <button type="submit">Predict Price</button>
            </form>
            {prediction && <h2>Predicted Price: ${prediction}</h2>}
            {imageUrl && <img src={imageUrl} alt="Rolex Pricing Model" width="300"/>}
        </div>
    );
}

export default App;