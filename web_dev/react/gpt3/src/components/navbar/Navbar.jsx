import React, { useState } from 'react'
import { RiMenu3Line, RiCloseLine } from "react-icons/ri"
import "./navbar.css"
import logo from "../../assets/GPT-3.svg"

const Menu = () => (
  <>
    <p><a href="#home">Home</a></p>
    <p><a href="#wgpt">What is GPT-3?</a></p>
    <p><a href="#possibility">Open AI</a></p>
    <p><a href="#features">Case Studies</a></p>
    <p><a href="#blog">Library</a></p>
  </>
)

const Navbar = () => {
  const [toggleMenu, setToggleMenu] = useState(false);

  return (
    <div className='gpt-navbar gradient-bg'>
      <div className="gpt-nav-links">
        <img src={logo} alt="logo" className='gpt-logo' />
        <div className="text">
          <Menu />
        </div>
        <div className="gpt-nav-sign">
          <p><a href="#">Sign in</a></p>
          <button>Sign up</button>
        </div>
      </div>
      <div className="gpt-navbar-menu">
        {toggleMenu
          ? <RiCloseLine color='#fff' size={27} onClick={() => setToggleMenu(false)} />
          : <RiMenu3Line color='#fff' size={27} onClick={() => setToggleMenu(true)} />}
        {toggleMenu && (
          <div className="gpt-navbar-menu-container scale-up-center">
            <d className="gpt-navbar-menu-container-links">
              <Menu />
            </d>
            <div className="gpt-menu-container-sign">
              <p><a href="#">Sign in</a></p>
              <p><a href="#">Sign up</a></p>

            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default Navbar