navigator.geolocation.getCurrentPosition(function(position){
    const lat=position.coords.latitude;
    const lon=position.coords.longitude;
    
    document.write(lat,lon);
    let url=`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${api}&units=metric`
    fetch(url)
         .then(response => response.json())
         .then(data => {
          console.log(data)
          if (data.cod===200){
             const description=data.weather[0].description;
             const wind=data.wind.speed;
             const temp = data.main.temp;
             const humidity=data.main.humidity;
             const h2=`weather in ${data.name} is:<br>`
             const information=`Weather: ${description}<br>Temperature: ${temp} degrees celsius.<br>Humidity: ${humidity}% <br>Wind speed: ${wind} m/s`;
             document.write(h2,information);
          }else{
              document.write(data.message);
          }
         })
         .catch(error =>{
             document.write(error);
         });
})
