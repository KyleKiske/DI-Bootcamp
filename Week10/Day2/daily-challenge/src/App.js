import './App.css';
import 'react-responsive-carousel/lib/styles/carousel.min.css'
import { Carousel } from 'react-responsive-carousel';

function App() {
  return (
    <div className="App" style={{width: "500px", margin: 'auto' }}>
        <Carousel>
          <div>
            <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Salzburg_%2848489551981%29.jpg/640px-Salzburg_%2848489551981%29.jpg'></img>
            <p className='legend'>Salzburg</p>
          </div>
          <div>
            <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/OlV_toren_en_Boerentoren_Antwerpen_vanaf_Linkeroever.jpg/640px-OlV_toren_en_Boerentoren_Antwerpen_vanaf_Linkeroever.jpg'></img>
            <p className='legend'>Antwerp</p>
          </div>
          <div>
            <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Salzburg_%2848489551981%29.jpg/640px-Salzburg_%2848489551981%29.jpg'></img>
            <p className='legend'>Kuala Lumpur</p>
          </div>
          <div>
            <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/View_of_Garden_Pier_from_the_Observation_Lounge_of_Nagoya_Port_Building%2C_Minato-machi_Minato_Ward_Nagoya_2022.jpg/640px-View_of_Garden_Pier_from_the_Observation_Lounge_of_Nagoya_Port_Building%2C_Minato-machi_Minato_Ward_Nagoya_2022.jpg'></img>
            <p className='legend'>Nagoya</p>
          </div>
        </Carousel>
    </div>
  );
}

export default App;
