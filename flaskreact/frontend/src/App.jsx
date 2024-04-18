import {  } from 'react'
import './App.css'

import Home from "./components/Home"
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import View from "./components/View"
 
function App() {
  return (
    <div className="App">
        <Router>
            <Routes>
              <Route exact path="/" element={<Home/>}/>
              <Route exact path="/view/:p_id" element={<View/>}/>
              
            </Routes>
        </Router>
    </div>
  )
}
 
export default App
