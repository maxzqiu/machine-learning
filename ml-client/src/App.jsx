import { useState,useEffect } from 'react'
import './App.css'

function App() {
  let [data,setData]=useState([])
  let [input,setInput]=useState("Toy Story (1995)")
  let [number,setNumber]=useState(5);
  let [loading,setLoading]=useState("Waiting for a Valid Input");
  
    async function run(movie,top_k){
      const params = new URLSearchParams({
        "title":movie,
        "top_k":top_k
      })
      const options={
        method:"GET",
        headers:{
          "Content-Type":"application/json"
        },
        
      }
      let res = await fetch(`http://localhost:8000/api?${params}`,options)
      let json = await res.json()
      console.log(json)
      if (json[0]==400){
        alert("You have inputed an incorrect movie. Please try again:")
      }
      setLoading("")
      setData(json)
    }
    
   

  return (
    <>
      <h3>Movie Recommendations! </h3>
      <div className="one-line">
         <div className="input-css">
          <label htmlFor="movie-input">Enter Your Movie: </label>
          <input id="movie-input" onChange={(e)=>setInput(e.target.value)}></input>
          <p></p>
      </div>
      
      <br></br>
      <div className="input-css">
        <label  htmlFor="num-input">Enter Your Top K: </label>
        <input id="num-input" onChange={(e)=>setNumber(e.target.value)}></input>
        
      </div>
      </div>
     
      
      <br></br>
      <button className="button-css" onClick={()=>{
        setLoading("Status: Waiting for Valid Input")
        run(input,number)

        }}>Search</button>
      <h4>{loading}</h4>

      <h4><strong>Movie Recommendation Results:</strong> </h4>
      <table>
        <tbody>
            <tr>
              <th>Vector</th>
              <th>Movie Recommendation</th>
              <th>Movie Genres!</th>
            </tr>

          {data.map((i,key)=>{
            console.log(data)
            if (data[0]==400){

              return <tr key={key}>
                <td>---INVALID INPUT---</td>
              </tr>
            } else {
                return <tr key={key}>
              <td>{i[0]}</td>
              <td>{i[1]}</td>
              <td>{i[2].toString()}</td>
            </tr>
            }
            
          })}
        </tbody>
      </table>
    </>
  )
}

export default App
