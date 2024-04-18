import React, { useState } from 'react'
import List from './List'
import axios from 'axios'
 
const Home = () => {
 
    const [potholeField, setPotholeField] = useState({
        location: "",
        district: "",
        longitude: "",
        latitude:""
    })
 
    const changePotholeFieldHandler = (e) => {
        setPotholeField({
            ...potholeField,
            [e.target.name]: e.target.value
        })
        
 
    }
    const [loading,setLoading]=useState()

    return (
        <div className="container">
            <h2 className='w-100 d-flex justify-content-center p-3'>Pothole Detection Data in Riyadh</h2>
                <div className='row'>
                    <div className='col-md-4'>
                        
                    </div>
                    <div className='col-md-8'>
                        <List />
                    </div>
                </div>
        </div>
    )
}
 
export default Home