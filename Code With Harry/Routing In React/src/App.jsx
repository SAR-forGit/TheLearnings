import { useState } from 'react'
import './App.css'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import Navabar from './components/Navabar'
import home from './components/home'
import login from './components/login'
import about from './components/about'
import user from './components/user'

function App() {

  const router = createBrowserRouter([
    {
      path: "/",
      element: <><Navabar /><home /></>
    },
    {
      path: "/login",
      element: <><Navabar /><login /></>
    },
    {
      path: "/about",
      element: <><Navabar /><about /></>
    },
    {
      path: "/user:username",
      element: <><user /></>
    },

  ])

  return (
    <>
      <RouterProvider router={router} />
    </>
  )
}

export default App
