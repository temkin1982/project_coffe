import { Routes, Route } from 'react-router-dom'

import Menu from './components/Menu'
import Home from './pages/Home'
import Login from './pages/Login'
import CoffeeList from './pages/CoffeeList'
import Register from './pages/Register'
import CoffeePage from './pages/CoffeePage'
import CreateCoffee from './pages/CreateCoffee'
import CoffeeSearch from './pages/CoffeeSearch'

import './App.css'

function App() {
  

  return (
    <>
      <Menu/>
      <Routes>
        <Route path='/' element={<Home/>} />
        <Route path='/login' element={<Login/>} />
        <Route path='/register' element={<Register/>} />
        <Route path='/search' element={<CoffeeSearch/>} />
        <Route path='/coffee' element={<CoffeeList/>} />
        <Route path='/coffee/:coffeeId' element={<CoffeePage/>} />
        <Route path='/coffee/new' element={<CreateCoffee/>} />
      </Routes>
    </>
  )
}

export default App
