import React, { useState, useEffect } from 'react'
import { NavLink } from 'react-router-dom'
import axios from 'axios'
 
 
const List = () => {
    const [potholeData, setPotholeData] = useState([]);
    useEffect(() => {
        fetchData()
    }, [])
 
    const fetchData = async () => {
        try {
            const result = await axios("http://127.0.0.1:5000/api/v1/potholes");
            
            setPotholeData(result.data)
        } catch (err) {
            console.log("somthing Wrong")
        }
    }
 
    
 
    return(
        <div className="container">
        <h3>Pothole Details</h3>
        <table className="table table-bordered">
            <thead>
                <tr>
                    <th>Pothole No.</th>
                    <th>Location</th>
                    <th>District</th>
                    <th>Longitude</th>
                    <th>Latitude</th>
                    
                </tr>
            </thead>
            <tbody>
                {
                    potholeData.map((pothole, i) => {
                        return (
                            <tr key={i}>
                                <td>{i + 1}</td>
                                <td>{pothole.location} </td>
                                <td>{pothole.district} </td>
                                <td>{pothole.longitude} </td>
                                <td>{pothole.latitude} </td>
                                <td>
                                    <NavLink to={`/view/${pothole.p_id}`} className="btn btn-success mx-2">View</NavLink>
                                    
                                </td>
                            </tr>
                        )
                    })
                }
 
            </tbody>
        </table>
        </div>
    );
};
 
export default List