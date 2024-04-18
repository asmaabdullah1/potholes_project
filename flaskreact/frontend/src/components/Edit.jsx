import React,{ useState, useEffect } from 'react'
import axios from 'axios'
import { useNavigate ,useParams } from 'react-router-dom'
 
const Edit = () => {
    const {p_id}=useParams()
    const navigate = useNavigate()
    const clickToBackHandler=()=>{
        navigate('/')
    }
 
    const [potholeField, setPotholeField] = useState({
        location: "",
        district: "",
        longitude: "",
        latitude: ""
    })
 
    useEffect(()=>{
        fetchPothole()
    },[p_id])
 
    const fetchPothole=async()=>{
        try{
            const result=await axios.get("http://127.0.0.1:5000/api/v2/potholedetails/"+p_id);
            
            setPotholeField(result.data)
        }catch(err){
            console.log("Something Wrong")
        }
    }
 
    const changePotholeFieldHandler = (e) => {
        setPotholeField({
            ...potholeField,
            [e.target.name]: e.target.value
        });
        console.log(potholeField);
    }
     
    
}
 
export default Edit