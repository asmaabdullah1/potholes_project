import axios from 'axios'
import React, { useState, useEffect } from 'react'
import { useParams,useNavigate } from 'react-router-dom' 


const View = () => {
    const {p_id}=useParams()
    
    const[pothole,setPothole]=useState([])
    const navigate = useNavigate()
 
    useEffect(()=>{
        fetchPothole()
    },[p_id])
 
    const fetchPothole=async()=>{
        try{
        const result=await axios.get("http://127.0.0.1:5000/api/v1/potholedetails/"+p_id)
        console.log(result.data)
        setPothole(result.data)
 
        }catch(err){
            console.log("Something Wrong")
        }
    }
 
    const clickToBackHandler=()=>{
        navigate('/');
    }

    const imageData = `data:image/png;base64,${pothole.image}`;
 
    return <div>
        <div className="container">
            <div className='row'>
                <div className='col-md-12'>

                    <h1>Pothole Details</h1>
                    <table className="table">
                        <thead>
                            <tr>
                                <th>Pothole No.</th>
                                <th>Longitude</th>
                                <th>Latitude</th>
                                <th>Image</th>
                               
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>{pothole.p_id}</td>
                                <td>{pothole.longitude}</td>
                                <td>{pothole.latitude}</td>
                                <td><img src={imageData} alt="Pothole Image" /></td>
                            </tr>
 
                        </tbody>
                    </table>
                </div>
 
            </div>
        </div>
        <div className='container d-flex justify-content-center'>
            <div><button className='btn btn-primary' onClick={clickToBackHandler}>Back To Home</button></div>
        </div>
    </div>
}
 
export default View